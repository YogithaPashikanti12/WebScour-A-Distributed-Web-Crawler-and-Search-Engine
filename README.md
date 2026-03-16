# WebScour-A-Distributed-Web-Crawler-and-Search-Engine

## Introduction

**WebScour** is a simple web-based search engine developed to demonstrate the core concepts of information retrieval systems. The project collects web pages, processes their content, builds an inverted index, and allows users to search for relevant documents through a web interface.

The system extracts text from HTML pages, performs preprocessing and tokenization, and constructs an inverted index that maps terms to the documents in which they appear. When a user enters a query, the system retrieves matching documents and ranks them using the **TF-IDF (Term Frequency–Inverse Document Frequency)** scoring technique.

The backend of the system is implemented using Python with FastAPI for building the REST API, and the server is run using Uvicorn. A simple HTML and JavaScript based interface allows users to enter queries and view ranked search results.

This project demonstrates the working of a search engine pipeline including crawling, indexing, and query processing.

---

## Features

- Webpage crawling and HTML content extraction  
- Text preprocessing and tokenization  
- Inverted index creation  
- TF-IDF based document ranking  
- REST API for query processing  
- Interactive web interface for searching documents  

---

## Technologies Used

- Python  
- FastAPI  
- Uvicorn  
- HTML  
- CSS  
- JavaScript  
- JSON  

---

## How It Works

1. Web pages are collected and stored locally.  
2. Text is extracted from HTML pages and preprocessed.  
3. An inverted index is created to map words to documents.  
4. TF-IDF scores are calculated to measure document relevance.  
5. The FastAPI backend provides a search API endpoint.  
6. The user enters a query through the web interface.  
7. The system retrieves and ranks relevant documents and displays the results.
---
## Execution Order

1️⃣ RabbitMQ server
2️⃣ python producer.py
3️⃣ python worker.py
4️⃣ python indexer.py
5️⃣ uvicorn api:app --reload
6️⃣ Open ui.html

