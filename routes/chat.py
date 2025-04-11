from fastapi import APIRouter, Request
from model import generate_answer_from_context 
from utils import search_pinecone
from dotenv import load_dotenv
import os

load_dotenv()
router = APIRouter()

# sub route: /chat/query
@router.post('/query')
async def read_query(req: Request):
   try:   
      data = await req.json()
      query = data.get("query", "")
      print(query)

      index_name = os.getenv("PINECONE_INDEX_NAME")
      namespace = os.getenv("PINECONE_NAMESPACE")

      matched_docs = search_pinecone(query=query, index_name=index_name, namespace=namespace, k=7)
      response = generate_answer_from_context(context=matched_docs, query=query)

      print(response)
      return { "response": response }
   
   except Exception as e:
      return {"response": f"Did not get the query \nerror: {e}"}