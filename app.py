import streamlit as st
import tempfile
import os

# Get API key from secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from backend import load_and_index_doc, get_summary, answer_question, generate_challenge_questions

st.set_page_config(page_title="📚 Smart Assistant")

st.title("📚 Smart Assistant for Research Summarization")

uploaded_file = st.file_uploader("Upload PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    st.info("Processing document...")
    vectorstore, chunks = load_and_index_doc(tmp_path)

    summary = get_summary(chunks)
    st.subheader("📄 Auto Summary (≤150 words)")
    st.write(summary)

    mode = st.radio("Choose mode:", ("Ask Anything", "Challenge Me"))

    if mode == "Ask Anything":
        question = st.text_input("Ask your question:")
        if question:
            answer, snippet = answer_question(vectorstore, question)
            st.markdown(f"**Answer:** {answer}")
            st.caption(f"🔍 Justification: {snippet} ...")
    else:
        if st.button("Generate Challenge Questions"):
            questions = generate_challenge_questions(chunks)
            for i, q in enumerate(questions, 1):
                st.markdown(f"**Q{i}:** {q}")
                user_ans = st.text_input(f"Your answer to Q{i}")
                if user_ans:
                    correct_ans, snippet = answer_question(vectorstore, q)
                    st.markdown(f"✅ **Suggested Answer:** {correct_ans}")
                    st.caption(f"🔍 Justification: {snippet} ...")
