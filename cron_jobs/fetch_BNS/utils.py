from bs4 import BeautifulSoup
import requests
import urllib.request

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

         download_url = "https://www.mha.gov.in/" + str(href)
         urllib.request.urlretrieve(download_url, f"saves/file_{count}.pdf")
         count += 1

   except requests.RequestException as e:
      print(f"An error occured while fetching the file! \n{e}")
      

if __name__ == '__main__':
   URL = "https://www.mha.gov.in/en/commoncontent/new-criminal-laws"
   fetch_latest_BNS(URL)