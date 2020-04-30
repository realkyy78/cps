from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd()+"chromedriver"
path = 'C:\\Users\김윤영\Desktop\cps_live\chromedriver.exe'

driver = webdriver.Chrome(path)

try:
    driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1")
    time.sleep(1) # 드라이버로딩시간
    html = driver.page_source
    bs = BeautifulSoup(html,"html.parser")
    pages = bs.find("div", class_ = "pagination").find_all("a")[-1]["href"].split("page")[1]
        # 리스트 인덱스는 0부터 시작
    pages = int(pages)
    
    title=[]
    for i in range(pages) : #int값을 스트링으로 바꿈 page에 페이지 번쨰수 넣으면됨
        driver.get("https://www.cau.ac.kr/cms/FR_CON/index.do?MENU_ID=100#page1"+ str(i+1)) # 페이지 인덱스에 1더함
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("div",class_ = "txtL")
        title.append("page" + str(i + 1))
        for c in conts : # 컨텐츠
            title.append(c.find("a").text) # a 태그의 값 가져옴
finally:
    for t in title :
        if t.find("page") : 
            print()
            print(t)
        else : 
            print(t) # 페이지가 업는 경우, 값이 들어간경우

    time.sleep(3)
    driver.quit