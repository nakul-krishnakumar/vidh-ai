from utils import fetch_latest_BNS, chunk_file_data, embed_and_store
from db import connect_to_pinecone
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

# handler func for GET: /api/trigger-fetch
def run_fetch_pipeline():
   URL = os.getenv("MHA_BNS_PAGE_URL")
   file_datas, err = fetch_latest_BNS(URL)

   if err:
      print(f"Error fetching PDFs: {err}")
      return

   namespace = os.getenv("PINECONE_NAMESPACE")
   index_name = os.getenv("PINECONE_INDEX_NAME")
   PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

   pc, err = connect_to_pinecone(PINECONE_API_KEY)
   if err:
      print(f"Error connecting to Pinecone: {err}")
      return

   chunks = chunk_file_data(file_datas=file_datas)
   _, err = asyncio.run(embed_and_store(
      chunks=chunks,
      namespace=namespace,
      index_name=index_name,
      pc=pc
   ))

   if err:
      print(f"Error uploading to Pinecone: {err}")
   else:
      print("Upload successful!")