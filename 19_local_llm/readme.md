# Local LLM Deployment with Ollama and OpenWebUI

This guide provides step-by-step instructions for running a local language model (LLM) i.e. Llama 3.1 8B using Docker images of Ollama and OpenWebUI. By the end of this guide, you will have a fully functional LLM running locally on your machine.

## Prerequisites

Before starting, ensure that you have the following installed on your machine:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/) if you don't have it already.
- **Docker Compose** (optional): If you plan to manage multi-container applications, [install Docker Compose](https://docs.docker.com/compose/install/).

## Step 1: Run the Ollama and OpenWebUI Containers

In this step, you'll launch both the Ollama and OpenWebUI containers using Docker. These containers will be configured to store data persistently and restart automatically if needed.

### Running the Ollama Container

To start the Ollama container, execute the following command in your terminal:

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

This command performs the following actions:

- **Detached Mode (`-d`)**: Runs the container in the background, allowing you to continue using the terminal.
- **Volume Mount (`-v ollama:/root/.ollama`)**: Creates a Docker volume named `ollama` to persist data at `/root/.ollama` inside the container. This ensures your data remains intact even if the container is restarted or removed.
- **Port Mapping (`-p 11434:11434`)**: Maps port `11434` on your local machine to port `11434` inside the container, allowing you to access Ollama's services.
- **Container Name (`--name ollama`)**: Names the container `ollama` for easy reference.

### Running the OpenWebUI Container

Next, start the OpenWebUI container with the following command:

```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

This command performs the following actions:

- **Detached Mode (`-d`)**: Runs the container in the background.
- **Port Mapping (`-p 3000:8080`)**: Maps port `3000` on your local machine to port `8080` inside the container. This allows you to access the OpenWebUI interface through your web browser.
- **Host Gateway (`--add-host=host.docker.internal:host-gateway`)**: Adds an entry to the container's `/etc/hosts` file, enabling it to communicate with services running on your host machine.
- **Volume Mount (`-v open-webui:/app/backend/data`)**: Creates a Docker volume named `open-webui` to persist data at `/app/backend/data` inside the container, ensuring your data is saved even if the container is restarted.
- **Container Name (`--name open-webui`)**: Names the container `open-webui` for easy identification.
- **Automatic Restart (`--restart always`)**: Configures the container to restart automatically if it stops or if the Docker daemon is restarted, ensuring high availability.

With both containers running, you can now proceed to access the OpenWebUI interface.

![Containers](containers.png "Containers")

## Step 2: Access the OpenWebUI Interface

Once both containers are running, you can access the OpenWebUI interface through your web browser. Simply navigate to:

```
http://localhost:3000
```

Here, you can interact with the LLM powered by Ollama through a user-friendly web interface.

![Web UI](web_ui.png "Web UI")

## Step 3: Download the Llama Model in the Ollama Container

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
   ollama run phi
   ```

4. **Verify the Download**: You can verify that the model has been successfully downloaded by checking the container logs or listing the contents of the model directory inside the container.

![Pull LLM](pull_llm.png "Pull LLM")

## Step 4: Verify the LLM is Running

To ensure the LLM is running correctly, you can check the logs of the Ollama container:

```bash
docker logs ollama
```

You should see the model initialization and any requests being processed. This will confirm that your LLM is up and running smoothly.

### Step 5: Model Setting

![Model Setting](model_seeting.png "Model Setting")

## Step 6: Stop the Containers

When you're done using the LLM, you can stop and remove the containers with the following commands:

```bash
docker stop ollama open-webui
docker rm ollama open-webui
```

These commands will stop and remove both the Ollama and OpenWebUI containers, cleaning up your environment.

## Troubleshooting

- **Port Conflicts**: If ports `11434` or `3000` are already in use, you can change the host port mappings (e.g., `-p 11435:11434` or `-p 3001:8080`).
- **Container Logs**: Check logs for any errors using `docker logs <container-name>`.

## Important Note

If you are having memory issue on your machine please use this service:

https://www.docker.com/play-with-docker/

## Challenge Assignment

Please run Llama 3.1 8B on Google Colab


## Conclusion

Congratulations! You have successfully set up and run a local LLM using Docker images of Ollama and OpenWebUI. Enjoy experimenting with your model locally!





