from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import uvicorn
import os

from routes import api, chat

load_dotenv()
app = FastAPI()

# middlewares
app.add_middleware(CORSMiddleware)

# sub route /api
app.include_router(api.router, prefix='/api')
app.include_router(chat.router, prefix='/chat')

# base url
@app.get("/")
async def index():
   return {"message": "Hello World!"}

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8000))
   uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

