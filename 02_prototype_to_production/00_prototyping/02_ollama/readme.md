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
   docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
   ```

   - This command pulls the latest Ollama Docker image and runs it on port 11434.

#### Using Ngrok to Expose Local Ollama Instance to Google Colab

To interact with Ollama from Google Colab, you need to expose your local Ollama instance to the internet. Ngrok is a handy tool that creates secure tunnels to localhost, allowing you to access your local server from anywhere.

1. **Install Ngrok**:
   - Download and install Ngrok from [here](https://ngrok.com/download).

2. **Run Ngrok**:
   - Start Ngrok to tunnel your local Ollama instance.

   ```bash
   ngrok http --log stderr 11434 --host-header localhost:11434
   ```

   - This command will provide a public URL that forwards to your local Ollama instance on port 11434.

3. **Copy the Public URL**:
```bash
t=2024-09-05T18:46:58+0500 lvl=info msg="started tunnel" obj=tunnels name=command_line addr=http://localhost:11434 url=https://99fd-129.ngrok-free.app
```
   - Ngrok will output a public URL like `http://abcd1234.ngrok.io`. Copy this URL; you’ll need it in Google Colab.

### 3: Download the Llama Model in the Ollama Container

To download the Llama 3.1 model within the Ollama container, follow these steps:

1. **Open Docker Dashboard**: Navigate to your Docker Dashboard or use the command line.
2. **Access the Ollama Container**:
   - Find the `ollama` container from the list of running containers.
   - Click on the container to open the details.
   - Go to the `Exec` tab (or use `docker exec` via terminal).
3. **Run the Model Download Command**:
   - In the command input field, type the following command and execute it:
   
   ```bash
   ollama run llama3.1
   ```

   This command will initiate the download of the Llama 3.1 model into the container.

   Note: If you PC hardware is weak you can run the following model:

   ```bash
   ollama run tinyllama
   ```

### 4. Interacting with Ollama in Google Colab

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
ollama_url = "https://99fd-104-28-212-129.ngrok-free.app"

def query_ollama(prompt, model="tinyllama"):
   headers = {
      "ngrok-skip-browser-warning": "true"  # This header bypasses the Ngrok browser warning
   }
   data = {
      "prompt": prompt,
      "model": model,
      "stream": False  # Disable streaming for a simple response
   }
   
   # Sending the request to generate a completion from the model
   response = requests.post(f"{ollama_url}/api/generate", json=data, headers=headers)
   
   # If the response was successful, return the generated text
   if response.status_code == 200:
      return response.json().get("response", "No response found")
   else:
      return f"Error: {response.status_code}, {response.text}"

# Test the connection with a simple Hello World prompt
response = query_ollama("Greet me in 3 words!")
print(response)
```

#### Running API Calls from Colab

You can now send API requests to your Ollama instance directly from Google Colab. Here’s an example of generating text:

```python
# Generate text from a prompt
prompt = "Write a story about a robot exploring Mars within 50 words."
result = query_ollama(prompt)
print(result)
```

### 5. Advanced Usage

#### Customizing Ollama Models

Ollama allows you to customize and fine-tune models. You can pass additional parameters in your API request to adjust the model's behavior:

```python
def query_ollama_custom(prompt, model="tinyllama", temperature=0.7, max_tokens=100):
    headers = {
        "ngrok-skip-browser-warning": "true"  # This header bypasses the Ngrok browser warning
    }
    data = {
        "prompt": prompt,
        "model": model,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False  # Disable streaming for a simple response
    }
    
    # Sending the request to generate a completion from the model
    response = requests.post(f"{ollama_url}/api/generate", json=data, headers=headers)
    
    # If the response was successful, return the generated text
    if response.status_code == 200:
        return response.json().get("response", "No response found")
    else:
        return f"Error: {response.status_code}, {response.text}"

# Test the connection with a simple Hello World prompt
custom_result = query_ollama_custom("Describe a futuristic city.", temperature=0.8, max_tokens=50)
print(response)
```

#### Streaming API Response

```python
def query_ollama_streaming(prompt, model="tinyllama"):
    headers = {
        "ngrok-skip-browser-warning": "true"  # This header bypasses the Ngrok browser warning
    }
    data = {
        "prompt": prompt,
        "model": model, 
        "stream": True
    }
    
    # Stream the request to handle the sequence of JSON objects
    response = requests.post(f"{ollama_url}/api/generate", json=data, headers=headers)
    
    # Extract the text response
    text_response = ""
    for line in response.iter_lines():
        if line:
            try:
                json_data = json.loads(line)
                if "response" in json_data:
                    text_response += json_data["response"]
                    print(f"Partial response: {text_response}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    return text_response

# Test the connection
response_text = query_ollama("What is Generative AI?")
print(response_text)
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

### 6. Conclusion

While Ollama is typically run locally, using Google Colab in conjunction with tools like Ngrok allows you to interact with Ollama remotely. This setup provides the best of both worlds: local control over your models and the convenience of cloud-based development. Whether you’re generating text, fine-tuning models, or creating complex workflows, this approach gives you the flexibility to experiment and iterate quickly.

By following this tutorial, you should be well-equipped to start using Ollama in your AI projects, leveraging the power of both local and cloud resources.
