# LangChain for LLM Application Development - DeepLearningAI

## Overview
Crash course on LangChain for LLM Application Developement by [DeepLearning.AI](https://learn.deeplearning.ai/langchain/lesson/1/introduction) and lectured by `Andrew Ng` and `Harrison Chase` [LangChain](https://python.langchain.com/docs/tutorials/) Founder. Note: This repository uses Google's Gemini-1.5-Flash model instead of OpenAI model.

## Course Plan
- [Lesson0: Introduction](#)
- [Lesson1: Models, Prompts and Parsers](#)
- [Lesson2: Memory](#)
- [Lesson3: Chains](#)
- [Lesson4: Question & Answer](#)
- [Lesson5: Evaluation](#)
- [Lesson6: Agents](#)
- [Conclusion](#)

### Setup & Dependencies
Setup & import your Google Cloud API key:

```python
import os

# Load API key from environment variable
api_key = os.environ['GOOGLE_API_KEY']
```

### Gemini-1.5-Flash API call

```python
import google.generativeai as genai

llm_model = genai.GenerativeModel("gemini-1.5-flash")


def get_completion(prompt: str, model= llm_model) -> str:
    """
    Generate a completion for the given prompt using the specified language model.

    Args:
    prompt (str): The input prompt to complete.
    model (ll_model): The language model to use.

    Returns:
    str: The completed text.
    """

    response = model.generate_content(prompt)
    return response.text
```

## Changes from Original Code:
- Replaced OpenAI API with Google's Gemini-1.5-Flash model.
- Updated LangChain version from 0.1 to 0.3.1.
- Made minimal adjustments to the original code to ensure compatibility, without deviating significantly from the video lessons.

## Lab - Notebooks *(Refactored Code)*

|Chapter|Exercises|
|--|--|
|[Lesson 1: Models, Prompts and Parsers](./01_models-prompts-and-parsers.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/01_models-prompts-and-parsers.ipynb)|
|[Lesson 2: Memory](./02_Memory.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/02_Memory.ipynb)|
|[Lesson 3: Chains](./03_Chains.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/03_Chains.ipynb)|
|[Lesson 4: Question & Answer](./04_Question_and_Answer.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/04_Question_and_Answer.ipynb)|
|[Lesson 5: Evaluation](./05_Evaluation.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/05_Evaluation.ipynb)|
|[Lesson 6: Agents](./06_Agents.ipynb)|[![Open notebook in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/panaversity/learn-applied-generative-ai-fundamentals/blob/main/21_langchain_ecosystem/langchain/langChain_for_llm_application_development_deepLearningAI/06_Agents.ipynb)|

## References
Main Course : 
- https://learn.deeplearning.ai/langchain/lesson/1/introduction

LangChain resources : 
- https://learn.deeplearning.ai/langchain/lesson/1/introduction

Others short Free Courses available on DeepLearning.AI : 
- https://deeplearning.ai/