from langchain_pinecone import Pinecone as LangchainPinecone
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from db import initialize_vector_store

# split data into batches, due to upsert size limit
def batch_documents(docs: list[Document], batch_size: int):
   for i in range(0, len(docs), batch_size):
      yield docs[i:i + batch_size]

async def embed_and_store(chunks: list[Document], namespace: str, index_name: str, pc: LangchainPinecone) -> tuple[LangchainPinecone, str]:

   index = initialize_vector_store(pc=pc, index_name=index_name) # setup new index or use existing db index
   index_stats = index.describe_index_stats()
   # print(index_stats)

   existing_namespaces = index_stats.namespaces.keys()

   if namespace in existing_namespaces: # if exists, delete it for updating with latest version
      print(f"Namespace '{namespace}' exists. Deleting it first...")
      index.delete(delete_all=True, namespace=namespace)
   else:
      print(f"Namespace '{namespace}' does not exist. Safe to push.")

   try:
      # embedding model
      embedding = OpenAIEmbeddings(model="text-embedding-3-small")

      total_uploaded = 0 # keeping count of num of batches uploaded

      for batch in batch_documents(chunks, 1000):
         # generate embeddings from chunks and upserts it to pinecone
         LangchainPinecone.from_documents(
            documents=batch,
            embedding=embedding,
            index_name=index_name,
            namespace=namespace
         )

         total_uploaded += len(batch)
         print(f"Uploaded {total_uploaded}) chunks in total")

      print(f"Uploaded {len(chunks)} chunks to namespace '{namespace}'")
      return None, None
   
   except Exception as e:
      print(f"Could not embed & upload to pinecone \ne: {e}")
      return None, e
