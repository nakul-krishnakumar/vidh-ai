from fastapi import FastAPI
from cron_jobs import fetch_latest_BNS
from utils import save_files_to_bucket
from dotenv import load_dotenv
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