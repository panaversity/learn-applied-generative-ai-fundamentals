# [Flows Final Output](https://docs.crewai.com/concepts/flows#flow-output)

In CrewAI Flows, obtaining the final output of a workflow is straightforward and involves the following steps:

1. **Define the Flow Class**: Create a class that inherits from `Flow`, encapsulating the workflow's logic.

2. **Implement Methods with Decorators**:
   - Use the `@start()` decorator to mark the initial method(s) that kick off the workflow.
   - Utilize the `@listen()` decorator to define methods that respond to the completion of other tasks, establishing the sequence of operations.

3. **Execute the Flow**: Instantiate the Flow class and invoke the `kickoff()` method to start the workflow.

4. **Retrieve the Final Output**: The `kickoff()` method returns the output of the last method executed in the workflow, which is considered the final output.

**Example:**

```python
from crewai.flow.flow import Flow, listen, start

class ExampleFlow(Flow):
    @start()
    def initial_task(self):
        # Implementation of the initial task
        return "Initial task output"

    @listen(initial_task)
    def subsequent_task(self, input_data):
        # Process the input_data
        processed_data = input_data + " processed"
        return processed_data

    @listen(subsequent_task)
    def final_task(self, processed_data):
        # Further processing
        final_result = processed_data + " and finalized"
        return final_result

# Instantiate and execute the flow
flow = ExampleFlow()
final_output = flow.kickoff()
print("Final Output:", final_output)
```

**Explanation:**

- `initial_task` is marked with `@start()`, making it the entry point of the workflow.

- `subsequent_task` listens to the completion of `initial_task` and processes its output.

- `final_task` listens to `subsequent_task` and produces the final result.

- When `flow.kickoff()` is called, the workflow executes in the defined sequence, and the final output is obtained from `final_task`.

**Key Points:**

- The `kickoff()` method initiates the workflow and returns the output of the last executed method.

- The sequence of task execution is determined by the use of `@start()` and `@listen()` decorators.

By structuring your Flow with these decorators and understanding the execution sequence, you can effectively manage and retrieve the final output of your workflows in CrewAI.

For more detailed information, refer to the [CrewAI Flows output documentation](https://docs.crewai.com/concepts/flows#flow-output). 