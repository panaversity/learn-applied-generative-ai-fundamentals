# LangChain Academy 

## Introduction

Welcome to LangChain Academy! This is a growing set of modules focused on foundational concepts within the LangChain ecosystem. Module 0 is basic setup and Modules 1 - 4 focus on LangGraph, progressively adding more advanced themes. In each module folder, you'll see a set of notebooks. A video accompanies each notebook to guide you through the topic. Each module also has a `studio` subdirectory, with a set of relevant graphs that we will explore using the LangGraph API and Studio.

## Setup

### Clone repo
```
git clone https://github.com/langchain-ai/langchain-academy.git
$ cd langchain-academy
```

### Create an environment and install dependencies  
```
$ python3 -m venv lc-academy-env
$ source lc-academy-env/bin/activate
$ pip install -r requirements.txt
```

### Running notebooks
Notebooks for each module are in the `module-` folders.
```
$ jupyter notebook
```

### Set OpenAI API key
* If you don't have an OpenAI API key, you can sign up [here](https://openai.com/index/openai-api/).
*  Set `OPENAI_API_KEY` in your environment 

### Sign up for LangSmith

* Sign up [here](https://docs.smith.langchain.com/) 
*  Set `LANGCHAIN_API_KEY`, `LANGCHAIN_TRACING_V2=true` in your environment 

### Tavily for web search

Tavily Search API is a search engine optimized for LLMs and RAG, aimed at efficient, quick, and persistent search results. You can sign up for an API key [here](https://tavily.com/). It's easy to sign up and offers a generous free tier. Some lessons (in Module 4) will use Tavily. Set `TAVILY_API_KEY` in your environment.

### Set up LangGraph Studio

* Currently Studio only has macOS support
* Download the latest `.dmg` file [here](https://github.com/langchain-ai/langgraph-studio?tab=readme-ov-file#download)
* Install Docker desktop for Mac [here](https://docs.docker.com/engine/install/)

### Running Studio
Graphs for studio are in the `module-x/studio/` folders.

* To use Studio, you will need to create a .env file with the relevant API keys
* Run this from the command line to create these files for module 1 to 4, as an example:
```
$ for i in {1..4}; do
  cp module-$i/studio/.env.example module-$i/studio/.env
  echo "OPENAI_API_KEY=\"$OPENAI_API_KEY\"" > module-$i/studio/.env
done
echo "TAVILY_API_KEY=\"$TAVILY_API_KEY\"" >> module-4/studio/.env

```