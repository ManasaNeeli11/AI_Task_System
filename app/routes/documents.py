from fastapi import APIRouter, UploadFile, File
import os
import PyPDF2

from app.services.embedding import create_embedding
from app.services.vector_db import add_document

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = ""

    if file.filename.endswith(".txt"):

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

    elif file.filename.endswith(".pdf"):

        with open(file_path, "rb") as pdf:

            reader = PyPDF2.PdfReader(pdf)

            for page in reader.pages:
                text += page.extract_text()

    # ---------- ADD THESE LINES HERE ----------
    embedding = create_embedding(text)
    add_document(text, embedding)
    # ------------------------------------------

    return {
        "message": "Document uploaded successfully",
        "filename": file.filename,
        "characters": len(text)
    }