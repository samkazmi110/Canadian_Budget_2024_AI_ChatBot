import os
import textwrap
from langchain_astradb import AstraDBVectorStore
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Define a global variable to hold the OpenAI instance
llm = None
embedding = None
vstore = None
astra_vector_index = None


astra_db_token=os.getenv("astra_db_token")
astra_db_api_endpoint=os.getenv("astra_db_api_endpoint")
astra_db_namespace=os.getenv("astra_db_namespace")
astra_db_collection_name=os.getenv("astra_db_collection_name")

# Define a function to get the answer from the budget database
def get_answer_from_budget(question):
    global astra_vector_index
    astra_vector_index = VectorStoreIndexWrapper(vectorstore=vstore)
    response = astra_vector_index.query(question, llm=llm)
    return response

# Define a function to initialize the OpenAI instance and Vector Database
def Initialize_llm_and_vector_db(openapi_key):
    global llm, embedding, vstore
    llm = OpenAI( openai_api_key=openapi_key)
    embedding = OpenAIEmbeddings(openai_api_key=openapi_key)
    
    vstore = AstraDBVectorStore(
    embedding=embedding,
    namespace=astra_db_namespace,
    collection_name=astra_db_collection_name,
    token=astra_db_token,
    api_endpoint=astra_db_api_endpoint,
    )
    


    

