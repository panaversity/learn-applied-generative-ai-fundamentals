# State Managements in Flows

In CrewAI Flows, effective state management is crucial for building robust AI workflows. Flows support two primary approaches to state management: unstructured and structured. Both methods allow you to initialize or update the flow's state by passing inputs to the `kickoff` function.

**[Unstructured State Management](https://docs.crewai.com/concepts/flows#unstructured-state-management)**

In unstructured state management, the flow's state is a dictionary (`dict`) that can be dynamically updated. You can pass any dictionary to the `inputs` parameter of the `kickoff` function to initialize or update the state.

*Example:*

```python
from crewai.flow.flow import Flow, listen, start

class UnstructuredExampleFlow(Flow):
    @start()
    def first_method(self):
        self.state['message'] = "Hello from unstructured flow"
        self.state['counter'] = 0

    @listen(first_method)
    def second_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state['counter'] += 1
        self.state['message'] += " - updated again"
        print(f"State after third_method: {self.state}")

flow = UnstructuredExampleFlow()
flow.kickoff(inputs={'counter': 5, 'message': 'Initial message'})
```

In this example, the `kickoff` function initializes the state with `counter` set to 5 and `message` set to 'Initial message'. The methods then update these values as the flow progresses.

**[Structured State Management](https://docs.crewai.com/concepts/flows#structured-state-management)**

Structured state management utilizes predefined schemas to ensure consistency and type safety. By employing models such as Pydantic's `BaseModel`, you can define the exact structure of the state. Inputs passed to the `kickoff` function must adhere to this schema.

*Example:*

```python
from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""

class StructuredExampleFlow(Flow[ExampleState]):
    @start()
    def first_method(self):
        self.state.message = "Hello from structured flow"

    @listen(first_method)
    def second_method(self):
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        self.state.counter += 1
        self.state.message += " - updated again"
        print(f"State after third_method: {self.state}")

flow = StructuredExampleFlow()
flow.kickoff(inputs={'counter': 10, 'message': 'Starting message'})
```

Here, `ExampleState` defines the structure of the state with specific types for `counter` and `message`. The `kickoff` function initializes the state with `counter` set to 10 and `message` set to 'Starting message'. The methods then update these values as the flow progresses.

**Key Points:**

- **Unstructured State Management:** Offers flexibility by allowing dynamic addition of state attributes without predefined constraints.

- **Structured State Management:** Provides defined schemas, ensuring type safety and consistency, which is beneficial for complex workflows.

By effectively managing state within CrewAI Flows, you can create robust, maintainable, and efficient AI workflows tailored to your specific needs.

For more detailed information, refer to the [CrewAI Flows documentation](https://docs.crewai.com/concepts/flows). 

