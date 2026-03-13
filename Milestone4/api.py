from fastapi import FastAPI
from search_engine import search

app = FastAPI()


@app.get("/")
def home():
    return {"message": "WebScour Search Engine Running"}


@app.get("/search")
def search_api(q: str):

    results = search(q)

    response = []

    for doc, score in results:

        response.append({
            "document": doc,
            "score": round(score, 3)
        })

    return response