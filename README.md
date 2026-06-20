# NexusAI Platform

Enterprise-style conversational AI platform for private document question-answering using Retrieval-Augmented Generation (RAG).

NexusAI enables organizations to upload internal documents, index them into a vector database, and interact with them through a governed conversational interface powered by LLMs and agent workflows.

The platform combines document ingestion, role-based retrieval controls, vector search, LangGraph orchestration, and real-time streaming responses to simulate a production-ready enterprise AI system.

---

## Key Features

### Document Ingestion

* Upload PDF documents through a web interface
* Automatic document parsing and text extraction
* Recursive chunking for retrieval optimization
* Embedding generation using Sentence Transformers
* Vector indexing in Qdrant

### Retrieval-Augmented Generation (RAG)

* Dense vector similarity search
* Context-aware document retrieval
* Source citation generation
* Page-level metadata tracking
* Grounded answer generation

### Role-Based Access Control (RBAC)

* Document-level access permissions
* Role-aware retrieval filtering
* Configurable access roles:

  * Admin
  * HR
  * Engineering
  * Finance

### Agent Workflow

LangGraph orchestrates a multi-step reasoning pipeline:

Router → Retrieval → Summarizer → Critic

The workflow:

1. Routes incoming queries
2. Retrieves relevant documents
3. Generates grounded answers
4. Validates response quality before returning results

### Real-Time Chat Experience

* Server-Sent Events (SSE) streaming
* Source citations
* Agent execution trace visualization
* Local chat history persistence
* Session management

---

## System Architecture

```text
Frontend (Vue + Vite + Pinia)
|
| REST APIs
| SSE Streaming
v
Backend (FastAPI)
|
| LangGraph Workflow
| Router -> Retrieval -> Summarizer -> Critic
v
RAG Layer
|
| PDF Processing
| Recursive Chunking
| Embeddings
| Metadata Filtering
v
Qdrant Vector Database
```

---

## Technology Stack

### Frontend

* Vue 3
* Vite
* Pinia
* Vue Router

### Backend

* FastAPI
* Python
* Server-Sent Events (SSE)

### AI & Retrieval

* LangGraph
* LangChain
* Groq
* Llama 3.3
* Sentence Transformers
* Qdrant

### Infrastructure

* Docker Compose
* Redis
* Qdrant

---

## Project Structure

```
NexusAI/
│
├── backend/
│   ├── api/
│   ├── services/
│   ├── agents/
│   ├── models/
│   └── uploads/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── stores/
│
├── docker-compose.yml
└── README.md
```

---

## Local Setup

### Start Infrastructure

```bash
docker compose up qdrant redis
```

Qdrant Dashboard:

```
http://localhost:6333/dashboard
```

### Start Backend

```bash
cd backend

uvicorn app.main:app 
--host 0.0.0.0 
--port 8000 
--reload
```

Create:

```
backend/.env
```

```env
GROQ_API_KEY=your_key_here
```

### Start Frontend

```bash
cd frontend

npm install
npm run dev
```

Frontend URL:

```
http://localhost:5173
```

---

## Demo Workflow

1. Upload a PDF document.
2. Assign allowed access roles.
3. Open the chat interface.
4. Ask questions related to the uploaded document.
5. Observe retrieval citations and agent execution path.
6. Switch user roles and verify RBAC filtering behavior.

---

## Current Capabilities

* PDF ingestion
* Vector search
* LangGraph orchestration
* Streaming responses
* Source citations
* Role-based retrieval filtering
* Chat history persistence
* Monitoring dashboard

---

## Roadmap

* Hybrid Retrieval (Dense + BM25)
* Cross-Encoder Reranking
* Redis-Persisted Conversations
* PII Detection & Redaction
* Prompt Injection Protection
* Multi-Tenant Isolation
* Audit Logging
* LangSmith Observability
* RAGAS Evaluation Pipeline

---

## License

MIT License
