# Composio

Composio is an integration platform designed to seamlessly connect AI agents and Large Language Models (LLMs) with a wide array of tools and services. It enables developers to build, connect, and deploy integrations for various systems, including Customer Relationship Management (CRM), Human Resource Management (HRM), ticketing, productivity, and accounting systems, all with SOC Type II compliance. 

**Key Features:**

- **Extensive Tool Integration:** Composio supports over 150 tools, allowing AI agents to perform actions and subscribe to triggers across platforms like GitHub, Salesforce, Slack, and more. 

- **Managed Authentication:** It offers built-in authentication management, enabling engineers to handle user and agent authentication from a single dashboard, thereby reducing complexity. 

- **Framework and Model Agnostic:** Composio is compatible with various agentic frameworks and LLM providers, facilitating flexible integration through function calling. 

- **Enhanced Reliability:** The platform simplifies JSON structures, improves variable naming, and enhances error handling, resulting in a 30% increase in reliability. 

- **Security Compliance:** Composio is SOC Type II compliant, ensuring maximum security and protection of user data. 

**Use Cases:**

1. **Automated Code Review:** Developers can create AI agents that review and comment on pull requests by integrating GitHub tools, streamlining the code review process. 

2. **Intelligent Customer Support:** By connecting AI agents to CRM tools, businesses can provide efficient and personalized customer support, accessing relevant customer data and history. 

3. **Data Analysis and Visualization:** AI agents can be integrated with databases and data processing tools to perform analyses and generate visualizations, aiding in informed decision-making. 

4. **Automated Task Management:** Integrating with productivity tools like Trello or Asana, AI agents can automate task creation, assignment, and tracking, enhancing team productivity. 

By leveraging Composio, organizations can enhance the capabilities of their AI agents, leading to more efficient workflows and improved operational efficiency.

## Integrations

Composio integrates seamlessly with both CrewAI and LangGraph, enhancing their capabilities by providing access to a wide array of tools and services.

**Integration with CrewAI:**
Composio enables CrewAI agents to interact with various external applications. For instance, you can configure a CrewAI agent to star a GitHub repository using Composio's GitHub tools. This involves installing the necessary packages, connecting your GitHub account, and defining the agent's tasks and tools. 

**Integration with LangGraph:**
Similarly, Composio enhances LangGraph agents by allowing them to connect with multiple tools. For example, you can set up a LangGraph agent to star a GitHub repository by importing the required packages, fetching GitHub tools via Composio, and defining the agent's workflow. 

By integrating Composio with CrewAI and LangGraph, you can build robust AI agents capable of performing complex tasks across various platforms. 

## Integrating Composio with CrewAI

Composio enhances CrewAI by enabling seamless integration with a wide array of external applications, thereby expanding the capabilities of CrewAI agents. Here's a detailed guide on how to utilize Composio with CrewAI:

**1. Setting Up the Environment:**

- **Install Necessary Packages:**
  Begin by installing the `composio_crewai` package, which facilitates the integration between Composio and CrewAI.
  ```bash
  pip install composio_crewai
  ```

- **Authenticate and Configure Tools:**
  Use the Composio CLI to authenticate and configure the desired tools. For example, to integrate GitHub:
  ```bash
  composio-cli add github
  ```
  This command streamlines the authentication and configuration process, allowing CrewAI agents to interact with GitHub functionalities.

**2. Filtering Actions:**

Composio supports numerous actions for each integrated application. To enhance the accuracy of CrewAI agents, it's advisable to filter actions based on specific use cases.

- **Filter Actions by Use Case:**
  ```bash
  composio-cli get-actions github "Star a repository on GitHub" --limit=10
  ```
  This command retrieves actions related to starring a repository, ensuring the agent focuses on relevant tasks.

**3. Importing Base Packages:**

In your Python script, import the necessary packages to set up the language model and define the agent's tools.
```python
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI
from composio_crewai import ComposioToolSet, App
```

**4. Initializing the Language Model and Tools:**

- **Initialize the Language Model:**
  ```python
  llm = ChatOpenAI()
  ```

- **Fetch Tools via Composio:**
  ```python
  composio_toolset = ComposioToolSet()
  tools = composio_toolset.get_tools(apps=[App.GITHUB])
  ```
  This setup allows the agent to access GitHub tools through Composio.

**5. Defining and Executing the Agent:**

- **Define the Agent:**
  ```python
  crewai_agent = Agent(
      role="GitHub Agent",
      goal="You take action on GitHub using GitHub APIs",
      backstory="You are an AI agent responsible for taking actions on GitHub on the user's behalf.",
      verbose=True,
      tools=tools,
      llm=llm,
  )
  ```

- **Define the Task:**
  ```python
  task = Task(
      description="Star the repository 'composiohq/composio' on GitHub",
      agent=crewai_agent,
      expected_output="Confirm if the repository was starred successfully."
  )
  ```

- **Execute the Task:**
  ```python
  my_crew = Crew(agents=[crewai_agent], tasks=[task])
  result = my_crew.kickoff()
  print(result)
  ```
  This execution initiates the agent to perform the specified task using the integrated tools.

**6. Filtering Specific Actions or Apps:**

To restrict agents from using all available actions or tools, you can filter specific actions or applications:

- **Filter Specific Actions:**
  ```python
  composio_toolset = ComposioToolSet()
  tools = composio_toolset.get_tools(actions=[Action.GITHUB_CREATE_ISSUE])
  ```

- **Filter Specific Apps:**
  ```python
  composio_toolset = ComposioToolSet()
  tools = composio_toolset.get_tools(apps=[App.GITHUB])
  ```

By following these steps, you can effectively integrate Composio with CrewAI, enabling your agents to interact with external applications and perform complex tasks seamlessly.

For more detailed information and additional use cases, refer to the official Composio documentation: [Using Composio With CrewAI](https://docs.composio.dev/framework/crewai) 