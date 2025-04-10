from bs4 import BeautifulSoup
from dotenv import load_dotenv
from io import BytesIO
import requests
import time
import os

load_dotenv()

def fetch_latest_BNS(URL: str) -> tuple[list[BytesIO], str]:
   try:
      res: requests.Response = requests.get(url=URL)
      
      soup = BeautifulSoup(res.content, 'html.parser') # get the entire html 
   
      # print(soup)
      containers = soup.find_all(class_="file") # filter by class_name
      print(containers)

      file_datas: list[BytesIO] = []
      for link in containers:
         a = link.find('a')
         href = a.get('href')
         print(href)

         download_url = os.getenv("MHA_BASE_URL") + str(href) # get the pdf url

         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36"}

         file_res: requests.Response = requests.get(download_url, headers=headers, timeout=10) 
         if file_res.status_code == 200:
            file_data = BytesIO(file_res.content) # converting raw content to binary stream
            file_datas.append(file_data)
         else:
            err = f"Could not fetch {download_url}, status-code: {file_res.status_code}"
            print(err)
            return [], err
         
         time.sleep(1)

      return file_datas, None

   except requests.RequestException as e:
      print(f"An error occured while fetching the file! \n{e}")
      return [], str(e)
