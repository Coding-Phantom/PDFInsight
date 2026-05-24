# 📄 RAG PDF App (Retrieval-Augmented Generation)

A full-stack **Retrieval-Augmented Generation (RAG)** web application that allows users to upload PDFs and ask questions about the content they upload. The system uses embeddings + vector search to retrieve relevant context and generate AI-powered answers using Google Gemini.

---

## 🚀 Features

- 📁 Upload and manage PDF documents
- 🤖 Ask questions about uploaded PDFs
- 🧠 Responses using Gemini LLM, with given context chunks
- 📌 List source citations used in context for AI response
- 🗂️ Can select/deselect from multiple PDFs to add/remove context for the LLM to read

---

## 🧠 Tech Stack

### Backend
- **FastAPI** – REST API server
- **LangChain** – document processing + RAG pipeline
- **Google Gemini API** – LLM + embeddings
- **ChromaDB** – vector database
- **SQLite** – PDF metadata storage
- **PyPDFLoader** – PDF text extraction

### Frontend
- **React (TypeScript)**
- **Tailwind CSS**
- **React Markdown** – formatted AI responses
- **Fetch API** – backend communication

---

## ⚙️ Architecture
