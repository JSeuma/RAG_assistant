from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.vectorstores import Chroma
import chromadb
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()


def retrieval(question):
    """
    Function that creates the mebedding for all the documents and save it in the vectorstore "faiss_index".
        
    The argumants are:

    question:
        Question we need the assistant answers

    It uses OpenAI model, so it will need to define the OpenAI_key.
    
    """
    # RAG prompt from langchain-hub
    from langchain import hub
    prompt = hub.pull("rlm/rag-prompt")

    # Model used for embeding and answer generation
    embedding=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.2, api_key=os.getenv("OPENAI_API_KEY"))

    # Load the previously created Chroma index from the "chroma_db" directory
    vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

    # RetrievalQA
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=vectorstore.as_retriever(),
        chain_type_kwargs={"prompt": prompt}
    )

    result = qa_chain.invoke({"query": question})
    result["result"]