from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingest import load_documents


def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


if __name__ == "__main__":
    docs = load_documents()

    chunks = chunk_documents(docs)

    print(f"Total chunks created: {len(chunks)}")

    print("\nFirst chunk preview:\n")
    print(chunks[0].page_content)