from langchain_openai import AzureOpenAIEmbeddings
from langchain_pinecone import Pinecone as LangchainPinecone
from langchain.schema import Document
from db import connect_to_pinecone
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
EMBEDDING_MODEL_ENDPOINT = os.getenv("EMBEDDING_MODEL_ENDPOINT")

embedding_model = AzureOpenAIEmbeddings(
   model="text-embedding-3-small",
   azure_deployment="text-embedding-3-small",
   api_key=OPENAI_API_KEY,
   azure_endpoint=EMBEDDING_MODEL_ENDPOINT
   )

def search_pinecone(query: str, index_name: str, namespace: str, k: int) -> tuple[list[Document] | None, str | None]:
    pc, err = connect_to_pinecone(os.getenv("PINECONE_API_KEY"))
    if err:
        raise Exception(err)
    try:
        vectorstore = LangchainPinecone.from_existing_index(
            index_name=index_name,
            embedding=embedding_model,
            namespace=namespace
        )
        print("Fetched vectorstore")
        docs: list[Document] = vectorstore.similarity_search(query, k)
        return docs, None
    except Exception as err:
        print(f"Could not perform similarity search: {err}")
        return None, str(err)  # Convert exception to string
