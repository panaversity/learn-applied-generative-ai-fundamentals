# Knowledge

[Knowledge Docs](https://docs.crewai.com/concepts/knowledge)

CrewAI's "Knowledge" feature is designed to enhance AI agents by providing them with access to structured data sources, enabling more informed and contextually relevant responses. This functionality allows agents to query and retrieve information from various formats, such as text files, PDFs, and spreadsheets, thereby enriching their interactions and decision-making processes. 

**Key Components of CrewAI's Knowledge Feature:**

1. **Knowledge Class:** Acts as a manager for different information sources, facilitating seamless integration of diverse data formats into AI workflows. 

2. **Knowledge Sources:** These are the actual data inputs, which can include strings, text files, PDFs, and spreadsheets. Developers can extend the `KnowledgeSource` class to support additional data types as needed. 

**Implementing Knowledge in CrewAI:**

To utilize the Knowledge feature, developers can create knowledge sources and associate them with AI agents. This setup enables agents to access and leverage the information during task execution.

**Example:**

```python
from crewai import Agent, Task, Crew, Process
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

# Create a knowledge source
content = "User's name is John. He is 30 years old and lives in San Francisco."
string_source = StringKnowledgeSource(
    content=content,
    metadata={"preference": "personal"}
)

# Create an agent with the knowledge store
agent = Agent(
    role="About User",
    goal="You know everything about the user.",
    backstory="You are a master at understanding people and their preferences.",
    verbose=True
)

task = Task(
    description="Answer the following questions about the user: {question}",
    expected_output="An answer to the question.",
    agent=agent,
)

crew = Crew(
    agents=[agent],
    tasks=[task],
    verbose=True,
    process=Process.sequential,
    knowledge={"sources": [string_source], "metadata": {"preference": "personal"}},
)

# Execute the crew
crew.kickoff()
```

In this example:

- A `StringKnowledgeSource` is created containing personal information about a user.
- An agent is defined with the role of understanding the user, utilizing the provided knowledge source.
- A task is assigned to the agent to answer questions about the user based on the available knowledge.

By integrating the Knowledge feature, AI agents in CrewAI can perform tasks with a deeper understanding of the context, leading to more accurate and relevant outcomes.  