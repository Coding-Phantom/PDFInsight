# PDF RAG Web App

A small FastAPI + React + Tailwind CSS project for asking questions about uploaded PDF context.

## Project Shape

- `backend/` - FastAPI app and PDF/RAG logic
- `frontend/` - React + Tailwind user interface

## First Milestone

This version is intentionally simple:

- The backend exposes health, PDF list, toggle, and ask endpoints.
- The frontend shows PDFs, lets users include or remove each one from context, and sends a question.
- The answer endpoint returns a placeholder response so we can wire up the app before adding embeddings.

## Backend

```powershell
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

If PowerShell blocks activation scripts, use:

```powershell
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python -m uvicorn app.main:app --reload --port 8000
```

## Frontend

```powershell
cd frontend
npm.cmd install
npm.cmd run dev
```

Then open the local URL shown by Vite, usually `http://localhost:5173`.

## Next Milestone

Next we can add real PDF upload and text extraction, then chunking, embeddings, and retrieval.
