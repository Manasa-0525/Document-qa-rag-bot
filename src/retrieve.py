from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"


def retrieve_documents(query, k=3):

    # Real embedding model
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load vector database
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    # Similarity search
    results = db.similarity_search(query, k=k)

    return results


if __name__ == "__main__":

    query = input("Enter your question: ")

    results = retrieve_documents(query)

    print("\nTop Retrieved Chunks:\n")

    for i, doc in enumerate(results, 1):

        print(f"\n========== Result {i} ==========\n")

        print(doc.page_content[:700])

        print("\nSource:")
        print(f"File: {doc.metadata.get('source')}")
        print(f"Page: {doc.metadata.get('page')}")