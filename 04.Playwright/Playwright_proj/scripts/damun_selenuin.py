from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import sys
import time
import hashlib


def anonymize_username(username):
    return hashlib.sha256(username.encode()).hexdigest()


def run(sn) -> None:
    # Setup webdriver
    webdriver_service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=webdriver_service, options=options)

    # Navigate to the page
    driver.get(f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}")
    time.sleep(5)

    # Take screenshot
    driver.save_screenshot(f'../figures/ani_{sn}.jpg')

    # use Beautiful to get damun
    soup = BeautifulSoup(driver.page_source, 'lxml')

    # List comprehension to get the required data
    res = [{
        'userid': anonymize_username(li.select_one('.name > span').text.strip()),
        'text': li.select_one('.sub_content').text.strip(),
        'msg_time': li.select_one('b').text.strip()
    } for li in soup.select('.sub-list-li')]

    print(res)

    # write JSON data to a file
    with open(f'../data/raw/damun_{sn}.json', 'w') as f:
        json.dump(res, f)

    # Clean up
    driver.quit()

    return res


run(sys.argv[1])
