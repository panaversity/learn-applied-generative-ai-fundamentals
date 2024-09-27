import operator
from typing import Annotated
from typing_extensions import TypedDict

from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

from langgraph.graph.state import CompiledStateGraph
from langchain_google_genai import ChatGoogleGenerativeAI


from langgraph.constants import Send
from langgraph.graph import END, StateGraph, START

# Prompts we will use
subjects_prompt: str = """
You are a smart assistant that generates sub-topics for a given topic. You must return the sub-topics in valid JSON format, with a key `"subjects"` and the value as a list of three related sub-topics.

Each sub-topic should be a short, clear, and related concept or idea. The output should be formatted like this:
{{
  "subjects": ["sub-topic1", "sub-topic2", "sub-topic3"]
}}

Here are some examples:

Example 1:
Topic: "Technology"
Response: {{
  "subjects": ["Artificial Intelligence", "Blockchain", "Quantum Computing"]
}}

Example 2:
Topic: "Sports"
Response: {{
  "subjects": ["Soccer", "Basketball", "Tennis"]
}}

Example 3:
Topic: "Music"
Response: {{
  "subjects": ["Jazz", "Classical", "Pop"]
}}

Now, generate a list of 3 sub-topics that are related to this overall topic:
Topic: "{topic}"

Return the output as valid JSON, exactly like the examples above, with the key `"subjects"` and the value as a list of strings.
"""

joke_prompt: str = """Generate a joke about {subject}. Make it crunchy and enjoyable"""

best_joke_prompt: str = """Below are a bunch of jokes about {topic}. Select the best one! Return the ID of the best one, starting 0 as the ID for the first joke. Jokes: \n\n  {jokes}

Return in JSON format. The output should be formatted like this:
{{
  "id": 0
}}
"""

# LLM
model: ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Define the state
class Subjects(BaseModel):
    subjects: list[str]

class BestJoke(BaseModel):
    id: int
    
class OverallState(TypedDict):
    topic: str
    subjects: list
    jokes: Annotated[list, operator.add]
    best_selected_joke: str

def generate_topics(state: OverallState) -> Subjects:
    print("generate_topics_state", state)
    prompt = subjects_prompt.format(topic=state["topic"])

    response = model.invoke(prompt)
    # Parse the response
    parsed_response = PydanticOutputParser(pydantic_object=Subjects).parse(response.content)

    return {"subjects": parsed_response.subjects}

class JokeState(TypedDict):
    subject: str

class Joke(BaseModel):
    joke: str

def generate_joke(state: JokeState) -> list[Joke]:
    prompt = joke_prompt.format(subject=state["subject"])
    response = model.with_structured_output(Joke).invoke(prompt)
    return {"jokes": [response.joke]}

def best_joke(state: OverallState):
    print("best_joke_OverallState", state)
    jokes = "\n\n".join(state["jokes"])
    prompt = best_joke_prompt.format(topic=state["topic"], jokes=jokes)
    # response = model.with_structured_output(BestJoke).invoke(prompt)
    response = model.invoke(prompt)
    # print(response.content)
    parsed_response = PydanticOutputParser(pydantic_object=BestJoke).parse(response.content)
    # print(parsed_response)
    return {"best_selected_joke": state["jokes"][parsed_response.id]}

def continue_to_jokes(state: OverallState):
    return [Send("generate_joke", {"subject": s}) for s in state["subjects"]]

# Construct the graph: here we put everything together to construct our graph
graph_builder: StateGraph = StateGraph(OverallState)
graph_builder.add_node("generate_topics", generate_topics)
graph_builder.add_node("generate_joke", generate_joke)
graph_builder.add_node("best_joke", best_joke)
graph_builder.add_edge(START, "generate_topics")
graph_builder.add_conditional_edges("generate_topics", continue_to_jokes, ["generate_joke"])
graph_builder.add_edge("generate_joke", "best_joke")
graph_builder.add_edge("best_joke", END)

# Compile the graph
graph: CompiledStateGraph = graph_builder.compile()
