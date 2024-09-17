# LangGraph

## The LangChain Academy Course to Learn from

https://academy.langchain.com/courses/intro-to-langgraph

The LangGraph learning notebooks are in course-notebooks directory

## Other Courses and Resources

## Deep Learning Course

[AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)

## References:

[LangGraph 101: it's better than LangChain](https://www.youtube.com/watch?v=qaWOwbFw3cs)

[Introduction to LangGraph](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-1-build-a-basic-chatbot)

[Deep Dive into LangGraph: Building Stateful and Multi-Agent Language Models](https://blog.gopenai.com/deep-dive-into-langgraph-building-stateful-and-multi-agent-language-models-b92d75ebe6ba)

[Conceptual Guides](https://langchain-ai.github.io/langgraph/concepts/)

[How-To Guides](https://langchain-ai.github.io/langgraph/how-tos/)

[Build an AI Coding Agent with LangGraph by LangChain](https://www.analyticsvidhya.com/blog/2024/03/build-an-ai-coding-agent-with-langgraph-by-langchain/)

## LangGraph Framework

LangGraph is a framework designed for building stateful, multi-actor applications using large language models (LLMs). It is part of the LangChain ecosystem and offers several unique features that make it stand out from other agentic frameworks.

### Key Features of LangGraph

1. **State Management**: LangGraph excels in automatic state management, which allows it to track and persist information across multiple interactions. This ensures that the system maintains context and responds appropriately to new inputs⁶.

2. **Graph Structure**: LangGraph uses a directed graph structure where each node represents an LLM agent, and the edges are the communication channels between these agents. This structure allows for clear and manageable workflows⁶.

3. **Coordination**: LangGraph ensures that agents execute in the correct order and that necessary information is exchanged seamlessly. This is crucial for complex applications where multiple agents need to work together to achieve a common goal⁶.

4. **Cycles and Controllability**: LangGraph supports cyclical graphs, which are essential for developing sophisticated agent runtimes. It also offers granular control over the agent's thought process, enabling developers to make data-driven decisions⁷.

5. **Human-Agent Collaboration**: LangGraph is designed for seamless collaboration between agents and humans. It allows agents to write drafts for review and await approval before acting, making it easier to inspect and modify the agent’s actions³.

6. **Scalability**: With LangGraph Cloud, you can quickly deploy and scale your applications. It includes infrastructure for prototyping, debugging, and sharing LangGraph applications³.

### How LangGraph is Superior to Other Agentic Frameworks

1. **Expressiveness**: LangGraph provides a more expressive framework to handle unique tasks without restricting users to a single black-box cognitive architecture. This makes it suitable for complex, bespoke tasks³.

2. **Reliability**: LangGraph includes easy-to-add moderation and quality loops that prevent agents from veering off course. This ensures that the agents are reliable and perform tasks accurately³.

3. **Ease of Use**: LangGraph abstracts away the complexities associated with state management and agent coordination, simplifying the development process. This allows developers to focus on the high-level logic of their applications⁶.

4. **Advanced Control**: LangGraph offers advanced control features like "time-travel," which allows developers to take different actions at specific times. This level of control is not commonly found in other frameworks³.

5. **Iterative Development**: LangGraph supports iterative, decision-based flows, which are often required for advanced AI agentic frameworks. This makes it easier to build and improve complex applications over time⁵.

LangGraph's combination of state management, coordination, and advanced control features makes it a powerful tool for developing sophisticated, reliable, and scalable AI applications.

If you have any specific questions or need further details, feel free to ask!

Source: Conversation with Copilot, 9/17/2024
(1) LangGraph Tutorial: What Is LangGraph and How to Use It?. https://www.datacamp.com/tutorial/langgraph-tutorial.
(2) langgraph · PyPI. https://pypi.org/project/langgraph/.
(3) LangGraph - LangChain. https://www.langchain.com/langgraph.
(4) Decode How to Build Agentic AI Applications using LangGraph. https://datasciencedojo.com/newsletter/agentic_ai_langgraph/.
(5) Mastering Agents: LangGraph Vs Autogen Vs Crew AI - Galileo. https://www.rungalileo.io/blog/mastering-agents-langgraph-vs-autogen-vs-crew.
(6) An Overview of Multi Agent Frameworks: Autogen, CrewAI and LangGraph. https://sajalsharma.com/posts/overview-multi-agent-fameworks/.
(7) langchain-ai/langgraph: Build resilient language agents as graphs. - GitHub. https://github.com/langchain-ai/langgraph.