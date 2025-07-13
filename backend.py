from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA

def load_and_index_doc(file_path):
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore, chunks

def get_summary(chunks):
    llm = ChatOpenAI(temperature=0)
    text = ' '.join([chunk.page_content for chunk in chunks[:3]])
    prompt = f"Summarize this text in ≤150 words:\n{text}"
    summary = llm.predict(prompt)
    return summary

def answer_question(vectorstore, question):
    retriever = vectorstore.as_retriever(search_kwargs={"k":3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(temperature=0),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    result = qa_chain({"query": question})
    answer = result['result']
    snippet = result['source_documents'][0].page_content[:200]
    return answer, snippet

def generate_challenge_questions(chunks):
    llm = ChatOpenAI(temperature=0)
    text = ' '.join([chunk.page_content for chunk in chunks[:5]])
    prompt = f"Create 3 logical or comprehension-focused questions from this text:\n{text}"
    questions = llm.predict(prompt)
    return questions.strip().split('\n')
