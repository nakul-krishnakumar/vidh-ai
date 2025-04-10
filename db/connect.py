import os
from pinecone import Pinecone
from dotenv import load_dotenv

load_dotenv()

def connect_to_pinecone(PINECONE_API_KEY: str) -> tuple[Pinecone, str]:    

    if not PINECONE_API_KEY: # if key does not exist in env
        err = "Unauthorised pinecone connection attempt!"
        print(err)
        return None, err
    
    else:
        try:
            pc: Pinecone = Pinecone(api_key=PINECONE_API_KEY)
            print("Successfully connected to pinecone database!")
            # print(pc)
            return pc, None

        except Exception as e: # if invalid key or invalid connection 
            print(e)
            return None, str(e)  

