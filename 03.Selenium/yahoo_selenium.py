#@title Yahoo搜尋 "霍華德"
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') # 無頭模式
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

wd = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
url='https://tw.yahoo.com/'
wd.get(url)

# 操作網頁元素
element = wd.find_element(By.ID, 'header-search-input')
key_word = '霍華德'
element.send_keys(key_word)
wd.find_element(By.ID, 'header-desktop-search-button').click()

# 等待目標表格'id 為 web'的div出現
WebDriverWait(wd, 5).until(
    expected_conditions.presence_of_element_located((By.ID, 'web')))

#然後就是beautifulsoup的範疇了，將目前頁面用bs4解析
soup = BeautifulSoup(wd.page_source,"html.parser")
links = soup.select('div#web h3')

for link in links:
    print(link.get_text())

wd.quit()