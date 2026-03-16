
import json
import re
from collections import defaultdict

# -------------------------
# Load index data
# -------------------------
with open("inverted_index.json") as f:
    inverted_index = json.load(f)

with open("idf.json") as f:
    idf = json.load(f)


# -------------------------
# Query Tokenization
# -------------------------
def tokenize_query(query):
    query = query.lower()
    query = re.sub(r"[^a-z0-9\s]", "", query)
    tokens = query.split()
    return tokens


# -------------------------
# Search Function
# -------------------------
def search(query, top_n=5):

    tokens = tokenize_query(query)

    scores = defaultdict(float)

    for word in tokens:

        if word in inverted_index:

            postings = inverted_index[word]

            for doc_id, tf in postings:

                score = tf * idf.get(word, 0)

                scores[doc_id] += score

    # Sort by score
    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # Convert results to JSON-friendly format
    results = []

    for doc, score in ranked_docs[:top_n]:
        results.append({
            "document": doc,
            "score": round(score, 3)
        })

    return results


# -------------------------
# Test search in terminal
# -------------------------
if __name__ == "__main__":

    while True:

        query = input("Enter search query: ")

        results = search(query)

        print("\nResults:")

        for item in results:
            print(item["document"], "Score:", item["score"])