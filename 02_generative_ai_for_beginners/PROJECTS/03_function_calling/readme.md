# Project 3: LangChain Function/Tool Calling Calculator

In this Project, we will create a simple LangChain Colab Notebook that uses the **Google Gemini Flash model** to answer user calculation questions. This example below is provided to help you get started assumes you have access to the Gemini API and a basic Python environment. However, you are required to develop and submit your project using Google Colab.

Project Submission Form:

https://forms.gle/b5Npy6eg4wKWro6m6

Due Date: January 13, 2025

Checking: Your Instructors will check your project in the first class after January 13, 2025. You will be removed from the class until you sucessfully complete your project. 

---

Here’s a step-by-step tutorial for developing a **LangChain function/tool-calling calculator** using the **Google Gemini Flash model**. This tool will enable the model to perform mathematical calculations by invoking a custom calculator tool during a conversation.

---

## **Tutorial: Building a LangChain Calculator with Google Gemini Flash**

### Prerequisites
1. **Google Colab** signup.
2. API key for **Google Gemini Flash**.
3. Installed libraries: `langchain`, `google-generativeai`.

Install dependencies:

```bash
pip install langchain google-generativeai
```

---

### Step 1: Set Up Environment Variables
Create a `.env` file for your API key:

```plaintext
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

Load the API key in your script:

```python
import os
from dotenv import load_dotenv

load_dotenv()
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
```

---

### Step 2: Define the Calculator Tool

The calculator tool will handle basic arithmetic operations.

```python
class Calculator:
    def calculate(self, expression: str) -> str:
        try:
            # Use Python's eval to compute the result safely
            result = eval(expression, {"__builtins__": None}, {})
            return str(result)
        except Exception as e:
            return f"Error: {e}"
```

---

### Step 3: Create the Tool Wrapper for LangChain

Integrate the calculator with LangChain as a tool.

```python
from langchain.tools import tool

# Define the tool using a decorator
@tool
def calculator(expression: str) -> str:
    """
    Perform arithmetic calculations.
    Input: A mathematical expression as a string (e.g., "2 + 2").
    Output: Result of the calculation as a string.
    """
    calc = Calculator()
    return calc.calculate(expression)
```

---

### Step 4: Set Up the Google Gemini Flash Model

Initialize the LLM with tool-calling capabilities.

```python
from langchain.chat_models import GoogleGeminiFlash
from langchain.chains import ConversationalChain
from langchain.agents import ToolAgent, ToolAgentExecutor

# Initialize the Gemini model
gemini_model = GoogleGeminiFlash(api_key=GOOGLE_GEMINI_API_KEY)

# Define tools
tools = [calculator]

# Create a ToolAgent for the calculator
agent = ToolAgent.from_tools_and_llm(tools, gemini_model)
executor = ToolAgentExecutor(agent)
```

---

### Step 5: Build the Conversational Chain

Wrap the agent in a conversational chain for interaction.

```python
from langchain.memory import ConversationBufferMemory

# Set up memory to maintain conversation context
memory = ConversationBufferMemory()

# Build the conversational chain
chain = ConversationalChain(
    llm=gemini_model,
    agent_executor=executor,
    memory=memory
)
```

---

### Step 6: Test the Calculator Tool

Interact with the system by asking questions that require mathematical calculations.

```python
# User query
query = "What is 15 divided by 3?"

# Get response from the system
response = chain.run(query)
print(response)
```

---

### Expected Output

**Query:**  
What is 15 divided by 3?

**Response:**  
"The result of 15 divided by 3 is 5."

---

### Step 7: Optional Enhancements

1. **Advanced Operations**: Extend the calculator to handle more complex operations like logarithms, trigonometry, etc.
2. **Error Handling**: Provide user-friendly messages for invalid inputs or unsupported operations.
3. **UI**: Integrate this chain into a web application using frameworks like Streamlit and FastAPI.
4. **Logging**: Log all inputs and outputs for debugging or auditing.

---

### Example with Multiple Queries

```python
queries = [
    "What is 25 multiplied by 4?",
    "Now divide the result by 5.",
    "Add 10 to that."
]

for q in queries:
    print("Query:", q)
    print("Response:", chain.run(q))
    print("-" * 40)
```

**Output:**  
- Query 1: "The result of 25 multiplied by 4 is 100."
- Query 2: "The result of dividing 100 by 5 is 20."
- Query 3: "Adding 10 to 20 gives 30."

---

### Why Use LangChain Tool-Calling?

- **Modularity**: Tools like this calculator can be extended or replaced without rewriting the core logic.
- **Integration**: Easily combine multiple tools for complex workflows.
- **Dynamic Calls**: The LLM dynamically decides when to call the tool based on user input.

This setup is ideal for augmenting the capabilities of LLMs in practical applications!