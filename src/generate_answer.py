from retrieve import retrieve_documents


def generate_answer(query):

    # Retrieve relevant chunks
    results = retrieve_documents(query)

    # If no results found
    if not results:
        return "No relevant information found."

    # Build context
    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    # Build source citations
    sources = []

    for doc in results:

        source = doc.metadata.get("source", "Unknown File")
        page = doc.metadata.get("page", "N/A")

        citation = f"{source} (Page {page})"

        if citation not in sources:
            sources.append(citation)

    # Generate final formatted answer
    answer = f"""
==================================================
QUESTION:
{query}
==================================================

ANSWER:
Based on the retrieved documents, here is the relevant information:

{context[:1200]}

==================================================
SOURCES:
"""

    for src in sources:
        answer += f"\n- {src}"

    return answer


if __name__ == "__main__":

    query = input("Enter your question: ")

    response = generate_answer(query)

    print("\n")
    print(response)