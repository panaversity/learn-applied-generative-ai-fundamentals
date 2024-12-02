# Chatbot using Flows

Building a chatbot with CrewAI Flows enables the creation of structured, event-driven workflows that manage state and control execution flow effectively. This tutorial guides you through the process of developing a conversational chatbot using CrewAI Flows, integrating memory for context retention, and utilizing external tools for enhanced functionality.

**Prerequisites:**

- Basic knowledge of Python programming.
- Python 3.12 or later installed on your system.
- Familiarity with virtual environments (e.g., `venv` or `conda`).

**Step 1: Set Up the Development Environment**

1. **Create a Virtual Environment:**

   ```bash
   python -m venv crewai_chatbot_env
   ```

2. **Activate the Virtual Environment:**

   - On Windows:
     ```bash
     crewai_chatbot_env\Scripts\activate
     ```
   - On Unix or MacOS:
     ```bash
     source crewai_chatbot_env/bin/activate
     ```

3. **Install CrewAI:**

   ```bash
   pip install crewai
   ```

**Step 2: Define the Chatbot Agent**

Create a Python script (e.g., `chatbot.py`) and define the chatbot agent using CrewAI's `Agent` class:

```python
from crewai import Agent

# Define the chatbot agent
chatbot_agent = Agent(
    role="Conversational Assistant",
    goal="Engage in meaningful conversations with users, providing helpful and accurate information.",
    backstory="You are an AI-powered assistant designed to assist users with a variety of tasks and answer their questions.",
    verbose=True
)
```

**Step 3: Implement the Chatbot Task**

Define the task that the chatbot agent will perform:

```python
from crewai import Task

# Define the chatbot task
chatbot_task = Task(
    description="Respond to user inquiries based on the provided message: {user_message}",
    expected_output="A relevant and informative response to the user's message.",
    agent=chatbot_agent,
)
```

**Step 4: Configure the Flow**

Set up a flow to manage the conversation:

```python
from crewai.flow.flow import Flow, start

class ChatbotFlow(Flow):
    @start()
    def handle_message(self, user_message):
        # Process the user message
        response = chatbot_task.run(user_message=user_message)
        return response
```

**Step 5: Integrate Memory for Context Retention**

To enable the chatbot to remember previous interactions, integrate a memory system:

```python
from mem0 import Memory

# Configure memory
memory_config = {
    "provider": "mem0",
    "config": {"user_id": "unique_user_id"},
}
memory = Memory.from_config(memory_config)
```

Incorporate the memory into the flow:

```python
class ChatbotFlow(Flow):
    def __init__(self):
        super().__init__()
        self.memory = memory

    @start()
    def handle_message(self, user_message):
        # Retrieve conversation history
        history = self.memory.retrieve()
        # Process the user message with context
        response = chatbot_task.run(user_message=user_message, context=history)
        # Store the interaction
        self.memory.store(user_message, response)
        return response
```

**Step 6: Run the Chatbot**

Create a script to run the chatbot:

```python
if __name__ == "__main__":
    flow = ChatbotFlow()
    while True:
        user_message = input("You: ")
        response = flow.handle_message(user_message)
        print(f"Chatbot: {response}")
```

**Additional Resources:**

- For a comprehensive guide on CrewAI Flows, refer to the [CrewAI Flows Documentation](https://docs.crewai.com/concepts/flows).
- Explore practical examples in the [CrewAI Examples Repository](https://github.com/crewAIInc/crewAI-examples).
- Watch the [CrewAI Flows Crash Course](https://www.youtube.com/watch?v=8PtGcNE01yo) for a step-by-step video tutorial.

By following this tutorial, you've built a conversational chatbot using CrewAI Flows, capable of engaging in meaningful dialogues and retaining context through integrated memory. This foundation allows for further enhancements, such as integrating additional tools and expanding the chatbot's capabilities. 