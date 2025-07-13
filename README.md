# 🧠 Smart Assistant for Research Summarization

An AI-powered assistant that helps you read and understand large documents like research papers, legal files, and technical manuals.
Upload PDF/TXT → get a summary, ask free-form questions, and test yourself in challenge mode – all grounded in the document content.

---

## ✨ **Features**
✅ Upload PDF/TXT files  
✅ Auto summary (≤ 150 words)  
✅ Ask Anything: free-form Q&A, answers with justification from document  
✅ Challenge Me: AI-generated logic/comprehension questions → user answers → AI evaluates & explains  
✅ Local web app with clean interface (Streamlit)

---

## ⚙ **Setup Instructions**

> ⚡ Before starting, make sure you have Python 3.8+ installed

1️⃣ Clone this repo (or download ZIP & unzip):
```bash
git clone https://github.com/yourusername/smart-assistant.git
cd smart-assistant
🏛 Architecture & Reasoning Flow
Frontend:
Streamlit → user uploads document & interacts with modes

Backend:
LangChain + OpenAI:

langchain_community.document_loaders: load PDF/TXT files

langchain.text_splitter: split text into manageable chunks

langchain_openai.OpenAIEmbeddings: create embeddings

langchain_community.vectorstores: FAISS for vector DB

langchain_openai.ChatOpenAI: answer questions & generate challenges

Reasoning Modes:

✅ Auto Summary: uses LLM to create ≤150 words summary

✅ Ask Anything: question → retrieves matching chunk → answers + shows snippet as justification

✅ Challenge Me: AI generates questions → user answers → AI checks & gives feedback with reference

All answers are grounded in the uploaded document to reduce hallucination.

📁 Project Structure
plaintext
Copy
Edit
smart-assistant/
├── app.py                  # Streamlit frontend
├── backend.py              # Core logic & AI reasoning
├── requirements.txt        # All Python dependencies
└── README.md               # Project documentation
