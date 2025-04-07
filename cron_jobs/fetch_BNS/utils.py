from bs4 import BeautifulSoup
import requests
import urllib.request
from dotenv import load_dotenv
import os
load_dotenv()

def fetch_latest_BNS(URL: str):
   try:
      res: requests.Response = requests.get(url=URL)

      soup = BeautifulSoup(res.content, 'html.parser') # get the entire html 
   
      # print(soup)
      container = soup.find_all(class_="file") # filter by class_name
      print(container)

      count = 1
      for link in container:
         a = link.find('a')
         href = a.get('href')
         print(href)

         download_url = os.getenv("MHA_BASE_URL") + str(href)
         urllib.request.urlretrieve(download_url, f"temp/file_{count}.pdf")
         count += 1

   except requests.RequestException as e:
      print(f"An error occured while fetching the file! \n{e}")