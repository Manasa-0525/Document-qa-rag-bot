from langchain_community.document_loaders import PyPDFLoader
import os

DATA_PATH = "data"

def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(DATA_PATH, file)

            loader = PyPDFLoader(pdf_path)
            docs = loader.load()

            documents.extend(docs)

    return documents


if __name__ == "__main__":
    docs = load_documents()

    print(f"Loaded {len(docs)} pages")

    print("\nFirst page preview:\n")
    print(docs[0].page_content[:500])