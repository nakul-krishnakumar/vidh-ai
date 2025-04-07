from supabase import create_client, Client, SupabaseException
from dotenv import load_dotenv
import os
load_dotenv()

def connect_to_supabase(url: str, key: str) -> Client:
   try:
      supabase: Client = create_client(url, key)
      return supabase
   
   except SupabaseException as e:
      print(f"Could not connect to supabase storage!\n")
