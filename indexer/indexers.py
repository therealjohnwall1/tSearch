from whoosh.index import create_in
from whoosh.fields import *
import os.path
import nltk
from bs4 import BeautifulSoup
import requests 
from scrapy.http import HtmlResponse

r = requests.get("https://marriott.com")
response = HtmlResponse(url=r.url, body=r.content, encoding = 'utf-8')
site = BeautifulSoup(response.body, 'lxml')

tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
h1 = site.find_all(tags)

# links = site.find_all('a', href=True)
# print(type(links))
#get title alone
#get paragraph in one paragraph
#get links in a list














# def html_indexer(response):
#     url = response.url
#     site = BeautifulSoup(response.body, 'html.parser')
#     # print(site.prettify())
#     x = site.find_all('p')
#     print(x)
#     print("*"* 10)
#     links = site.find_all('a')
#     print(links)




# html_index(res)
# def writer():
#     if not os.path.exists("indexdir"):
#         os.mkdir("indexdir")
#         schema = Schema(title=TEXT(stored=True),content=TEXT)
#         ix = create_in("indexdir", schema)
#     else:
#         ix = open_dir("indexdir")
        
#     return ix.writer()

