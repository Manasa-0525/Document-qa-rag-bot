from src.retrieve import retrieve_documents


def generate_answer(query):

    results = retrieve_documents(query)

    if not results:

        return f"""
========================================

QUESTION:
{query}

========================================

ANSWER:

Sorry, the answer to this question was not found in the uploaded documents.

The system only answers from retrieved document context and does not generate answers from external knowledge.

========================================
"""

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    sources = []

    for doc in results:

        source = doc.metadata.get("source", "Unknown")
        page = doc.metadata.get("page", "N/A")

        sources.append(f"{source} (Page {page})")

    answer = f"""
========================================

QUESTION:
{query}

========================================

ANSWER:

Based on the retrieved documents, here is the relevant information:

{context[:1500]}

========================================

SOURCES:

{chr(10).join(sources)}

========================================
"""

    return answer


if __name__ == "__main__":

    query = input("Enter your question: ")

    response = generate_answer(query)

    print("\nANSWER:\n")

    print(response)