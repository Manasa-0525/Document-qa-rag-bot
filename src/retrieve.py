from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

CHROMA_PATH = "chroma_db"


def retrieve_documents(query, k=3):

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_model
    )

    results = db.similarity_search_with_score(query, k=k)

    filtered_results = []

    for doc, score in results:

        # lower score = better match
        if score < 1.2:
            filtered_results.append(doc)

    return filtered_results


if __name__ == "__main__":

    query = "What is Artificial Intelligence?"

    results = retrieve_documents(query)

    print("\nTop Retrieved Chunks:\n")

    for i, doc in enumerate(results, 1):

        print(f"\nResult {i}:\n")

        print(doc.page_content[:500])

        print("\nSource:", doc.metadata)