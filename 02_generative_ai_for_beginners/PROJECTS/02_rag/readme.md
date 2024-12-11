# Project 2: LangChain RAG Project

In this Project, we will create a simple LangChain RAG Colab Notebook that uses the **Google Gemini Flash model** to answer user questions from the document provided. This example below is provided to help you get started assumes you have access to the Gemini API, Pinecone and a basic Python environment. However, you are required to develop and submit your project using Google Colab.

Project Submission Form:

https://forms.gle/b5Npy6eg4wKWro6m6

Due Date: Jan 6, 2025

Checking: Your Instructors will check your project in the first class after Jan 6, 2025. You will be removed from the class until you sucessfully complete your project. 

---

Here’s a detailed project for creating a **Retrieval-Augmented Generation (RAG)** system using LangChain with Google Gemini Flash and Pinecone. This system will retrieve relevant context from a vector database and use that context to generate a more accurate and informed response from the Gemini model.

---

## **Project: LangChain RAG with Google Gemini Flash and Pinecone**

### Prerequisites
1. **Python 3.8+** installed.
2. API keys for:
   - Google Gemini Flash.
   - Pinecone.
3. Installed Python libraries: `langchain`, `pinecone-client`, `google-generativeai`, `openai`, and `tqdm`.

Install dependencies with:

```bash
pip install langchain pinecone-client google-generativeai openai tqdm
```

---

### Step 1: Set Up Environment Variables
Create a `.env` file in your project directory to store API keys securely:

```plaintext
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_ENVIRONMENT=your_pinecone_environment
GOOGLE_GEMINI_API_KEY=your_google_gemini_api_key
```

Load these variables into your script using the `dotenv` package:

```bash
pip install python-dotenv
```

Add this to your script:

```python
import os
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
```

---

### Step 2: Initialize Pinecone
Pinecone is used to store and retrieve vectorized documents.

```python
import pinecone

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)

# Create a new index or connect to an existing one
index_name = "gemini-rag-index"
if index_name not in pinecone.list_indexes():
    pinecone.create_index(index_name, dimension=768)

# Connect to the index
index = pinecone.Index(index_name)
```

---

### Step 3: Use LangChain for RAG Workflow

#### 1. **Set Up Embedding Model**
Use Google Gemini embeddings to vectorize documents.

```python
from langchain.embeddings import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(api_key=GOOGLE_GEMINI_API_KEY)
```

#### 2. **Set Up Document Loader**
Load and preprocess your documents.

```python
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load documents
loader = TextLoader("documents.txt")  # Replace with your file
documents = loader.load()

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)
```

#### 3. **Embed and Store Documents in Pinecone**
Store the vectorized document chunks in Pinecone.

```python
from tqdm import tqdm

# Create embeddings and upload to Pinecone
for doc in tqdm(docs):
    vector = embeddings.embed_query(doc.page_content)
    index.upsert([(doc.metadata["source"], vector, doc.page_content)])
```

#### 4. **Set Up Retriever**
Use LangChain’s Pinecone integration to retrieve relevant documents.

```python
from langchain.vectorstores import Pinecone

retriever = Pinecone(pinecone_index=index, embedding_function=embeddings.embed_query, text_key="text")
```

---

### Step 4: Set Up Google Gemini Flash Model

Initialize the model for RAG generation.

```python
from langchain.chat_models import GoogleGeminiFlash

gemini_model = GoogleGeminiFlash(api_key=GOOGLE_GEMINI_API_KEY, temperature=0.7)
```

---

### Step 5: Combine Retriever and LLM

Use LangChain’s `RetrievalQA` chain to integrate the retriever and the LLM.

```python
from langchain.chains import RetrievalQA

qa_chain = RetrievalQA.from_chain_type(
    llm=gemini_model,
    chain_type="stuff",  # Other options: "map_reduce", "refine"
    retriever=retriever
)
```

---

### Step 6: Query the RAG System

Test the system by asking a question.

```python
query = "What is the history of artificial intelligence?"
response = qa_chain.run(query)
print(response)
```

---

### Step 7: Deploy and Iterate

1. **Deploy the RAG system** as an API using FastAPI or Flask.
2. **Monitor performance** and fine-tune:
   - Add more documents to the Pinecone index.
   - Adjust `chunk_size` and `chunk_overlap` for better retrieval results.
   - Experiment with `temperature` and other model parameters for creativity or accuracy.

---

### Optional Enhancements
- **Streamlined Search**: Use Pinecone’s hybrid search (text + vector search).
- **Custom Retrieval Logic**: Fine-tune how documents are retrieved or preprocessed.
- **UI/UX**: Build a web-based interface for querying your RAG system.

---

### Example Output

**Question:**  
*What were the major milestones in AI development during the 20th century?*

**Response (Generated by Gemini):**  
"The history of AI in the 20th century includes milestones such as the founding of the field in 1956, the development of expert systems in the 1970s, and the rise of machine learning in the 1980s. Key contributors include pioneers like Alan Turing, John McCarthy, and Marvin Minsky."

---

This project provides the foundation for building a RAG system using LangChain, Google Gemini Flash, and Pinecone. With these tools, you can create robust, context-aware AI applications tailored to specific use cases!