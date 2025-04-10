from pinecone import Pinecone, ServerlessSpec
import time

def initialize_vector_store(pc: Pinecone, index_name: str) -> Pinecone.Index:

   existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]

   if index_name not in existing_indexes: # if index does not exist, create new index
      pc.create_index(
         name=index_name,
         dimension=1536,
         metric="cosine",
         spec=ServerlessSpec(cloud="aws", region="us-east-1"),
      )
      while True:
         status = pc.describe_index(index_name).status
         if status['ready']:
            break
         time.sleep(1)

   index = pc.Index(index_name) 
   return index