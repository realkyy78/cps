from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import time

path = os.getcwd()+"chromedriver"
path = 'C:\\Users\김윤영\Desktop\cps_live\chromedriver.exe'

driver = webdriver.Chrome(path)
title=[]
price=[]

try:
    driver.get("https://www.coupang.com/")
    time.sleep(1) 

    searchIndex = "로션"
    element = driver.find_element_by_id("headerSearchKeyword") #id로 검색창 엘레먼트 찾기
    element.send_keys(searchIndex)
    driver.find_element_by_id("headerSearchBtn").click() #검색창 버튼 엘레먼트

    html = driver.page_source # html 파일에 넣기
    bs = BeautifulSoup(html,"html.parser")

    for i in range(10): # 결과가 너무 많아서 10 페이지만 추출
        time.sleep(1)
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser")

        conts = bs.find_all("dl",class_ ="search-product-wrap")
        for c in conts : # 컨텐츠
            title.append(c.find("div",class_="name").text)
            price.append(c.find("div", class_="price").find("strong",class_="price-value").text)
        driver.find_element_by_xpath('//*[@id="searchOptionForm"]/div[2]/div[2]/div[4]/a[2]').click()
finally :
    for t in title:
        print(t)
    for t in price:
        print(t)
driver.quit()   