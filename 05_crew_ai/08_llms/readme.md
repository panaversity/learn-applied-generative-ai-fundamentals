# [LLMs](https://docs.crewai.com/concepts/llms)

We use Google Gemini Flash LLM for our courses, therefore we will start my learning to configure it.

Note: We have also updated the poemflow project in the directory poemflow to use Goolge Gemini Flash.

## Google Gemini Flash

To integrate Google's Gemini API with CrewAI, follow these steps:

**1. Obtain the Google Gemini API Key**

- Visit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) and sign in with your Google account.
- Create a new project or select an existing one.
- Generate an API key for the Gemini API.

**2. Install Required Packages**

Ensure you have the necessary Python packages installed:

```bash
pip install langchain-google-genai
```

**3. Configure Environment Variables**

Store your API key securely using environment variables. Create a `.env` file in your project directory with the following content:

```
GOOGLE_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with the API key obtained earlier.

**4. Set Up the Language Model in CrewAI**

In your Python script, configure the Gemini language model:

```python
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

**5. Define Agents with the Gemini LLM**

Create agents in CrewAI that utilize the configured Gemini LLM:

```python
# Define a researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking topics in {topic}",
    backstory="Driven by curiosity, you are at the forefront of innovation, sharing knowledge and news that would change the world.",
    tools=[],
    llm=llm,
    allow_delegation=True,
    verbose=True,
    memory=True
)

# Define a writer agent
writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    backstory="Your expertise lies in breaking down complex topics into simpler and digestible knowledge, captivating the audience with engaging narratives.",
    tools=[],
    llm=llm,
    allow_delegation=False,
    verbose=True,
    memory=True
)
```

**6. Execute Tasks with the Agents**

Assign tasks to the agents and execute them:

```python
from crewai import Task, Crew, Process

# Define tasks
research_task = Task(
    description="Identify the next big trend in {topic}. Focus on pros and cons and the overall narrative.",
    expected_output="A comprehensive 3-paragraph report on the latest AI trends.",
    tools=[],
    agent=researcher
)

write_task = Task(
    description="Compose an insightful article on {topic}, focusing on the latest trends and their impact on the industry.",
    expected_output="A 4-paragraph article on {topic} advancements formatted as markdown.",
    tools=[],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
)

# Create a crew and execute tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)
```

By following these steps, you can effectively integrate Google's Gemini API with CrewAI to build collaborative AI agents. For more detailed information, refer to the [CrewAI documentation on LLMs](https://docs.crewai.com/concepts/llms). 



## LLM Overview

Configuring Large Language Models (LLMs) for agents in CrewAI involves several steps to ensure that each agent operates with the desired model and settings. Here’s a comprehensive guide to achieve this:

1. Understanding LLM Configuration in CrewAI

In CrewAI, agents utilize LLMs to perform tasks. By default, CrewAI uses the gpt-4o-mini model. However, you can customize this by specifying different models and settings either through environment variables or directly within your code.

2. Setting Environment Variables

Environment variables allow you to define default settings for LLMs without hardcoding them into your application. This approach is beneficial for managing configurations across different environments.
	•	Default Model Configuration:
By default, CrewAI uses the gpt-4o-mini model. You can set this using the OPENAI_MODEL_NAME environment variable:

export OPENAI_MODEL_NAME="gpt-4o-mini"


	•	Additional Environment Variables:
Depending on the LLM provider, you may need to set additional variables:

export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="https://api.your-provider.com/v1"

Replace "your-api-key" and "https://api.your-provider.com/v1" with your actual API key and base URL.

3. Configuring Agents with Specific LLMs

You can assign specific LLMs to agents by updating the agents.yml configuration file or by setting the llm attribute directly in your code.
	•	Using agents.yml:
Modify the agents.yml file to specify the LLM for each agent:

researcher:
  role: Research Specialist
  goal: Conduct comprehensive research and analysis
  backstory: A dedicated research professional with years of experience
  verbose: true
  llm: openai/gpt-4o

Ensure that the llm field corresponds to the desired model.

	•	Directly in Code:
Alternatively, set the llm attribute when initializing an agent:

from crewai import Agent

agent = Agent(
    role='Research Specialist',
    goal='Conduct comprehensive research and analysis',
    backstory='A dedicated research professional with years of experience',
    llm='openai/gpt-4o'
)



4. Customizing LLM Parameters

CrewAI allows you to fine-tune LLM behavior by setting various parameters:
	•	Temperature: Controls randomness in output (0.0 to 1.0).
	•	Top_p: Controls diversity of output (0.0 to 1.0).
	•	Max_tokens: Maximum number of tokens to generate.
	•	Presence_penalty: Penalizes new tokens based on their presence in prior text.
	•	Frequency_penalty: Penalizes new tokens based on their frequency in prior text.

