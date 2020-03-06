# coding:utf-8

import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def GetHTMLText(link_text):
    html_data = requests.get(link_text)
    try:
        return html_data.text
    except RequestException:
        return None

def FormatText(link_text, html_text):
    if 'weixin' in link_text:
        soup = BeautifulSoup(html_text)
        title = soup.h2.string.strip()
        text = "%s\n\n[WeChat](%s)" % (title, link_text)
        print(text)
        return text
    elif 'bilibili' in link_text:
        soup = BeautifulSoup(html_text)
        title = soup.title.string.strip()
        title = title.replace('_','')
        text = "%s\n\n[Bilibili](%s)" % (title, link_text)
        print(text)
        return text
    return None

def HTML2TelegramText(link_text):
    html_text = GetHTMLText(link_text)
    if html_text == None:
        return None
    text = FormatText(link_text, html_text)
    return text
