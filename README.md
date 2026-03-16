# WebScour-A-Distributed-Web-Crawler-and-Search-Engine
WebScour – A Simple Search Engine
Introduction

WebScour is a simple web-based search engine designed to demonstrate the fundamental concepts of information retrieval systems. The project crawls webpages, extracts useful textual information, builds an index of the content, and allows users to search for relevant documents through a web interface.

The system works by collecting HTML pages, processing their text, and constructing an inverted index that maps words to the documents in which they appear. When a user enters a search query, the system processes the query, retrieves relevant documents from the index, calculates relevance scores using the TF-IDF (Term Frequency–Inverse Document Frequency) method, and ranks the documents accordingly.

The backend of WebScour is implemented using Python and exposes search functionality through a REST API built with FastAPI. The server is run using Uvicorn. A simple HTML and JavaScript based user interface allows users to submit queries and view ranked search results.

This project was developed as part of a milestone-based implementation of a search engine system, where each milestone focuses on a specific component such as crawling, indexing, and search functionality.

Features

Webpage crawling and HTML content extraction

Text preprocessing and tokenization

Inverted index creation

TF-IDF based document ranking

REST API for query processing

Interactive web interface for searching documents

Technologies Used

Python

FastAPI

Uvicorn

HTML

CSS

JavaScript

JSON

How It Works

Web pages are collected and stored locally.

Text is extracted and processed to build an inverted index.

TF-IDF values are calculated for ranking documents.

The FastAPI backend provides a search endpoint.

The user enters a query through the web interface.

The system retrieves and ranks relevant documents and displays the results.
