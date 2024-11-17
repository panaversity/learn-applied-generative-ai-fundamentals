from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
import markdown
from weasyprint import HTML
import os
import zipfile
import tempfile
import io
from typing import Optional

app = FastAPI()

class RepoURL(BaseModel):
    url: str

def download_repo_zip(repo_url: str) -> bytes:
    repo_url = repo_url.rstrip('.git')
    repo_zip_url = f"{repo_url}/archive/refs/heads/main.zip"
    response = requests.get(repo_zip_url)
    response.raise_for_status()
    return response.content

def extract_markdown_files(zip_content: bytes, temp_dir: str) -> list:
    markdown_files = []
    with zipfile.ZipFile(io.BytesIO(zip_content), 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
        for root, _, files in os.walk(temp_dir):
            for file in files:
                if file.endswith('.md'):
                    markdown_files.append(os.path.join(root, file))
    return markdown_files

def convert_markdown_files_to_html(markdown_files: list, base_dir: str) -> str:
    combined_html = ""
    for md_file in markdown_files:
        relative_path = os.path.relpath(md_file, base_dir)
        dir_name = os.path.dirname(relative_path)
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        html_content = markdown.markdown(md_content, extensions=['extra'])
        html_content = remove_images(html_content)
        combined_html += f"<h2>Directory: {dir_name}</h2>\n" + html_content + "<hr>"
    return combined_html

def remove_images(html_content: str) -> str:
    import re
    html_content = re.sub(r'<img[^>]*>', '', html_content)
    return html_content

def create_pdf_from_html(html_content: str) -> io.BytesIO:
    pdf_stream = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_stream)
    pdf_stream.seek(0)
    return pdf_stream

@app.post("/generate-pdf/")
async def generate_pdf(repo_url: str):
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            zip_content = download_repo_zip(repo_url)
            markdown_files = extract_markdown_files(zip_content, temp_dir)
            combined_html = convert_markdown_files_to_html(markdown_files, temp_dir)
            pdf_stream = create_pdf_from_html(combined_html)
            return StreamingResponse(pdf_stream, media_type="application/pdf", headers={"Content-Disposition": "attachment; filename=repo.pdf"})
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Error fetching repository: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
