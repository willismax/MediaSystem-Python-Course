#@title 以 Selenium 搜尋 PTT 指定列表

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

options = Options()
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome(options=options)
url ='https://www.ptt.cc/bbs/movie/index.html'
wd.get(url)

elem = wd.find_element(By.CLASS_NAME,"title")
print(elem.text)

#beautifulsoup解析
soup = BeautifulSoup(wd.page_source,"html.parser")
links = soup.select('div.title > a')

# title = [ link.get_text() for link in links if '板規' not in link.get_text()]
# href = [ f'https://www.ptt.cc{link.get("href")}' for link in links ]

res = [
    {'title': link.get_text(),
     'href': f'https://www.ptt.cc{link.get("href")}'
     } for link in links if '公告' not in link.get_text() ]


print(res)
wd.close()