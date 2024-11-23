from crewai import Agent, Task, Crew, Process

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

def createPoemCrew()->Crew:

    # Initialize the Gemini LLM
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        verbose=True,
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )


    #https://docs.crewai.com/concepts/agents#creating-an-agent
    poem_writer: Agent = Agent(
    role='CrewAI Poem Writer',
    goal="""Generate a funny, light heartedpoem about how CrewAI is
            awesome with a sentence count of {sentence_count}""",
    backstory="""You're a creative poet with a talent for capturing the essence of any topic
        in a beautiful and engaging way. Known for your ability to craft poems that
        resonate with readers, you bring a unique perspective and artistic flair to
        every piece you write.""",
    llm=llm,
    allow_delegation=True,
    verbose=True,
    memory=True
    )

    #https://docs.crewai.com/concepts/tasks#creating-a-task
    write_poem: Task = Task(
        description="""Write a poem about how CrewAI is awesome.
        Ensure the poem is engaging and adheres to the specified 
        sentence count of {sentence_count}.""",
        agent=poem_writer,
        expected_output='A beautifully crafted poem about CrewAI, with exactly {sentence_count} sentences.',
    )

    #https://docs.crewai.com/concepts/crews
    return Crew(
                agents=[poem_writer], # Automatically created by the @agent decorator
                tasks=[write_poem], # Automatically created by the @task decorator
                process=Process.sequential,
                verbose=True,
            )
