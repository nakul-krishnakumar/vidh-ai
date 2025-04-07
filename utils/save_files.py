from supabase_utils import connect_to_supabase
from dotenv import load_dotenv
import os
load_dotenv()

def save_files_to_bucket():
   url = os.getenv("SUPABASE_URL")
   key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
   supabase = connect_to_supabase(url=url, key=key)

   bucket = os.getenv("BUCKET_NAME")
   try:
      if (len(os.listdir("./temp")) == 0):
         print("Files do not exist!")
      
      else:
         for file in os.listdir("./temp"):

            file_path = os.path.join("./temp", file)
            print(f"Uploading {file_path}")
            
            with open(file_path, "rb") as f:
               response = supabase.storage.from_(bucket).upload(
                     file,  
                     f,
                     {"upsert": "true"}
               )
               print(response)
            
            os.remove(file_path)

   except FileNotFoundError as e:
      print("File not found!\n")


      