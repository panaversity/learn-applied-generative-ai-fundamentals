# Conditional Logic

In CrewAI Flows, implementing conditional logic is facilitated through the or_ and and_ functions, which allow methods to respond to multiple events based on specified conditions.

Using the or_ Function

The or_ function enables a method to listen to multiple events and triggers the listener when any of the specified events occur.

Example:

from crewai.flow.flow import Flow, listen, or_, start

class OrExampleFlow(Flow):
    @start()
    def start_method(self):
        return "Output from start_method"

    @start()
    def another_method(self):
        return "Output from another_method"

    @listen(or_(start_method, another_method))
    def logger(self, result):
        print(f"Logger received: {result}")

In this example:
	•	start_method and another_method are both starting points of the Flow.
	•	The logger method listens to both methods using or_ and is triggered when either emits an output.

Using the and_ Function

The and_ function allows a method to listen to multiple events and triggers the listener only when all specified events have occurred.

Example:

from crewai.flow.flow import Flow, listen, and_, start

class AndExampleFlow(Flow):
    @start()
    def first_method(self):
        return "Output from first_method"

    @start()
    def second_method(self):
        return "Output from second_method"

    @listen(and_(first_method, second_method))
    def combined_logger(self, result):
        print(f"Combined Logger received: {result}")

In this example:
	•	first_method and second_method are both starting points of the Flow.
	•	The combined_logger method listens to both methods using and_ and is triggered only after both have emitted outputs.

Considerations
	•	Execution Timing: Ensure that the methods being listened to are executed in a manner that aligns with the intended conditional logic.
	•	State Management: Maintain a consistent state within the Flow to handle the outputs appropriately when using or_ and and_.

For more detailed information, refer to the official CrewAI documentation on Flows. ￼