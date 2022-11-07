import sys
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup



def run(playwright: Playwright, sn) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto(f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}")
    time.sleep(5)
    page.screenshot(path='ani.jpg', full_page = True)
    soup = BeautifulSoup(page.content(), 'lxml')
    k={}
    for li in soup.select('.sub-list-li'):
        # userid = li.select('.name > span').text.strip()
        k['userid'] = li.select_one('.name > span').text.strip()
        k['text'] = li.select_one('.sub_content').text.strip()
        k['msg_time'] = li.select_one('b').text.strip()
        print(k)

    page.close()

    # ---------------------
    context.close()
    browser.close()
    return k


with sync_playwright() as playwright:
    run(playwright, sys.argv[1])
