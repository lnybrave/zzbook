# !/usr/bin/python
# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_html_text(url):
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text


def get_rank_list(url):
    html = get_html_text(url)

    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.find_all('div')
    for i in divs:
        print i


def main():
    rank_list_url = 'http://r.qidian.com/'
    get_rank_list(rank_list_url)


main()
