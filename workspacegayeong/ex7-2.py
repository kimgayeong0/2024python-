import requests
from bs4 import BeautifulSoup
url="https://time.navyism.com/?host="
response=requests.get(url)
soup=BeautifulSoup(response.text,'onclick')
result=soup.find("time area",href=f"/eonyang-h/M01030601/list?ymd=")
print(result.text)