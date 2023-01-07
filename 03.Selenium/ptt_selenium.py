#@title 以 Selenium 搜尋 PTT 指定列表

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import sys

sys.path.insert(0,'chromedriver')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 成為無頭模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
url ='https://www.ptt.cc/bbs/movie/index.html'
wd.get(url)

elem = wd.find_element(By.CLASS_NAME,"title")
# print(elem.text)

#beautifulsoup解析
soup = BeautifulSoup(wd.page_source,"html.parser")
links = soup.select('div.title > a')

# title = [ link.get_text() for link in links if '板規' not in link.get_text()]
# href = [ f'https://www.ptt.cc{link.get("href")}' for link in links ]

res = [{
    'title': link.get_text(),
    'href': f'https://www.ptt.cc{link.get("href")}'
} for link in links if '板規' not in link.get_text() ]

print(res)
wd.close()