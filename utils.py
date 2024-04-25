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

def load_doc():
    
    """
    Function to extract text from pdf, create the embeddings of the documents and save them in the file "chroma_db".

    No arguments because the directories for all the pdf files are already inside the function.

    FOr a correct use, put "paths" as argument of the function and delete de variable with the same name from inside the function. 
    
    It uses OpenAI model, so it will need to define the OpenAI_key.

    """    
    # Embedding´s model
    embedding=OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

    paths = ["documentos/doc_2023_12_Posicionamiento_Environment.pdf", 
              "documentos/Ficha tecnica CI Environment ISR_240317.pdf", 
              "documentos/NORRCO004_V28_Catalogo de productos de activo vigentes.pdf", 
              "documentos/docu_ejemplo\Tarifas transferencias Extranjero.pdf",
             ]
    # Convert to list
    if isinstance(paths, str):
        paths = [paths] 

    # Loop to embed and add to vectorstore all the doocuments
    for pth in paths:
        loader = PyMuPDFLoader(pth)
        data = loader.load()

        # Split
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
        all_splits = text_splitter.split_documents(data)

        # Store splits
        embedding = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        vectorstore = Chroma.from_documents(documents=all_splits, embedding=embedding, persist_directory="./chroma_db")
        print(f"Vectorstore for {pth} created and stored.")
    return vectorstore