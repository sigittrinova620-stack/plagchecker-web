"""
FastAPI Server for Turnitin-style Plagiarism Detection
"""
import os
import shutil
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from detector import PlagiarismDetector, extract_text_from_file

BASE_DIR = Path(__file__).resolve().parent
REPO_DIR = BASE_DIR / "repository"
UPLOADS_DIR = BASE_DIR / "uploads"
STATIC_DIR = BASE_DIR / "static"

REPO_DIR.mkdir(exist_ok=True)
UPLOADS_DIR.mkdir(exist_ok=True)
STATIC_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Turnitin Similarity Checker Clone")
detector = PlagiarismDetector(REPO_DIR)

# Serve static frontend
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_file = STATIC_DIR / "index.html"
    if not index_file.exists():
        raise HTTPException(status_code=404, detail="Index HTML not found")
    return index_file.read_text(encoding="utf-8")

@app.get("/api/repository")
async def list_repository_documents():
    """List all reference documents in the repository."""
    docs = detector.get_reference_documents()
    items = []
    for d in docs:
        items.append({
            "id": d["id"],
            "filename": d["filename"],
            "title": d["title"],
            "word_count": len(d["tokens"])
        })
    return items

@app.post("/api/repository/upload")
async def upload_repository_document(file: UploadFile = File(...)):
    """Upload a new reference document into the database."""
    file_path = REPO_DIR / file.filename
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"status": "success", "filename": file.filename}

@app.post("/api/check")
async def check_document_similarity(
    file: UploadFile = File(None),
    text: str = Form(None),
    title: str = Form(None)
):
    """
    Check document similarity against the reference database.
    Accepts either an uploaded file or raw text.
    """
    doc_text = ""
    filename = "Pasted_Text"
    
    if file and file.filename:
        filename = file.filename
        temp_path = UPLOADS_DIR / file.filename
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        doc_text = extract_text_from_file(temp_path)
    elif text:
        doc_text = text
        if title:
            filename = title
            
    if not doc_text.strip():
        raise HTTPException(status_code=400, detail="Tidak ada teks atau isi file yang terbaca.")

    # Run detection
    result = detector.compare_documents(doc_text, min_match_words=4)
    result["filename"] = filename
    return result

if __name__ == "__main__":
    import uvicorn
    print("Starting Turnitin Clone at http://localhost:8000 ...")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
