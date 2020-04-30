from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd()+"chromedriver"
path = 'C:\\Users\김윤영\Desktop\cps_live\chromedriver.exe'

driver = webdriver.Chrome(path)

try :
    driver.get("http://www.kyobobook.co.kr/index.laf?OV_REFFER=https://www.google.com/")
    time.sleep(1) # 드라이버로딩시간

    searchIndex = "파이썬"
    element = driver.find_element_by_class_name("main_input") #class name으로 검색창 엘레먼트 찾기
    element.send_keys(searchIndex)
    driver.find_element_by_class_name("btn_search").click() #검색창 버튼 엘레먼트
    title=[]

    html = driver.page_source # html 파일에 넣기
    bs = BeautifulSoup(html,"html.parser")

    pages = int(bs.find("span", id = "totalpage").text)
    print(pages)
    for i in range(3) :
        html =driver.page_source
        bs = BeautifulSoup(html,"html.parser")

        conts = bs.find("div", class_="list_search_result").find_all("td", class_ = "detail") # 큰 네모
        
        for c in conts :  # 네모 안에 타이틀
            print(c.find("div", class_ = "title").find("strong").text)
finally :
    driver.quit()