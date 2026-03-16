from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from search_engine import search

app = FastAPI()

# Enable CORS so UI.html can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Home Route
# -------------------------
@app.get("/")
def home():
    return {"message": "WebScour Search Engine Running"}

# -------------------------
# Search API
# -------------------------
@app.get("/search")
def search_api(q: str):

    results = search(q)

    return results