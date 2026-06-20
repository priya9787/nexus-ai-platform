# NexusAI Platform

Enterprise-style conversational AI platform for private document Q&A. NexusAI combines PDF ingestion, Qdrant vector retrieval, LangGraph agent orchestration, role-aware access filtering, and a Vue streaming chat interface.

This project is built as a portfolio-grade AI engineering system: the goal is to show how a real enterprise RAG application is structured, where documents are ingested into a private knowledge base and users query them through a governed chat interface.

## Implemented Features

- PDF document upload, parsing, chunking, embedding, and indexing.
- Qdrant dense vector search over uploaded enterprise documents.
- Role-aware retrieval filtering using document-level `allowed_roles` metadata.
- LangGraph multi-step agent workflow with router, retrieval, summarizer, and critic nodes.
- Server-sent event streaming for real-time assistant responses.
- Source citations with page metadata and access-role visibility.
- Local chat session history with saved messages, sources, and agent path.
- Grounded generation behavior that returns no sources when the model says it does not know.
- Vue dashboard, documents, chat, monitoring, and settings pages.

## Architecture

```text
Frontend: Vue + Vite + Pinia
    |
    | /api/v1/upload
    | /api/v1/stream
    v
Backend: FastAPI
    |
    | LangGraph agent workflow
    | Router -> Retrieval/Summarizer -> Critic
    v
RAG Services
    |
    | PDF loader
    | Recursive chunking
    | Sentence Transformers embeddings
    | RBAC metadata
    v
Qdrant Vector DB
```

## Tech Stack

- **Frontend:** Vue, Vite, Pinia
- **Backend:** FastAPI, SSE streaming
- **Agents:** LangGraph
- **LLM:** Groq-hosted Llama 3.3 model
- **Embeddings:** Sentence Transformers `all-MiniLM-L6-v2`
- **Vector DB:** Qdrant
- **Document Processing:** LangChain PDF loader and recursive text splitter
- **Local Services:** Docker Compose for Qdrant and Redis

## Current Resume Bullets

Use these bullets for the current state of the project. They are intentionally written to be defensible from the code and UI.

- Architected an enterprise-style conversational AI platform with FastAPI, Vue, LangGraph, Qdrant, and streaming chat for document-grounded Q&A over private uploaded knowledge bases.
- Built a RAG pipeline using PDF ingestion, recursive document chunking, Sentence Transformers embeddings, Qdrant dense vector retrieval, and grounded Llama 3.3 generation to reduce unsupported answers.
- Implemented LangGraph-based multi-agent orchestration with router, retrieval, summarization, and critic nodes, exposing source citations and agent path traces in the chat interface.
- Added role-aware retrieval controls using document-level access metadata and Qdrant filters, enabling users to restrict document access by role such as HR, Engineering, Finance, and Admin.
- Developed a recruiter-ready Vue product interface with dashboard, document ingestion, streaming chat, source citations, local chat history, monitoring, and settings surfaces.

## Resume Claims To Avoid Until Implemented

Do not claim these yet unless the corresponding work is added and tested:

- FAISS retrieval
- Active BM25 hybrid retrieval
- Active cross-encoder reranking
- BERT-based semantic chunking
- Presidio PII masking
- Prompt injection defense
- Tenant-level isolation
- Full audit logging
- LangSmith or RAGAS evaluation scores
- QLoRA/PEFT fine-tuning or 4-bit quantization

## Planned Improvements

- Hybrid retrieval with Qdrant dense search plus BM25 sparse retrieval.
- Cross-encoder reranking integrated into the active query path.
- Backend-persisted chat sessions using Redis or a database.
- Document management page with indexed files, chunk counts, roles, and delete/re-index actions.
- PII redaction before indexing and generation.
- Prompt injection detection for uploaded documents and user queries.
- Tenant-aware document isolation.
- Audit logging for query, role, retrieved sources, and model response.
- RAGAS/LangSmith evaluation pipeline for faithfulness, answer relevancy, latency, and token usage.

## Local Setup

### 1. Start Infrastructure

```powershell
docker compose up qdrant redis
```

Qdrant dashboard:

```text
http://localhost:6333/dashboard
```

### 2. Start Backend

```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Create `backend/.env` with your Groq key:

```env
GROQ_API_KEY=your_key_here
```

### 3. Start Frontend

```powershell
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

## Demo Flow

1. Open the Documents page.
2. Upload a PDF and select allowed roles, for example `hr`.
3. Open the Chat page.
4. Set Active role to `engineering` and ask about the HR document.
5. The assistant should not retrieve HR-only sources.
6. Switch Active role to `hr` and ask again.
7. The assistant should answer using the HR document and show citations.

## Notes

- Documents uploaded before the RBAC feature may not contain `allowed_roles` metadata. Re-upload documents after restarting the backend for clean RBAC tests.
- `admin` is treated as a full-access role.
- Non-admin roles are filtered against document `allowed_roles`.
- Monitoring currently shows active/planned service signals, not measured benchmark results.
