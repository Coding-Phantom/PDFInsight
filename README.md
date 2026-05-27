# PDFInsight

A full-stack **Retrieval-Augmented Generation (RAG)** web application that allows users to upload PDFs and ask questions about the content they upload. The system uses embeddings + vector search to retrieve relevant context and generate AI-powered answers using Google Gemini.

**Live demo:** [https://rag-frontend-qvep.onrender.com](https://rag-frontend-qvep.onrender.com)

---

## Features

- User authentication with JWT (register and login)
- Upload and manage PDF documents
- Ask questions about uploaded PDFs
- Live streaming AI responses (typing animation)
- List source citations used in context for AI response
- Click a source citation to open the PDF at the relevant page
- Select/deselect from multiple PDFs to add/remove context for the LLM to read
- Chat history with the ability to revisit and re-ask questions
- Delete PDFs and chat history entries
- Drag-and-drop PDF upload
- Per-user request usage tracking (300 requests per day limit with visual indicator)
- Mobile responsive layout with collapsible sidebar

---

## Tech Stack

### Backend
- **FastAPI** – REST API server
- **LangChain** – document processing + RAG pipeline
- **Google Gemini API** – LLM + embeddings
- **ChromaDB** – vector database
- **SQLite** – user data, PDF metadata, chat history, and usage tracking
- **PyPDFLoader** – PDF text extraction
- **JWT (python-jose)** – authentication tokens
- **bcrypt** – password hashing

### Frontend
- **React (TypeScript)**
- **Tailwind CSS**
- **React Markdown** – formatted AI responses
- **React PDF** – in-browser PDF viewer
- **Vite** – development server and build tool

### Deployment
- **Docker** – containerized development environment
- **Render** – production deployment (Python web service + static site)

---

## Installation

### Prerequisites

- Python 3.12+
- Node.js 18+
- Google Gemini API key

### Backend setup

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Create a .env file in the backend folder:

```
GOOGLE_API_KEY=your_api_key_here
SECRET_KEY=your_random_secret_here
```

Note: API keys are not included in the project for security reasons.

### Frontend setup

```bash
cd frontend
npm install
```

### Run the project locally

Backend (from the backend directory):
```bash
python app/main.py
```

Frontend (from the frontend directory, in a separate terminal):
```bash
npm run dev
```

Open http://localhost:5173 in your browser.

### Run with Docker

```bash
docker compose up -d --build
```

---

## Future Features

- Suggested questions based on the PDF context
- Improved RAG retrieval with better chunking strategies
- Admin page for monitoring usage across users
