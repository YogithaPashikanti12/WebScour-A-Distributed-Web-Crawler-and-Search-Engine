import os
import re
import math
import json
from bs4 import BeautifulSoup
from collections import defaultdict, Counter

PAGES_FOLDER = "pages"

inverted_index = defaultdict(list)
idf = {}
total_documents = 0


# -------------------------------
# Step 1: Load HTML Files
# -------------------------------
def load_documents():
    documents = {}

    for filename in os.listdir(PAGES_FOLDER):
        if filename.endswith(".html"):
            path = os.path.join(PAGES_FOLDER, filename)
            with open(path, "r", encoding="utf-8") as f:
                documents[filename] = f.read()

    return documents


# -------------------------------
# Step 2: Extract Visible Text
# -------------------------------
def extract_text(html):
    soup = BeautifulSoup(html, "html.parser")

    # Remove script and style
    for tag in soup(["script", "style"]):
        tag.decompose()

    text = soup.get_text()
    return text


# -------------------------------
# Step 3: Tokenization & Cleaning
# -------------------------------
def tokenize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    tokens = text.split()
    return tokens


# -------------------------------
# Step 4 & 5: TF + Inverted Index
# -------------------------------
def build_index(documents):
    global total_documents
    total_documents = len(documents)

    for doc_id, html in documents.items():
        text = extract_text(html)
        tokens = tokenize(text)

        term_freq = Counter(tokens)

        for word, freq in term_freq.items():
            inverted_index[word].append((doc_id, freq))


# -------------------------------
# Step 6 & 7: Compute IDF
# -------------------------------
def compute_idf():
    for word, doc_list in inverted_index.items():
        doc_count = len(doc_list)
        idf[word] = math.log(total_documents / doc_count)


# -------------------------------
# Step 8: Save to Disk
# -------------------------------
def save_to_disk():
    with open("inverted_index.json", "w") as f:
        json.dump(dict(inverted_index), f, indent=4)

    with open("idf.json", "w") as f:
        json.dump(idf, f, indent=4)


# -------------------------------
# Step 9: Validation Output
# -------------------------------
def print_summary():
    print("\n----- Indexing Summary -----")
    print("Total Documents Indexed:", total_documents)
    print("Total Unique Terms:", len(inverted_index))

    print("\nSample Index Entries:")
    for i, (word, postings) in enumerate(inverted_index.items()):
        print(word, "→", postings)
        if i == 5:
            break

    print("\nSample IDF Values:")
    for i, (word, value) in enumerate(idf.items()):
        print(word, "→", value)
        if i == 5:
            break


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    documents = load_documents()
    build_index(documents)
    compute_idf()
    save_to_disk()
    print_summary()