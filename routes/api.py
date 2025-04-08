from fastapi import APIRouter
from utils import save_files_to_bucket, fetch_latest_BNS
from dotenv import load_dotenv

import os

load_dotenv()
router = APIRouter()


# have set a cronjob to hit this api endpoint once every year
@router.get("/trigger-fetch") # api/trigger-fetch
async def fetch(): 
   URL = os.getenv("MHA_BNS_PAGE_URL")
   fetch_latest_BNS(URL) # fetches & downloads to temp folder
   save_files_to_bucket() # saves to bucket & delete the files

   return {"message": "Fetched and saved documents to bucket!"}

@router.get("/keep-alive")
async def keep_alive():
   return {"message": "Server is alive and running"}