from fastapi import FastAPI
from utils import save_files_to_bucket, fetch_latest_BNS
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
app = FastAPI()

# base url
@app.get("/")
async def index():
   return {"message": "Hello World!"}

# have set a cronjob to hit this api endpoint once every year
@app.get("/trigger-fetch")
async def fetch():
   URL = os.getenv("MHA_BNS_PAGE_URL")
   fetch_latest_BNS(URL) # fetches & downloads to temp folder
   save_files_to_bucket() # saves to bucket & delete the files

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 8000))
   uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)