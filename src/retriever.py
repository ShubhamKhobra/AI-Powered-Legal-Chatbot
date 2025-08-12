from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings


def get_retriever(path):
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5", encode_kwargs={"normalize_embeddings": True})
    vectorstore = FAISS.load_local(path, embeddings=embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    return retriever