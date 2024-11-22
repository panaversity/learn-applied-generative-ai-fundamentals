# Conditional Logic

In CrewAI Flows, implementing conditional logic is facilitated
through the `or_` and `and_` functions, which allow methods to 
respond to multiple events or combinations of events.

**[Using `or_` for Conditional Execution](https://docs.crewai.com/concepts/flows#conditional-logic-or)**

The `or_` function enables a method to execute when any one of the
specified events occurs. This is useful when you want a task to
proceed upon the completion of any among several preceding tasks.

*Example:*

```python
from crewai.flow.flow import Flow, listen, start, or_

class OrExampleFlow(Flow):
    @start()
    def task_a(self):
        return "Output from task A"

    @start()
    def task_b(self):
        return "Output from task B"

    @listen(or_(task_a, task_b))
    def task_c(self, result):
        print(f"Task C received: {result}")
        return "Output from task C"

flow = OrExampleFlow()
flow.kickoff()
```

In this example, `task_c` will execute when either `task_a` or 
`task_b` completes, receiving the result from whichever task
finishes first.

**[Using `and_` for Conditional Execution](https://docs.crewai.com/concepts/flows#conditional-logic-and)**

The `and_` function allows a method to execute only after 
all specified events have occurred. This is beneficial when a
task depends on the completion of multiple preceding tasks.

*Example:*

```python
from crewai.flow.flow import Flow, listen, start, and_

class AndExampleFlow(Flow):
    @start()
    def task_x(self):
        return "Output from task X"

    @start()
    def task_y(self):
        return "Output from task Y"

    @listen(and_(task_x, task_y))
    def task_z(self, results):
        result_x, result_y = results
        print(f"Task Z received: {result_x} and {result_y}")
        return "Output from task Z"

flow = AndExampleFlow()
flow.kickoff()
```

Here, `task_z` will execute only after both `task_x` and `task_y` 
have completed, receiving their results as a **tuple**.

**Important Considerations**

- **Execution Timing**: When using `or_`, the listening method executes upon the first completion among the specified tasks. With `and_`, the method waits until all specified tasks have completed.

- **Result Handling**: For `or_`, the result passed to the listening method corresponds to the task that completed first. For `and_`, the results are provided as a tuple, maintaining the order of the specified tasks.

- **Potential Issues**: Be aware of known issues with these functions. For instance, there have been reports of the `or_` function executing only once when listening to multiple methods . Similarly, issues with the `and_` function have been documented . It's advisable to consult the latest CrewAI documentation and community forums for updates and best practices.

By effectively utilizing `or_` and `and_`, you can implement 
complex conditional logic within your CrewAI Flows, allowing for
dynamic and responsive workflows. 