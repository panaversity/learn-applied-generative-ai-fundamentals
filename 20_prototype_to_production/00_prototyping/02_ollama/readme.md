# [Ollama](https://ollama.com/)

Run Llama 3.1, Phi 3, Mistral, Gemma 2, and other models. Customize and create your own.

[Ollama on Google Colab: A Game-Changer!](https://www.youtube.com/watch?v=9sPKTNGaPf8)

### In-Depth Tutorial on Using Ollama in Google Colab

**Ollama** is a powerful tool that allows you to run and experiment with language models locally. It offers flexibility for running different models, including some that may not be available on cloud-based APIs. In this tutorial, we'll walk through how to set up and use Ollama within Google Colab, even though Ollama is typically designed for local environments. 

Given that Ollama typically runs as a Docker container or through a local setup, using it directly in Google Colab requires some creative workarounds. We will explore a few strategies to make the most out of Ollama's capabilities within Colab.

### Table of Contents
1. Introduction to Ollama
2. Setting Up Ollama
   - Running Ollama Locally
   - Using Ngrok to Expose Local Ollama Instance to Google Colab
3. Interacting with Ollama in Google Colab
   - Connecting Colab to Your Local Ollama Instance
   - Running API Calls from Colab
4. Advanced Usage
   - Customizing Ollama Models
   - Chaining API Calls for Complex Tasks
5. Conclusion

### 1. Introduction to Ollama

**Ollama** is a platform that enables you to run language models on your local machine. It is often used to run large language models (LLMs) for tasks like text generation, question answering, or code generation. Ollama typically uses Docker for deployment, which ensures consistency across different environments.

**Why use Ollama in Colab?**
- **Experimentation**: While Ollama is designed for local use, integrating it with Colab allows you to experiment with models remotely and share your work easily.
- **Flexibility**: By connecting Colab to a local instance of Ollama, you can leverage Colab's cloud environment to process and analyze results, even if the heavy computation is done locally.

### 2. Setting Up Ollama

#### Running Ollama Locally

Before using Ollama in Google Colab, you need to set it up on your local machine. Here's a brief overview of the steps to install and run Ollama locally:

1. **Install Docker**:
   - Ollama requires Docker to run its containers. Install Docker for your operating system by following the instructions [here](https://docs.docker.com/get-docker/).

2. **Download and Run Ollama**:
   - Once Docker is installed, you can pull the Ollama Docker image and run it.

   ```bash
   docker pull ollama/ollama:latest
   docker run -d -p 5000:5000 ollama/ollama
   ```

   - This command pulls the latest Ollama Docker image and runs it on port 5000.

#### Using Ngrok to Expose Local Ollama Instance to Google Colab

To interact with Ollama from Google Colab, you need to expose your local Ollama instance to the internet. Ngrok is a handy tool that creates secure tunnels to localhost, allowing you to access your local server from anywhere.

1. **Install Ngrok**:
   - Download and install Ngrok from [here](https://ngrok.com/download).

2. **Run Ngrok**:
   - Start Ngrok to tunnel your local Ollama instance.

   ```bash
   ngrok http 5000
   ```

   - This command will provide a public URL that forwards to your local Ollama instance on port 5000.

3. **Copy the Public URL**:
   - Ngrok will output a public URL like `http://abcd1234.ngrok.io`. Copy this URL; you’ll need it in Google Colab.

### 3. Interacting with Ollama in Google Colab

Now that Ollama is running locally and exposed via Ngrok, you can interact with it from Google Colab.

#### Connecting Colab to Your Local Ollama Instance

In your Google Colab notebook:

1. **Install Required Libraries**:
   - Colab comes with many libraries pre-installed, but you might need `requests` for API interactions.

   ```python
   !pip install requests
   ```

2. **Set Up the Connection**:
   - Use the Ngrok URL to connect Colab to your local Ollama instance.

   ```python
   import requests

   # Replace this URL with your Ngrok URL
   ollama_url = "http://abcd1234.ngrok.io"

   def query_ollama(prompt):
       response = requests.post(f"{ollama_url}/api/generate", json={"prompt": prompt})
       return response.json()

   # Test the connection
   response = query_ollama("What is Ollama?")
   print(response)
   ```

#### Running API Calls from Colab

You can now send API requests to your Ollama instance directly from Google Colab. Here’s an example of generating text:

```python
# Generate text from a prompt
prompt = "Write a story about a robot exploring Mars."
result = query_ollama(prompt)
print(result)
```

### 4. Advanced Usage

#### Customizing Ollama Models

Ollama allows you to customize and fine-tune models. You can pass additional parameters in your API request to adjust the model's behavior:

```python
def query_ollama_custom(prompt, temperature=0.7, max_tokens=100):
    payload = {
        "prompt": prompt,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(f"{ollama_url}/api/generate", json=payload)
    return response.json()

# Example with custom settings
custom_result = query_ollama_custom("Describe a futuristic city.", temperature=0.8, max_tokens=150)
print(custom_result)
```

#### Chaining API Calls for Complex Tasks

You can chain multiple API calls to create more complex workflows. For instance, you could first generate an outline for a story and then flesh out each section:

```python
# Generate an outline
outline_prompt = "Generate an outline for a science fiction story about time travel."
outline = query_ollama(outline_prompt)["text"]

# Generate the story based on the outline
story_prompt = f"Write a detailed story based on this outline:\n{outline}"
story = query_ollama(story_prompt)["text"]

print(story)
```

### 5. Conclusion

While Ollama is typically run locally, using Google Colab in conjunction with tools like Ngrok allows you to interact with Ollama remotely. This setup provides the best of both worlds: local control over your models and the convenience of cloud-based development. Whether you’re generating text, fine-tuning models, or creating complex workflows, this approach gives you the flexibility to experiment and iterate quickly.

By following this tutorial, you should be well-equipped to start using Ollama in your AI projects, leveraging the power of both local and cloud resources.
