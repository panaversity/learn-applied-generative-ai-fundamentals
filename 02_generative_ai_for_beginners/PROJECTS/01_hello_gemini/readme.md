# Project 1: LangChain Hello World Project 

In this Project, we will create a simple LangChain Colab Notebook that uses the **[Google Gemini Flash 2.0 model](https://ai.google.dev/gemini-api/docs/models/gemini-v2)** to answer user questions. This example below is provided to help you get started assumes you have access to the Gemini API and a basic Python environment. However, you are required to develop and submit your project using Google Colab.

Project Submission Form:

https://forms.gle/b5Npy6eg4wKWro6m6

Due Date: December 30, 2024

Checking: Your Instructors will check your project in the 
first class after December 30, 2024. You will be removed from
the class until you successfully complete your project. 

Learning Material:

[Google intros Gemini 2.0 with a focus on AI agents](https://readwrite.com/google-intros-gemini-2-0-with-a-focus-on-ai-agents/)

[LangChain Tutorials](https://python.langchain.com/docs/tutorials/)

[LangChain Google Documentation](https://python.langchain.com/docs/integrations/providers/google/)

[ChatGoogleGenerativeAI](https://python.langchain.com/docs/integrations/chat/google_generative_ai/)

---

### Prerequisites

1. **Colab Signup**: Ensure Python 3.9+ is installed.
2. **LangChain Installed**: Install LangChain via pip:
   ```bash
   pip install langchain
   ```
3. **Gemini Flash API Key**: Obtain an API key for the Google Gemini Flash model.
4. **OpenAI Client for Gemini Flash**: Install the Gemini Flash client or SDK:
   ```bash
   pip install google-generativeai
   ```

---

### Step 1: Set Up Your Environment

Create a Python script or Jupyter notebook for your application.

Import the required libraries:

```python
from langchain.llms import GoogleGeminiFlash
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
```

---

### Step 2: Configure the Gemini Flash Model

Use the `GoogleGeminiFlash` class to interface with the Gemini Flash API. You’ll need to pass your API key.

```python
# Configure the Gemini Flash model
llm = GoogleGeminiFlash(
    api_key="your_gemini_api_key_here",
    model="gemini-flash",
    temperature=0.7  # Adjust for creativity
)
```

---

### Step 3: Create a Prompt Template

Define a simple template for the LLM to follow. This allows you to structure the interaction.

```python
# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question:\n\n{question}"
)
```

---

### Step 4: Build the LangChain Pipeline

Combine the LLM and the prompt template into a chain.

```python
# Create the LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)
```

---

### Step 5: Run the Hello World Example

Pass a sample question to the chain and print the response.

```python
# Run the chain with a sample question
question = "What is LangChain?"
response = chain.run({"question": question})

print("Answer:", response)
```

---

### Complete Script

Here’s the complete code:

```python
from langchain.llms import GoogleGeminiFlash
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Configure the Gemini Flash model
llm = GoogleGeminiFlash(
    api_key="your_gemini_api_key_here",
    model="gemini-flash",
    temperature=0.7  # Adjust for creativity
)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["question"],
    template="You are a helpful assistant. Answer the following question:\n\n{question}"
)

# Create the LLM chain
chain = LLMChain(llm=llm, prompt=prompt_template)

# Run the chain with a sample question
question = "What is LangChain?"
response = chain.run({"question": question})

print("Answer:", response)
```

---

### Output

When you run the script, the output will look something like this:

```plaintext
Answer: LangChain is an open-source framework for building applications powered by large language models. It simplifies workflows, integrates tools, and supports multi-step chains and agents.
```

---


---

### Next Steps in Colab Project

- **Experiment with Prompts**: Add more prompt templates to see how the model responds.
- **Add Memory**: Use LangChain’s memory feature to make the interaction multi-turn.
- **Integrate Tools**: Extend the chain to include tools like database queries or APIs.
- **Explore Gemini Features**: Adjust temperature, max tokens, and other parameters to optimize responses.

Enjoy building your LangChain-powered AI Colab Notebook Project with Gemini Flash!