# PDF Generator from GitHub Repositories

This project is a FastAPI application that generates PDFs from Markdown files in a GitHub repository. It uses `weasyprint` to convert Markdown to HTML and then to PDF. The application exposes an endpoint where you can provide a GitHub repository URL, and it will generate a PDF of the repository's Markdown files.

## Prerequisites

- Docker
- Poetry (for managing Python dependencies)

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:

Build the Docker image

```bash
docker build -t pdf-generator .
```

Run the Docker Container

```bash
docker run --rm -p 8000:8000 pdf-generator
```

Once the container is running, you can access the FastAPI application at http://localhost:8000.


Go to http://localhost:8000/docs.
Locate the /generate-pdf/ endpoint in the Swagger UI.
Click on the "Try it out" button.
Enter the GitHub repository URL in the input field.
Click "Execute" to generate the PDF.
The PDF will be downloaded as repo.pdf.
