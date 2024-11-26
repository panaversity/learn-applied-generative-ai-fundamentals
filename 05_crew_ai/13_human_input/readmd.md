# Human Input on Execution

[Official Documentation](https://docs.crewai.com/how-to/human-input-on-execution)

Integrating human input into CrewAI's agent execution enhances the system's adaptability and accuracy, especially when dealing with complex or ambiguous tasks. This integration allows agents to solicit additional information or clarification from users before finalizing their outputs.

**Steps to Integrate Human Input in CrewAI:**

1. **Enable Human Input in Task Definition:**
   To allow an agent to request user input during task execution, set the `human_input` flag to `True` in the task's definition. This configuration prompts the agent to seek additional information from the user before delivering its final response. 

   Example:
   ```python
   from crewai import Task

   my_task = Task(
       description="Analyze the provided data and generate a report.",
       human_input=True,
       # other task parameters
   )
   ```

2. **Implement Human Input Handling:**
   When `human_input` is enabled, the agent will pause execution to request input from the user. This input can provide additional context, clarify ambiguities, or validate the agent's output. 

   Example:
   ```python
   def handle_human_input(prompt):
       user_input = input(prompt)
       return user_input
   ```

3. **Configure the Agent to Use Human Input:**
   Assign the human input handling function to the agent, enabling it to call this function when needed during task execution.

   Example:
   ```python
   from crewai import Agent

   my_agent = Agent(
       role='Data Analyst',
       goal='Generate accurate data reports.',
       human_input_function=handle_human_input,
       # other agent parameters
   )
   ```

4. **Execute the Task with Human Input:**
   Initiate the task execution. During the process, the agent will prompt the user for input at designated points, incorporating the provided information into its workflow.

   Example:
   ```python
   from crewai import Crew

   my_crew = Crew(
       agents=[my_agent],
       tasks=[my_task],
       # other crew parameters
   )

   response = my_crew.kickoff()
   print(response)
   ```

**Benefits of Integrating Human Input:**

- **Enhanced Accuracy:** Human input provides additional context, leading to more precise outputs.
- **Clarification of Ambiguities:** Users can clarify uncertainties, ensuring the agent's understanding aligns with the user's intent.
- **Validation:** Human input serves as a validation step, confirming the agent's output before finalization.

**Considerations:**

- **User Interface:** Ensure that the system's interface facilitates seamless human-agent interactions, allowing users to provide input efficiently.
- **Task Complexity:** Implement human input for tasks where human oversight is critical to ensure accuracy and quality.
- **Asynchronous Execution:** Utilize asynchronous execution to improve efficiency and handle multiple tasks simultaneously.

By integrating human input into CrewAI's agent execution, you can create a more interactive and adaptable AI system capable of handling complex tasks with greater accuracy. 