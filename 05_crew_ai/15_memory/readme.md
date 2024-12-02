# Memory

[Memory Docs](https://docs.crewai.com/concepts/memory)

CrewAI's memory system enhances AI agents' capabilities by enabling them to retain and utilize information from past interactions, leading to more coherent and contextually relevant responses. This system comprises several components, each serving a distinct purpose:

**1. Short-Term Memory:**
- **Function:** Temporarily stores recent interactions and outcomes, allowing agents to recall information pertinent to the current context during execution.
- **Implementation:** Utilizes Retrieval-Augmented Generation (RAG) techniques to manage and retrieve this information.

**2. Long-Term Memory:**
- **Function:** Preserves valuable insights and learnings from past executions, enabling agents to build and refine their knowledge over time.
- **Implementation:** Stores task results in a SQLite3 database, facilitating persistent knowledge retention.

**3. Entity Memory:**
- **Function:** Captures and organizes information about entities (such as people, places, and concepts) encountered during tasks, aiding in understanding and relationship mapping.
- **Implementation:** Employs RAG for storing and retrieving entity-related information.

**4. Contextual Memory:**
- **Function:** Maintains the context of interactions by integrating short-term, long-term, and entity memory, ensuring coherence and relevance in agent responses throughout a sequence of tasks or conversations.

**5. User Memory:**
- **Function:** Stores user-specific information and preferences, enhancing personalization and user experience.
- **Implementation:** Can be integrated using external memory layers like Mem0 to manage user preferences effectively.

**Benefits of CrewAI's Memory System:**
- **Adaptive Learning:** Agents become more efficient over time, adapting to new information and refining their approach to tasks.
- **Enhanced Personalization:** Memory enables agents to remember user preferences and historical interactions, leading to personalized experiences.
- **Improved Problem Solving:** Access to a rich memory store aids agents in making more informed decisions, drawing on past learnings and contextual insights. 

**Implementing Memory in CrewAI:**
To enable the memory system in your CrewAI project, set the `memory` parameter to `True` when configuring your crew. By default, the system uses OpenAI embeddings, but you can customize the embedder to suit your needs.

**Example: Configuring Memory for a Crew**
```python
from crewai import Crew, Agent, Task, Process

# Assemble your crew with memory capabilities
my_crew = Crew(
    agents=[...],
    tasks=[...],
    process=Process.sequential,
    memory=True,
    verbose=True
)
```

In this example, setting `memory=True` activates the memory system, allowing agents to utilize short-term, long-term, and entity memory during task execution.

**Customizing Memory Components:**
You can customize each memory component to align with your project's objectives. For instance, integrating Mem0 for enhanced user memory involves setting environment variables and configuring the memory provider accordingly.

**Example: Integrating Mem0 for User Memory**
```python
import os
from crewai import Crew, Process
from mem0 import MemoryClient

# Set environment variables for Mem0
os.environ["MEM0_API_KEY"] = "m0-xx"

# Record user preferences
client = MemoryClient()
messages = [
    {"role": "user", "content": "Hi there! I'm planning a vacation and could use some advice."},
    {"role": "assistant", "content": "Hello! I'd be happy to help with your vacation planning. What kind of destination do you prefer?"},
    {"role": "user", "content": "I am more of a beach person than a mountain person."},
    {"role": "assistant", "content": "That's interesting. Do you like hotels or Airbnb?"},
    {"role": "user", "content": "I like Airbnb more."},
]
client.add(messages, user_id="john")

# Create a Crew with User Memory
crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=True,
    process=Process.sequential,
    memory=True,
    memory_config={
        "provider": "mem0",
        "config": {"user_id": "john"},
    },
)
```

This setup enables the agent to access and utilize user-specific information, enhancing the personalization of interactions.

By leveraging CrewAI's comprehensive memory system, you can develop AI agents capable of learning from past interactions, understanding complex contexts, and delivering personalized user experiences. 