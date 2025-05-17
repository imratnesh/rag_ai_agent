# Resume AI Agent with RAG

An intelligent resume analysis system that uses RAG (Retrieval-Augmented Generation) to answer questions about candidate resumes. The system uses ChromaDB for vector storage, Sentence Transformers for embeddings, and Ollama for LLM responses.

## Features

- PDF Resume Upload
- Semantic Search
- Interactive Chat Interface
- RAG-based Question Answering

## Prerequisites

- Python 3.10 or higher
- Ollama installed and running locally
- Mistral model pulled in Ollama

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd rag_ai_agent
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Pull the Mistral model in Ollama:
```bash
ollama pull mistral
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided URL (usually http://localhost:8501)

3. Upload a resume PDF using the file uploader

4. Ask questions about the candidate in the chat interface

## Project Structure

- `app.py`: Main Streamlit application
- `rag.py`: RAG implementation with ChromaDB and Ollama
- `resumes/`: Directory for uploaded resumes
- `resume_db/`: ChromaDB storage directory

## Dependencies

- streamlit
- chromadb
- sentence-transformers
- ollama
- PyMuPDF (fitz)
- torch

## License

MIT 