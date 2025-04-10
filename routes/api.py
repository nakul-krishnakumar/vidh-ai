from fastapi import APIRouter
from controllers import run_fetch_pipeline
import threading

router = APIRouter()


# have set a cronjob to hit this api endpoint once every year
@router.get("/trigger-fetch") # api/trigger-fetch
async def fetch(): 
   thread = threading.Thread(target=run_fetch_pipeline)
   thread.start()
   return {"message": "Pipeline triggered, processing in background."}

@router.get("/keep-alive")
async def keep_alive():
   return {"message": "Server is alive and running"}