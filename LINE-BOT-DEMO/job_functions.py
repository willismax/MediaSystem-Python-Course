from googletrans import Translator
from bs4 import BeautifulSoup
import pandas as pd
import requests


def translate_text(text,dest='en'):
    """以google翻譯將text翻譯為dest語言
    param:
        text: 要翻譯的字串，接受UTF-8編碼。
        dest: 要翻譯的目標語言，參閱googletrans.LANGCODES語言列表。
    return:
        翻譯結果。
    """
    text = text.strip()
    translator = Translator()
    result = translator.translate(text, dest).text
    return result

def query_illegal_announcement(cmpqry):
    """違反勞動法令事業單位雇主查詢系統-公司查詢"""
    url = f'https://announcement.mol.gov.tw/cmpqry/{cmpqry}'
    r = requests.get(url)
    df = pd.read_html(r.text)[0]
    _ = df[df['處分日期']>'109/01/01']
    ill_cmp = _['事業單位名稱(負責人) / 自然人姓名'][0]
    ill_count = _['罰鍰金額'].count()
    ill_cumsum = _['罰鍰金額'].sum()
    return f"「{ill_cmp}」等公司自109年起計違反{ill_count}件，累計處罰金額{ill_cumsum/1000}千元。\n更多參見 {url} "


def search_jobbooks(jobs):
    """搜尋台灣就業通職務百科
    Args:
        jobs: 職務
    Return:
        list([
            'link':詳細內容
            'title':相關職務類別名稱
            'intro':簡介
        ])
    """
    jobs = jobs.strip()
    url = f'https://jobooks.taiwanjobs.gov.tw/InsideIndustrySearch.aspx?n=200&q={jobs}'
    r = requests.get(url)
    if '查無符合相關' in r.text:
        return f"查無「{jobs}」職務的資料。"
    soup = BeautifulSoup(r.text, "html.parser") 
    d = soup.select('#CCMS_Content > div > div > div > div > div > div > div > ul > li' )
    k = [i for i in d]
    res = [ 
        {
            'link': f"https://jobooks.taiwanjobs.gov.tw{i.div.div.div.div.a['href']}",
            'title': i.div.div.div.div.a['title'][7:],
            'intro': i.div.div.div.div.a.p.span.text.replace("\r\n","").replace("\xa0\xa0","")
            } for i in k ][0]
    return f"搜尋「{jobs}職務」共{len(res)}筆，參見{url}"