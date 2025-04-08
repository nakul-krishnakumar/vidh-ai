from fastapi import APIRouter, Request

router = APIRouter()

@router.post('/query')
async def read_query(req: Request):
   try:   
      data = await req.json()
      query = data.get("query", "")
      print(query)
      return {"response": "Hey this is a message from backend!"}
   except:
      return {"response": "Did not get the query"}