from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from src.chunking import chunk_documents
from src.ingest import load_documents

CHROMA_PATH = "chroma_db"


def create_vector_store():

    # Load documents
    documents = load_documents()

    # Chunk documents
    chunks = chunk_documents(documents)

    # Fake embedding model
    embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Create vector database
    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_PATH
    )

    db.persist()

    print("Vector database created successfully!")
    print(f"Total chunks stored: {len(chunks)}")


if __name__ == "__main__":
    create_vector_store()