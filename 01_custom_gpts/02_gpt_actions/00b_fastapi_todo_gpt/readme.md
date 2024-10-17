
---

# Todo App

This project is a full-stack Todo application built using FastAPI for the backend and Next.js for the frontend. The application is containerized using Docker and accessible through a Cloudflare Tunnel. This README provides detailed instructions on setting up, running, and using the application.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running the Application](#running-the-application)
4. [Project Structure](#project-structure)
5. [API Documentation](#api-documentation)
6. [Using the Application](#using-the-application)
7. [Deploying with Cloudflare Tunnel](#deploying-with-cloudflare-tunnel)
8. [Project Testing](#project-testing)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)


## Project Overview

This Todo application allows users to create, update, delete, and view their tasks. The application is built with a microservices architecture where the backend and frontend are separated into different services. Docker is used to containerize the services, and Cloudflare Tunnel is employed to make the application accessible from the internet.

## Technologies Used

- **Backend**: FastAPI (Python), SQLModel (ORM), PostgreSQL (Database)
- **Frontend**: Next.js (React framework), Tailwind CSS (Styling)
- **DevOps**: Docker, Docker Compose, Cloudflare Tunnel

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your local machine:

- **Docker**: To run the application in containers.
- **Docker Compose**: To manage multi-container Docker applications.
- **Cloudflare CLI (`cloudflared`)**: For setting up a Cloudflare Tunnel.
- **Node.js**: To run the Next.js frontend locally.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/panaversity/learn-applied-generative-ai-fundamentals.git
   cd 15_gpt_actions/00b_fastapi_todo_gpt
   ```

2. **Set Up Environment Variables**:
   
   Create a `.env.local` file in the frontend directory and `.env` file in the backend directory:

   ```bash
   # Backend (.env)
   DATABASE_URL=postgresql://waniakazmi:my_password@postgres_db:5432/todo_db

   # Frontend (.env.local)
   NEXT_PUBLIC_API_URL=https://localhost:8001/
   ```

3. **Install Dependencies**:
   
   The dependencies are managed by Docker, so there’s no need to install them manually.

### Running the Application

1. **Start the Application**:

   Use Docker Compose to start the entire application (both backend and frontend services):

   ```bash
   docker-compose up -d
   ```

   This command will build and run the containers for the backend, frontend, and database.

2. **Access the Application**:

   - The frontend will be accessible at `http://localhost:3000`.
   - The backend API will be accessible at `http://localhost:8001/docs`.

## Project Structure

```plaintext
.
├── backend/                # FastAPI backend service
│   ├── app/
│   │   ├── main.py         # Main application entry point
│   │   ├── models.py       # SQLModel models for the database
│   │   ├── database.py     # Database connection and session management
│   │   ├── configuration.py # Configuration settings
│   │   └── ...
│   ├── Dockerfile          # Dockerfile for the backend
│   ├── pyproject.toml      # Python dependencies (managed by Poetry)
│   └── ...
├── frontend/               # Next.js frontend service
│   ├── src/app
│   │   ├── page.tsx       # Main page component
│   │   └── ...
│   ├── components/         # Reusable UI components
│   ├── public/             # Public static assets
│   ├── styles/             # Global styles
│   ├── Dockerfile          # Dockerfile for the frontend
│   └── ...
├── docker-compose.yml      # Docker Compose configuration file
└── README.md               # Project README
```

## API Documentation

The backend provides the following API endpoints:

- **`GET /todos/`**: Retrieve all todos.
- **`POST /todos/`**: Create a new todo.
- **`PUT /todos/{todo_id}`**: Update an existing todo by its ID.
- **`DELETE /todos/{todo_id}`**: Delete a todo by its ID.

### Example API Request

**Create a New Todo**:

```bash
curl -X POST http://localhost:8001/todos/ -H "Content-Type: application/json" -d '{"content": "Buy groceries"}'
```

## Using the Application

1. **Adding Todos**: Use the input box on the frontend to add a new todo item. Click the "Add Todo" button to submit.
2. **Updating Todos**: Click the "Edit" button next to a todo item, update the content, and save.
3. **Deleting Todos**: Click the "Delete" button next to a todo item to remove it from the list.

## Deploying with Cloudflare Tunnel

To make your application accessible from the internet:

1. **Install Cloudflare CLI**:
   
   ```bash
   npm install -g cloudflared
   ```

2. **Login to Cloudflare**:

   ```bash
   cloudflared login
   ```

   Follow the instructions in the browser to authenticate.

3. **Create a Cloudflare Tunnel**:

   ```bash
   cloudflared tunnel create my-tunnel
   ```

   This will generate a tunnel ID and credentials file.

4. **Start the Tunnel**:

   ```bash
   cloudflared tunnel --url http://localhost:8001
   ```

   The Cloudflare Tunnel will provide you with a URL like `https://your-tunnel-name.trycloudflare.com`, which you can use as the public endpoint.

   <b>Note:</b> This project uses a custom domain linked via Cloudflare, resulting in a persistent URL: https://web.wania.xyz/. You will encounter this URL throughout the project. For your implementation, please replace it with your own live URL.

   ![Creating Tunnel](./assets/tunnel1.PNG)
   ![Tunnel Created](./assets/tunnel2.PNG)


5. **Custom GPT URL**:

   Your custom GPT can be accessed via the following URL:

   [Task Manager Assistant GPT](https://chatgpt.com/g/g-VbDzJGI77-task-manager-assistant)

   Here’s a screenshot of the Task Manager Assistant GPT:

   ![Task Manager Assistant GPT](./assets/gpt.PNG)

## Project Testing
We will perform all CRUD operations through our custom GPT and then check all changes on our frontend page
   1. Initialize Todo List with empty bucket
      ![Task Manager Assistant GPT](./assets/testing1.PNG)
      ![Task Manager Assistant GPT](./assets/testing1.1.PNG)
   2. Add Todo - we added "Todo task 1" from CUI and can see manipulation occur at GUI
      ![Task Manager Assistant GPT](./assets/testing2.1.PNG)
      ![Task Manager Assistant GPT](./assets/testing2.2.PNG)
   3. Update Todo - Add another Todo and make changes in it
      ![Task Manager Assistant GPT](./assets/testing3.PNG)
      ![Task Manager Assistant GPT](./assets/testing3.1.PNG)
      ![Task Manager Assistant GPT](./assets/testing3.2.PNG)
      ![Task Manager Assistant GPT](./assets/testing3.3.PNG)
   4. Delete Todo - Delete "Todo task 3" todo
      ![Task Manager Assistant GPT](./assets/testing4.1.PNG)
      ![Task Manager Assistant GPT](./assets/testing4.2.PNG)
   5. Get Todo - Show all todos
      ![Task Manager Assistant GPT](./assets/testing5.PNG)

## Troubleshooting

- **CORS Errors**: Ensure the backend has the correct CORS settings to allow requests from the frontend's domain.
- **Database Connection Issues**: Double-check the `DATABASE_URL` in the backend `.env` file.
- **Cloudflare Issues**: Ensure your tunnel is correctly configured and running.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---