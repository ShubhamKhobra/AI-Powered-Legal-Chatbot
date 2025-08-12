from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from src.retriever import get_retriever
import os
from dotenv import load_dotenv


def generator_response(query):

    # Setting the api key
    load_dotenv()
    os.environ.get("OPENAI_API_KEY")

    # Load the llm 
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    # Define prompt template
    template = """
    You are an assistant for question-answering tasks.
    Use the provided context only to answer the following question:
    Also provide the source paragraph from where the answer was derived.
    If you don't know the answer, say "Sorry, I have not been built to answer this question."

    <context>
    {context}
    </context>

    Question: {input}
    """

    # Create a prompt template
    prompt = ChatPromptTemplate.from_template(template)

    # Creating path for vectorstore
    root_directory = os.path.dirname(os.path.abspath(__file__))
    vectorstore_path = os.path.join(root_directory, '../vectordb/vectorstore.db')

    # Create a retriever
    retriever = get_retriever(vectorstore_path)

    # Create a chain 
    doc_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, doc_chain)

    # Get the streaming response
    response = chain.stream({"input": query})

    return response