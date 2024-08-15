# Video-04: Custom GPT with Retrieval-Augmented Generation (RAG)

## Overview

This video demonstrates how to create a custom GPT using Retrieval-Augmented Generation (RAG), allowing the model to respond to new information without the need for retraining. RAG dynamically fetches and integrates relevant data into the prompt, enabling the model to generate accurate, up-to-date answers.

### Key Concepts Covered:
- **Retrieval-Augmented Generation (RAG)**: A technique where the model retrieves relevant external data (documents, web pages, databases) and integrates it into the prompt to generate more accurate responses.
- **Custom GPT Creation**: The video shows how to augment a GPT model with external data sources and customize its responses to specific domains without retraining.

## System-Level Prompts

System-level prompts control how the model handles the retrieved information and prioritize it over previously known information.

```yaml
# Example of a system-level instruction in a RAG-based custom GPT:
{
  "instruction": "Retrieve the latest information from the external data source and use only that information to answer the user's question. Ignore older information that conflicts with the new data."
}
```

System-level prompts help guide the model to:
1. **Prefer new data**: Ensure the GPT responds with retrieved up-to-date data.
2. **Handle conflicting information**: Instruct GPT on how to prioritize new vs. old data.
3. **Search and retrieval**: Direct GPT to retrieve data from relevant sources.

## User-Level Prompts

User-level prompts specify what the user wants to ask, with GPT pulling relevant information via RAG to respond. This prompt is issued by the user to interact with the GPT system.

```yaml
# Example of a user-level prompt to a custom GPT augmented with external data:
{
  "query": "Tell me about the new Generative AI innovation program that Jules White's team is running at Vanderbilt."
}
```

The user-level prompt simply asks for information, and the model:
1. **Retrieves** relevant data from the external source (such as web pages, documents, etc.).
2. **Augments** the prompt with this retrieved information.
3. **Generates** the final response using the up-to-date data.

## Steps to Create Custom GPT using RAG

1. **Identify External Data Sources**: Determine which data sources you want to use for your custom GPT (e.g., web pages, internal documents, etc.).
   
2. **Set up Retrieval Mechanism**: Implement a retrieval system to fetch relevant information when a prompt is issued (could involve APIs, databases, or a web search mechanism).
   
3. **Augment Prompts with Retrieved Data**: Design the system to automatically insert relevant information retrieved from the external sources into the prompt for generating responses.

4. **Provide Instructions to GPT**: Include system-level instructions on how to prioritize and use the retrieved information in responses.

5. **Test and Iterate**: Test your custom GPT by issuing different prompts and checking its ability to respond using the latest data.

## Example Scenario

In this video, the custom GPT is expected to answer queries about new developments at Vanderbilt, including its new AI program, even though the model was not initially trained on this specific information. Using RAG, the system retrieves data from external sources and augments it into the prompt to generate a current and accurate response.
