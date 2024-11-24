# [Processes](https://docs.crewai.com/concepts/processes)

In CrewAI, processes define the strategy by which tasks are managed and executed by agents. Currently, CrewAI supports two primary process types: Sequential and Hierarchical. A third process type, Consensual, is planned for future development. This tutorial provides an in-depth look at each process type, including their characteristics, implementation, and use cases.

## 1. Sequential Process

**Overview:**
The Sequential Process ensures that tasks are executed in a predefined, linear order. Each task begins only after the preceding one has been completed, making this approach ideal for workflows where tasks must follow a specific sequence.

**Key Features:**
- **Linear Task Flow:** Tasks are handled in a predetermined sequence, ensuring orderly progression.
- **Simplicity:** Best suited for projects with clear, step-by-step tasks.
- **Easy Monitoring:** Facilitates straightforward tracking of task completion and project progress.

**Implementation:**
To implement a Sequential Process in CrewAI, define your agents and tasks in the order they should be executed. Here's an example:

```python
from crewai import Agent, Task, Crew, Process

# Define agents
researcher = Agent(
    role='Researcher',
    goal='Conduct foundational research',
    backstory='An experienced researcher with a passion for uncovering insights'
)
analyst = Agent(
    role='Data Analyst',
    goal='Analyze research findings',
    backstory='A meticulous analyst with a knack for uncovering patterns'
)
writer = Agent(
    role='Writer',
    goal='Draft the final report',
    backstory='A skilled writer with a talent for crafting compelling narratives'
)

# Define tasks
research_task = Task(
    description='Gather relevant data...',
    agent=researcher,
    expected_output='Raw Data'
)
analysis_task = Task(
    description='Analyze the data...',
    agent=analyst,
    expected_output='Data Insights'
)
writing_task = Task(
    description='Compose the report...',
    agent=writer,
    expected_output='Final Report'
)

# Form the crew with a sequential process
report_crew = Crew(
    agents=[researcher, analyst, writer],
    tasks=[research_task, analysis_task, writing_task],
    process=Process.sequential
)

# Execute the crew
result = report_crew.kickoff()
```

**Workflow in Action:**
1. **Initial Task:** The first agent completes their task and signals completion.
2. **Subsequent Tasks:** Each following agent begins their task based on the completion of the previous one.
3. **Completion:** The process concludes once the final task is executed, leading to project completion.

**Use Cases:**
The Sequential Process is ideal for projects requiring tasks to be completed in a specific order, such as data analysis pipelines, content creation workflows, or any scenario where each step depends on the previous one.

## 2. Hierarchical Process

**Overview:**
The Hierarchical Process introduces a structured approach to task management, emulating traditional organizational hierarchies. In this setup, a 'manager' agent coordinates the workflow, delegates tasks, and validates outcomes, ensuring streamlined and effective execution.

**Key Features:**
- **Task Delegation:** A manager agent allocates tasks among crew members based on their roles and capabilities.
- **Result Validation:** The manager evaluates outcomes to ensure they meet the required standards.
- **Efficient Workflow:** Emulates corporate structures, providing an organized approach to task management.

**Implementation:**
To utilize the Hierarchical Process, set the `process` attribute to `Process.hierarchical` and define a manager agent. Here's an example:

```python
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Define agents
researcher = Agent(
    role='Researcher',
    goal='Conduct in-depth analysis',
    backstory='Experienced data analyst with a knack for uncovering hidden trends.'
)
writer = Agent(
    role='Writer',
    goal='Create engaging content',
    backstory='Creative writer passionate about storytelling in technical domains.'
)

# Define tasks
# Tasks are not pre-assigned in hierarchical processes; the manager assigns them dynamically

# Establish the crew with a hierarchical process
project_crew = Crew(
    agents=[researcher, writer],
    process=Process.hierarchical,
    manager_llm=ChatOpenAI(model="gpt-4")  # Specify the manager language model
)

# Execute the crew
result = project_crew.kickoff()
```

**Workflow in Action:**
1. **Task Assignment:** The manager assigns tasks strategically, considering each agent’s capabilities.
2. **Execution and Review:** Agents complete their tasks, and the manager reviews the outcomes to ensure quality.
3. **Sequential Task Progression:** Tasks follow a logical order for smooth progression, facilitated by the manager’s oversight.

**Use Cases:**
The Hierarchical Process is suitable for complex projects requiring dynamic task allocation, such as large-scale research projects, content production teams, or any scenario where oversight and quality control are essential.

## 3. Consensual Process (Planned)

**Overview:**
The Consensual Process is a planned feature aimed at achieving collaborative decision-making among agents. This process type introduces a democratic approach to task management within CrewAI, where agents collectively decide on task execution strategies.

**Key Features:**
- **Collaborative Decision-Making:** Agents discuss and agree on task assignments and execution plans.
- **Democratic Workflow:** Emphasizes equal participation from all agents in the decision-making process.
- **Flexibility:** Allows for adaptive strategies based on collective intelligence.

**Implementation:**
As the Consensual Process is still under development, specific implementation details are not yet available. Future updates to CrewAI will provide comprehensive guidance on utilizing this process type.

**Use Cases:**
The Consensual Process will be ideal for projects that benefit from collaborative planning and decision-making, such as brainstorming sessions, strategic planning, or any scenario where diverse perspectives enhance the outcome.

## Conclusion

Understanding and implementing the appropriate process type in CrewAI is crucial for optimizing task execution and achieving project goals efficiently. The Sequential Process offers a straightforward, linear workflow, while the Hierarchical Process provides structured oversight and dynamic task allocation. The upcoming Consensual Process aims to introduce collaborative decision-making capabilities, further enhancing CrewAI's versatility.
