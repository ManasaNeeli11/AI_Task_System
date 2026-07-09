import faiss
import numpy as np

dimension = 384

index = faiss.IndexFlatL2(dimension)

documents = []


def add_document(text, embedding):
    vector = np.array([embedding]).astype("float32")
    index.add(vector)
    documents.append(text)


def search_document(query_embedding, k=3):
    vector = np.array([query_embedding]).astype("float32")
    distances, indices = index.search(vector, k)

    results = []

    for i in indices[0]:
        if i != -1:
            results.append(documents[i])

    return results