# Decorators

CrewAI's introduction of Flows provides a structured, event-driven framework for building and managing AI workflows. Within this framework, decorators play a crucial role in defining the behavior and execution flow of tasks. The primary decorators used in CrewAI Flows are `@start()` and `@listen()`.

**1. [`@start()` Decorator](https://docs.crewai.com/concepts/flows#start)**

The `@start()` decorator designates a method as the entry point of a Flow. When a Flow is initiated, all methods marked with `@start()` are executed in parallel. This allows for multiple starting tasks within a single Flow.

*Example:*

```python
from crewai.flow.flow import Flow, start

class ExampleFlow(Flow):
    @start()
    def initial_task(self):
        # Implementation of the initial task
        pass
```

In this example, `initial_task` is marked as the starting point of the Flow. When the Flow is initiated, `initial_task` will execute.

**2. [`@listen()` Decorator](https://docs.crewai.com/concepts/flows#listen)**

The `@listen()` decorator specifies that a method should execute in response to the completion of another task within the Flow. It effectively sets up an event-driven relationship between tasks, where the decorated method listens for the output of a specified task and executes upon its completion.

*Usage:*

- **Listening to a Method by Name:** You can pass the name of the method you want to listen to as a string.

  ```python
  from crewai.flow.flow import Flow, listen, start

  class ExampleFlow(Flow):
      @start()
      def generate_data(self):
          # Implementation of data generation
          return data

      @listen("generate_data")
      def process_data(self, data):
          # Implementation of data processing
          pass
  ```

- **Listening to a Method Directly:** You can pass the method itself.

  ```python
  from crewai.flow.flow import Flow, listen, start

  class ExampleFlow(Flow):
      @start()
      def generate_data(self):
          # Implementation of data generation
          return data

      @listen(generate_data)
      def process_data(self, data):
          # Implementation of data processing
          pass
  ```

In both examples, `process_data` is set to execute after `generate_data` completes, receiving its output as an argument.

**Key Points:**

- The `@start()` decorator identifies methods that serve as entry points for the Flow.

- The `@listen()` decorator establishes dependencies between tasks, enabling event-driven execution based on the completion of specified methods.

By utilizing these decorators, developers can create complex, event-driven workflows in CrewAI, ensuring tasks are executed in a controlled and logical sequence.

For more detailed information, refer to the [CrewAI Flows documentation](https://docs.crewai.com/concepts/flows). 