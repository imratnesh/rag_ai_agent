import fitz  # PyMuPDF for PDF extraction
import chromadb
from sentence_transformers import SentenceTransformer
import ollama
import os

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
DB_PATH = "./resume_db"
client = chromadb.PersistentClient(path=DB_PATH)
collection = client.get_or_create_collection("resumes")


def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = "\n".join([page.get_text() for page in doc])
    return text


def add_resume_to_db(pdf_path):
    """Extracts text, generates embeddings, and stores in ChromaDB."""
    text = extract_text_from_pdf(pdf_path)
    embedding = embedding_model.encode(text).tolist()
    
    # Use filename as the unique ID
    resume_id = os.path.basename(pdf_path).split('.')[0]
    collection.add(ids=[resume_id], documents=[text], embeddings=[embedding])
    
    return f"Resume '{resume_id}' added to the database."


def search_resume(query):
    """Performs semantic search on resumes."""
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)
    
    if results["documents"]:
        return results["documents"][0]
    return "No matching resume found."


def chat_with_rag(query):
    """Retrieves relevant resume info and generates AI response."""
    context = search_resume(query)
    prompt = f"Use the following resume data to answer the query:\n\n{context}\n\nQuery: {query}"
    
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response['message']
