# Router Decorator

In CrewAI Flows, the `@router()` decorator enables dynamic routing within your workflow based on the output of preceding tasks. This functionality allows you to direct the flow of execution to different methods or tasks, facilitating complex decision-making processes.

**Implementing the `@router()` [Decorator](https://docs.crewai.com/concepts/flows#router)**

To utilize the `@router()` decorator, follow these steps:

1. **Define the Flow Class**: Create a class that inherits from `Flow`.

2. **Implement Methods with Decorators**:
   - Use the `@start()` decorator to mark the initial method(s) that initiate the workflow.
   - Apply the `@router()` decorator to a method that will determine the next step based on the output of a preceding task.
   - Use the `@listen()` decorator to define methods that will execute based on the routing decisions.

3. **Execute the Flow**: Instantiate the Flow class and invoke the `kickoff()` method to start the workflow.

**Example:**

```python
from crewai.flow.flow import Flow, listen, router, start

class ContentModerationFlow(Flow):
    @start()
    def analyze_content(self):
        # Analyze the content and return a category
        content = "Sample content to analyze"
        # Placeholder for content analysis logic
        category = "safe"  # This could be 'safe', 'sensitive', or 'unsafe'
        return category

    @router(analyze_content)
    def route_based_on_category(self, category):
        if category == "safe":
            return "process_safe_content"
        elif category == "sensitive":
            return "process_sensitive_content"
        elif category == "unsafe":
            return "process_unsafe_content"

    @listen("process_safe_content")
    def handle_safe_content(self):
        # Handle safe content
        print("Handling safe content")

    @listen("process_sensitive_content")
    def handle_sensitive_content(self):
        # Handle sensitive content
        print("Handling sensitive content")

    @listen("process_unsafe_content")
    def handle_unsafe_content(self):
        # Handle unsafe content
        print("Handling unsafe content")

# Instantiate and execute the flow
flow = ContentModerationFlow()
flow.kickoff()
```

**Explanation:**

- `analyze_content`: This method analyzes the content and returns a category (e.g., 'safe', 'sensitive', or 'unsafe').

- `route_based_on_category`: Decorated with `@router(analyze_content)`, this method receives the category from `analyze_content` and returns the name of the method to execute next based on the category.

- `handle_safe_content`, `handle_sensitive_content`, `handle_unsafe_content`: These methods are decorated with `@listen()` and correspond to the possible routes determined by `route_based_on_category`. Each method handles a specific category of content.

**Key Points:**

- The `@router()` decorator facilitates dynamic decision-making within the workflow by directing the flow based on the output of a preceding task.

- The method decorated with `@router()` should return the name of the next method to execute, allowing for flexible and dynamic routing.

By incorporating the `@router()` decorator, you can implement complex, conditional workflows in CrewAI, enabling your application to respond dynamically to varying inputs and conditions.

For more detailed information, refer to the [CrewAI Flows documentation](https://docs.crewai.com/concepts/flows). 