# Microsoft Agentic AI

Magentic-One and AutoGen are both initiatives from Microsoft Research aimed at advancing multi-agent AI systems, but they serve distinct purposes within this domain.

AutoGen is an open-source programming framework designed to facilitate the development of AI agents and their collaboration to solve complex tasks. It provides a multi-agent conversation framework, allowing developers to build and orchestrate workflows involving multiple agents. AutoGen supports agents powered by large language models (LLMs), tools, human inputs, or combinations thereof, enabling flexible and customizable agent interactions. Its modular design simplifies the creation of diverse applications across various domains. ￼

Magentic-One, on the other hand, is a generalist multi-agent system built upon the AutoGen framework. It comprises a team of specialized agents, each with unique capabilities such as web browsing, file handling, and code execution. An Orchestrator agent oversees these specialized agents, planning and directing their actions to achieve high-level goals. Magentic-One’s modular architecture allows for the addition or removal of agents without the need for additional prompt tuning or training, enhancing its adaptability to various tasks. ￼

In summary, AutoGen serves as the foundational framework that provides the tools and infrastructure for building multi-agent systems, while Magentic-One is an implementation of such a system, leveraging AutoGen to coordinate specialized agents in solving complex, open-ended tasks.