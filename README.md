# RAG ASSISTANT RETO

This folder contains the results of the "RETO" performed by Jaime Seuma on 24th-25th April 2024

The content is divided in 2 parts:
- Scripts
- Notebooks

EXECUTE
- Important: the model for embedding and answer generation are OpenAI. Create a .env file containing the `OPENAI_API_KEY`
- To install the required libraries run the command: `pip install -r requirements`
- To execute the application from stremlit (still not working, need some adjustments):

`streamlit run app.py`

## SCRIPTS:

- `retrieval.py`: Contains the function to execute the RAG assistant

- `app.py`: Contains the code to launch the application of RAG chat-assistant with the library Streamlit

- `utils.py`: Contains the function to digest the PDF documents, embed and save them in a vectorstore named `chroma_db`, using the library Chroma.

## NOTEBOOKS (in folder notebooks):


**notebooks\notebook_working.ipynb**
### RAG assintant notebook

Notebook consisting in two parts:
- Generation of the vectorstore from the 4 PDF documents provided.
- Model to inference the answer from a question using RAG retrieving from the vectorstore generated

The model used for the embeddings and the text generation are from OpenAI.
And the library using for generate the embeddings and the vectorstore is Chroma.

--------------------------------------------

**notebooks\notebook_test_prompt.ipynb**
### Testing Prompt

This notebook is for testing and improvement the system prompt for a better performance of the RAG assitant.
It is used the vectorstore previously generated.

Some strategies are:
- Mentioning to perform calculations with the retrieved information to answer the answer more accurately in the prompt.
- Another strategy would be Few-shots prompting, including some examples of question-answer in the prompt to guide the model to prepare the answers.
- A final strategy not tested would be Chain-of-Thougts, guiding the model in the process of preparing the answer.

--------------------------------------------

**`notebooks\notebook_test_faiss.ipynb**
### RAG assitant with FAISS

Notebook consisting in several parts:
- Function that receives a document and a question and provides an answer. IT IS WORKING
- Separate the function in 2 parts:
    - Generation of the vectorstore from the 4 PDF documents provided.
    - Model to inference the answer from a question using RAG retrieving from the vectorstore generated

The model used for the embeddings and the text generation are from OpenAI.
And the library using for generate the embeddings and the vectorstore is FAISS.