from selenium import webdriver
from bs4 import BeautifulSoup
import time
from adapt import Insert


driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://sports.news.naver.com/index.nhn')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
news = soup.select('div.text_area > strong.title')
for n in news:
    print(n.text.strip())


Insert(news)


    