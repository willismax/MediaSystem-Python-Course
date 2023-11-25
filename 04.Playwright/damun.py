from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup
import json
import sys
import time



def run(playwright: Playwright, sn) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()

    page.goto(f"https://ani.gamer.com.tw/animeVideo.php?sn={sn}")
    time.sleep(5)

    # screenshot
    page.screenshot(path='ani.jpg', full_page = True)
    
    # use Beautiful to get damun
    soup = BeautifulSoup(page.content(), 'html.parser')


    # for-loops
    # res = []
    # k = {}
    # for li in soup.select('.sub-list-li'):
    #     k['userid'] = li.select_one('.name > span').text.strip()
    #     k['text'] = li.select_one('.sub_content').text.strip()
    #     k['msg_time'] = li.select_one('b').text.strip()
    #     print(k)
    #     res.append(k)
    
    # 列表推導式
    res = [ {
        'userid': li.select_one('.name > span').text.strip(),
        'text' : li.select_one('.sub_content').text.strip(),
        'msg_time' : li.select_one('b').text.strip()
    } for li in soup.select('.sub-list-li')]

    print(res)

    
    # write JSON data to a file
    with open(f'damun_{sn}.json', 'w') as f:
        json.dump(res, f)

    page.close()

    # ---------------------
    context.close()
    browser.close()
    return res


with sync_playwright() as playwright:
    run(playwright, sys.argv[1])