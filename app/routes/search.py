# & "C:\Program Files\MySQL\MySQL Server 9.7\bin\mysql.exe" -u root -p
from fastapi import APIRouter

from app.services.embedding import create_embedding
from app.services.vector_db import search_document

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


@router.get("/")
def semantic_search(query: str):

    embedding = create_embedding(query)

    results = search_document(embedding)

    return {
        "query": query,
        "results": results
    }