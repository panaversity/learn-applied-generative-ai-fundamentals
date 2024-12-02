# Planning

[Planning](https://docs.crewai.com/concepts/planning)

In the CrewAI framework, **planning** is an optional feature that enhances the coordination and efficiency of AI agents, referred to as a "crew." When enabled, this feature allows the crew to devise a structured, step-by-step plan before executing tasks, ensuring a systematic approach to achieving the desired objectives.

**Key Components of Planning in CrewAI:**

1. **AgentPlanner Integration:**
   - Upon activation of the planning feature, all relevant information about the crew is transmitted to an `AgentPlanner`.
   - The `AgentPlanner` formulates a detailed plan, outlining the sequence and methodology for task execution.
   - This plan is appended to each task description, providing clear guidance for the agents. 

2. **Enabling the Planning Feature:**
   - To incorporate planning capabilities into a crew, set the `planning` parameter to `True` during the crew's initialization.
   - **Example:**
     ```python
     from crewai import Crew, Agent, Task, Process

     # Assemble your crew with planning capabilities
     my_crew = Crew(
         agents=self.agents,
         tasks=self.tasks,
         process=Process.sequential,
         planning=True,
     )
     ```
   - With this configuration, the crew will generate a plan before each iteration, enhancing task execution. 

3. **Customizing the Planning Language Model (LLM):**
   - CrewAI allows the specification of a custom language model for the planning process.
   - By setting the `planning_llm` parameter, developers can choose any available `ChatOpenAI` model.
   - **Example:**
     ```python
     from crewai import Crew, Agent, Task, Process
     from langchain_openai import ChatOpenAI

     # Assemble your crew with planning capabilities and custom LLM
     my_crew = Crew(
         agents=self.agents,
         tasks=self.tasks,
         process=Process.sequential,
         planning=True,
         planning_llm=ChatOpenAI(model="gpt-4o")
     )

     # Run the crew
     my_crew.kickoff()
     ```
   - This customization allows for flexibility in selecting the most suitable language model for planning tasks. 

**Benefits of Utilizing the Planning Feature:**

- **Structured Task Execution:** By establishing a clear plan, agents can follow a defined sequence, reducing ambiguity and enhancing efficiency.
- **Improved Coordination:** The planning process ensures that tasks are assigned and executed in a cohesive manner, promoting better collaboration among agents.
- **Enhanced Performance:** A well-devised plan can lead to more effective task completion, as agents operate with a clear understanding of their roles and objectives.

Incorporating the planning feature in CrewAI facilitates a more organized and efficient approach to task management, leveraging the capabilities of AI agents to achieve complex goals systematically. 