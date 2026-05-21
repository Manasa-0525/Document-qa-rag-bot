# Document QA RAG Bot

A Retrieval-Augmented Generation (RAG) based Question Answering system that allows users to ask questions from uploaded documents.  
The bot extracts content from PDFs, splits the text into chunks, generates embeddings, stores them in a vector database, retrieves the most relevant context, and generates answers with source citations.

This project demonstrates the complete RAG pipeline including document ingestion, chunking, embeddings, vector search, retrieval, and answer generation using open-source tools.

---

# Features

- Load and process PDF documents
- Automatic text chunking
- Semantic search using embeddings
- Vector database storage with ChromaDB
- Context-aware answer generation
- Source citation with page numbers
- Streamlit web interface
- Fully local pipeline without paid APIs
- Similarity threshold to prevent irrelevant or hallucinated answers

---

# Tech Stack

| Technology | Purpose | Version |
|---|---|---|
| Python | Core programming language | 3.11 |
| Streamlit | Frontend UI | Latest |
| LangChain | RAG pipeline framework | Latest |
| ChromaDB | Vector database | Latest |
| Sentence Transformers | Embedding generation | Latest |
| HuggingFace | Embedding models | Latest |
| PyPDF | PDF document loading | Latest |
| Torch | ML backend | Latest |

---

# Architecture Overview

## RAG Pipeline

1. **Document Ingestion**
   - PDF files are loaded from the `/data` folder
   - Text is extracted using PyPDF

2. **Chunking**
   - Documents are split into smaller overlapping chunks
   - RecursiveCharacterTextSplitter is used

3. **Embedding Generation**
   - Each chunk is converted into vector embeddings
   - Embeddings capture semantic meaning

4. **Vector Storage**
   - Embeddings are stored in ChromaDB
   - Enables fast semantic similarity search

5. **Retrieval**
   - User query is embedded
   - Most relevant chunks are retrieved

6. **Answer Generation**
   - Retrieved chunks are combined into a final response
   - Source citations are included

---

# Chunking Strategy

This project uses **Recursive Character Text Splitting** with chunk overlap.

### Configuration
- Chunk Size: 1000 characters
- Chunk Overlap: 200 characters

### Why this strategy?

- Prevents loss of context
- Improves retrieval accuracy
- Handles long PDF documents efficiently
- Overlapping chunks preserve sentence continuity

---

# Embedding Model and Vector Database

## Embedding Model

`sentence-transformers/all-MiniLM-L6-v2`

### Why this model?

- Lightweight and fast
- Good semantic understanding
- Works efficiently on local machines
- Popular open-source embedding model for RAG systems

---

## Vector Database

### ChromaDB

Why ChromaDB?

- Easy local setup
- Fast similarity search
- Persistent vector storage
- Integrates well with LangChain

---

# Project Structure

```bash
Document-qa-rag-bot/
│
├── data/
│   ├── ai_document.pdf
│   ├── cyber_security.pdf
│   ├── renewable_energy.pdf
│   └── ...
│
├── chroma_db/
│
├── src/
│   ├── ingest.py
│   ├── chunking.py
│   ├── embed_store.py
│   ├── retrieve.py
│   ├── generate_answer.py
│
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd Document-qa-rag-bot
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Add Documents

Place your PDF documents inside the `/data` folder.

---

## 5. Run Document Ingestion

```bash
python src/ingest.py
```

---

## 6. Run Chunking

```bash
python src/chunking.py
```

---

## 7. Create Vector Database

```bash
python src/embed_store.py
```

---

## 8. Run Retrieval Testing

```bash
python src/retrieve.py
```

---

## 9. Run Streamlit Application

```bash
streamlit run app.py
```

---

# Environment Variables

Create a `.env` file in the root directory.

Example:

```env
GOOGLE_API_KEY=your_api_key_here
HF_TOKEN=your_huggingface_token_here
```

Note:
- API keys are optional in the current local implementation
- Never commit real API keys to GitHub

---

# Example Queries

## Query 1
"What is Artificial Intelligence?"

Expected:
- Definition of AI
- Applications and concepts

---

## Query 2
"What are renewable energy mitigation options?"

Expected:
- Renewable energy strategies
- Environmental mitigation approaches

---

## Query 3
"How are IoT devices used in smart homes?"

Expected:
- IoT architecture
- Smart home automation concepts

---

## Query 4
"What are common cyber security threats?"

Expected:
- Malware
- Phishing
- Digital forensics concepts

---

## Query 5
"How does AI impact tourism industries?"

Expected:
- AI applications in travel
- Automation and personalization

---

# Known Limitations

- Answers depend completely on retrieved chunks
- No advanced LLM generation currently enabled
- Retrieval quality depends on chunking strategy
- Large PDFs may increase embedding time
- Context window is limited
- The system uses a similarity threshold to reduce hallucinated answers, but retrieval quality may still depend on document relevance and embedding accuracy

---

# Future Improvements

- Add Gemini/OpenAI integration
- Improve citation formatting
- Support DOCX and TXT files
- Add chat history memory
- Add hybrid search (BM25 + embeddings)
- Deploy on cloud platforms

---

# Author

K. Jhansi Manasa  
Final Year B.Tech CSE Student
