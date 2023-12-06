import requests 
from bs4 import BeautifulSoup
from whoosh.fields import *
from scrapy.http import HtmlResponse
import os.path
import os
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import create_in, open_dir
from pathlib import Path
import sys
sys.setrecursionlimit(10000)

path = "../indexer/theINDEX"

def makeWriter():
    if not os.path.exists(path):
        stem_ana= StemmingAnalyzer()
        os.makedirs(path, exist_ok=True)
        schema = Schema(title=TEXT(stored=True),
                        headers=TEXT(sortable = True),
                        content = TEXT(analyzer = stem_ana, sortable = True),
                        url = TEXT(stored = True))
        ix = create_in(path, schema)
    else:
        ix = open_dir(path)
    return ix.writer()

def parse_item(response,writer):

        site = BeautifulSoup(response.body, 'lxml')

        print(type(site.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])))
        title_tag = site.title
        title = title_tag.string if title_tag and title_tag.string else b''

        # Extract body
        body_tags = site.find_all('p')
        body = ''.join(tag.text for tag in body_tags)

        # Extract headers
        header_tags = site.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        headers = ''.join(tag.text for tag in header_tags)
        url = response.url
        fileName = response.url.split("/")[-2] + '.html'
        route = "testIndex/" + fileName
        Path(route).write_bytes(response.body)

        print(type(body))
        print(type(headers))
        print(type(url))

        print(body)
        print(headers)
        print(url)

        try:
            writer.add_document(title=title, content=body, headers =headers, url = url)
            writer.commit()
        except Exception as e:
            print("\n"*5 + "*"*50)
            print(e)
            print("*"*50 + "\n"*5)

#**************************************************************
r = requests.get("https://books.toscrape.com/")
res = HtmlResponse(url=r.url, body=r.content, encoding = 'utf-8')


writer = makeWriter()
parse_item(res,writer)


#**************************************************************
