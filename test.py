from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import sys
import requests as rq

def main():

    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'

    session = HTMLSession()
    session.cookies.set('over18', '1')  # 向網站回答滿 18 歲了 !
    content = session.get(url)

    soup = bs(content.text, "lxml") #用lxml解析html結構
    contents = soup.select("div.title") #取得所有class為"title"的div tag
    
    for item in contents:
        link = item.find_next('a') # 往下找<a>內容
        if link:
            print(link.text)
            print(link.get('href'))

if __name__ == '__main__':
    main()