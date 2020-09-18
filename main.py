from selenium import webdriver
from bs4 import BeautifulSoup
import time
from adapt import Insert


driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get('https://sports.news.naver.com/kbaseball/news/index.nhn?isphoto=N&type=team&team=SS&date=20200918')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
news = soup.select('#_newsList > ul > li > div > a > span')
for n in news:
    print(n.text.strip())
    Insert(n.text.strip())


