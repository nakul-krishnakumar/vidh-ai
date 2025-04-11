from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain.schema import Document
from db import connect_to_pinecone
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

def search_pinecone(query: str, index_name: str, namespace: str, k: int) -> tuple[list[Document], str]:

   pc, err = connect_to_pinecone(os.getenv("PINECONE_API_KEY"))
   if err:
      raise Exception(err)
   
   try:
      # connecting to the existing indexw
      vectorstore = LangchainPinecone.from_existing_index(
         index_name=index_name,
         embedding=embedding_model,
         namespace=namespace
      )

      print("Fetched vectorstore")
      
      docs: list[Document] = vectorstore.similarity_search(query, k)
      return docs, None

   except Exception as err:
      print(f"Could not perform similarity search")
      return None, err
