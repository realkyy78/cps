import requests 
import csv
from bs4 import BeautifulSoup

req=requests.get("https://search.naver.com/search.naver?where=post&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
html=req.text
soup = BeautifulSoup(html,'html.parser')

title = soup.find_all(class_='sh_blog_title')


sitetitle=[]
address=[]

for j in title:
    sitetitle.append(j.attrs['title'])
    address.append(j.attrs['href'])

print(sitetitle)
print(address)


file = open("naver.csv","w",newline="")

wr = csv.writer(file)
for i in range(len(address)) :
    wr.writerow([str(i+1), sitetitle[i],address[i]])
file.close