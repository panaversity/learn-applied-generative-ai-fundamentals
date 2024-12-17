# Tool Calling (Compositional Function Calling)

Compositional function calling refers to the ability to combine user defined functions with the `code_execution` tool. The model will write them into larger blocks of code, and then pause execution while it waits for you to send back responses for each call.

[Function Calling](https://googleapis.github.io/python-genai/#function-calling)

[Gemini 2.0 - Multimodal live API: Tool use](https://github.com/google-gemini/cookbook/blob/main/gemini-2/live_api_tool_use.ipynb)

[Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)

Compositional function calling is a feature of Google's Gemini API that enables the model to recommend multiple API function calls based on a single user request. This capability allows developers to define custom functions that the model can suggest, facilitating complex interactions with external systems. 

In the Gemini API, developers can define function declarations within a `tools` object. Each function declaration includes a name, description, and parameters, which help the model understand the function's purpose and how to use it. When a user makes a request, the model analyzes these declarations and the query to determine which functions to suggest, returning a structured output specifying the function names and suggested arguments. Developers can then use this information to call external APIs and incorporate the results into further interactions with the model. 

The Gemini API supports different modes for function calling:

- **AUTO**: The model decides whether to predict a function call or provide a natural language response.

- **ANY**: The model is constrained to always predict a function call. If `allowed_function_names` is provided, the model picks from the set of allowed functions; otherwise, it picks from all available functions.

- **NONE**: The model won't predict a function call, behaving as if no function declarations were provided.

These modes allow developers to control the model's behavior in different scenarios. 

Compositional function calling enhances the model's ability to interact with real-time information and services, such as databases, customer relationship management systems, and document repositories. This feature improves the relevance and contextual accuracy of the model's responses, making it a powerful tool for developers building AI-driven applications. 

 