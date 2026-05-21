import streamlit as st

from src.generate_answer import generate_answer


st.set_page_config(
    page_title="Document QA RAG Bot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Document QA RAG Bot")

st.markdown(
    "Ask questions from your uploaded PDF documents using Retrieval-Augmented Generation (RAG)."
)

query = st.text_input(
    "Enter your question:"
)

if st.button("Get Answer"):

    if query.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching documents and generating answer..."):

            response = generate_answer(query)

        st.success("Answer generated successfully!")

        st.markdown("## Answer")

        st.write(response)