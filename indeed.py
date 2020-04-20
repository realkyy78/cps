import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.naver.com/movie/running/current.nhn")
if req.status_code !=200 :
    print("failed",req.status_code) 

html = req.text
bs = BeautifulSoup(html, "html.parser")

box = bs.find_all("dl", class_="lst_dsc")

ratio=[]
title=[]

for b in box :
    ratio.append(b.find("div",class_="star_t1").find("span",class_="num").text)
    title.append (b.find("dt", class_="tit").find("a").text)

movieInfo=[]
for i in range(len(box)) :
    movie=[]
    movie.append(title[i])
    movie.append(ratio[i])
    movieInfo.append(movie) 

for i in movieInfo:
    print(i)