You can set these parameters when initializing the LLM:

from crewai import LLM

llm = LLM(
    model="gpt-4",
    temperature=0.8,
    max_tokens=150,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    api_key="your-api-key",
    base_url="https://api.openai.com/v1"
)

Then, assign this LLM to an agent:

agent = Agent(
    role='Research Specialist',
    goal='Conduct comprehensive research and analysis',
    backstory='A dedicated research professional with years of experience',
    llm=llm
)

5. Connecting to Different LLM Providers

CrewAI supports integration with various LLM providers, including OpenAI, Azure, Anthropic, and local models via Ollama. Each provider may require specific configurations:
	•	OpenAI-Compatible LLMs:
Set the following environment variables:

export OPENAI_API_KEY="your-api-key"
export OPENAI_API_BASE="https://api.your-provider.com/v1"


	•	Azure OpenAI:
Set these environment variables:

export AZURE_API_KEY="your-api-key"
export AZURE_API_BASE="https://example.openai.azure.com/"
export AZURE_API_VERSION="2024-08-01-preview"

Then, configure the agent in agents.yml:

researcher:
  role: Research Specialist
  goal: Conduct comprehensive research and analysis
  backstory: A dedicated research professional with years of experience
  llm: azure/gpt-4o-mini

For detailed guidance, refer to CrewAI’s documentation on configuring Azure OpenAI. ￼

	•	Local Models via Ollama:
Set the following environment variables:

export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_MODEL_NAME="openhermes"
export OPENAI_API_KEY=""

Ensure that Ollama is running locally and serving the specified model.

6. Best Practices
	•	Choose the Right Model: Balance capability and cost based on your application’s needs.
	•	Optimize Prompts: Clear, concise instructions improve output quality.
	•	Manage Tokens: Monitor and limit token usage for efficiency.
	•	Adjust Temperature: Lower values for factual tasks, higher for creative ones.
	•	Implement Error Handling: Gracefully manage API errors and rate limits.

By following these steps, you can effectively configure LLMs for agents in CrewAI, tailoring their behavior to meet your specific requirements.

## Google Gemini

To integrate Google's Gemini API with CrewAI, follow these steps:

**1. Obtain the Google Gemini API Key**

- Visit [Google AI Studio](https://ai.google.dev/gemini-api/docs/api-key) and sign in with your Google account.
- Create a new project or select an existing one.
- Generate an API key for the Gemini API.

**2. Install Required Packages**

Ensure you have the necessary Python packages installed:

```bash
pip install crewai langchain-google-genai
```

**3. Configure Environment Variables**

Store your API key securely using environment variables. Create a `.env` file in your project directory with the following content:

```
GOOGLE_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with the API key obtained earlier.

**4. Set Up the Language Model in CrewAI**

In your Python script, configure the Gemini language model:

```python
import os
from dotenv import load_dotenv
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    verbose=True,
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
```

**5. Define Agents with the Gemini LLM**

Create agents in CrewAI that utilize the configured Gemini LLM:

```python
# Define a researcher agent
researcher = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking topics in {topic}",
    backstory="Driven by curiosity, you are at the forefront of innovation, sharing knowledge and news that would change the world.",
    tools=[],
    llm=llm,
    allow_delegation=True,
    verbose=True,
    memory=True
)

# Define a writer agent
writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    backstory="Your expertise lies in breaking down complex topics into simpler and digestible knowledge, captivating the audience with engaging narratives.",
    tools=[],
    llm=llm,
    allow_delegation=False,
    verbose=True,
    memory=True
)
```

**6. Execute Tasks with the Agents**

Assign tasks to the agents and execute them:

```python
from crewai import Task, Crew, Process

# Define tasks
research_task = Task(
    description="Identify the next big trend in {topic}. Focus on pros and cons and the overall narrative.",
    expected_output="A comprehensive 3-paragraph report on the latest AI trends.",
    tools=[],
    agent=researcher
)

write_task = Task(
    description="Compose an insightful article on {topic}, focusing on the latest trends and their impact on the industry.",
    expected_output="A 4-paragraph article on {topic} advancements formatted as markdown.",
    tools=[],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
)

# Create a crew and execute tasks
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential
)

result = crew.kickoff(inputs={"topic": "AI in healthcare"})
print(result)
```

By following these steps, you can effectively integrate Google's Gemini API with CrewAI to build collaborative AI agents. For more detailed information, refer to the [CrewAI documentation on LLMs](https://docs.crewai.com/concepts/llms). 