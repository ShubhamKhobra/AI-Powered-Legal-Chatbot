# 📚 AI-Powered Legal Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built with **LangChain**, **FAISS**, and **OpenAI GPT**, designed to answer legal and policy-related questions using uploaded documents.

---

## 📌 Project Overview

This project implements an **end-to-end RAG pipeline** that:

- Ingests and preprocesses legal documents.
- Splits them into semantic chunks for retrieval.
- Generates embeddings and stores them in a **FAISS** vector database.
- Retrieves top-matching chunks for a query.
- Uses **GPT-3.5-turbo** (via LangChain) to generate grounded, streamed answers.
- Displays responses in a **Streamlit** chatbot interface.

## 🎥 Demo

![AI-Powered Legal Chatbot Demo](demo/demo.gif)


