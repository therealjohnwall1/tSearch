import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.analysis import StemmingAnalyzer
from whoosh.index import open_dir
import os.path
import os
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(10000)

def makeWriter():
    if not os.path.exists("../indexer/theINDEX"):
        stem_ana= StemmingAnalyzer()
        os.makedirs("../indexer/theINDEX", exist_ok=True)
        schema = Schema(title=TEXT(stored=True),
                        headers=TEXT(sortable = True),
                        content = TEXT(analyzer = stem_ana, sortable = True),
                        url = TEXT(stored = True))
        
        ix = create_in("../indexer/theINDEX", schema)
    else:
        ix = open_dir("../indexer/theINDEX")
    return ix.writer()

class rSpider(CrawlSpider):
    name = "rSpider"
    DEPTH_LIMIT = 5
    with open("crawler/util/top-1000-websites.txt", "r") as links:
        urls = [site.strip() for site in links.readlines()]

    
    
    def start_requests(self): 
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    rules = (
        Rule(callback = "parse_item"),
    )

    def parse_item(self,response):
        writer = makeWriter()
        site = BeautifulSoup(response.body, 'lxml')
        title_tag = site.title
        title = title_tag.string if title_tag and title_tag.string else b''

        # Extract body
        body_tags = site.find_all('p')
        body = ''.join(tag.text for tag in body_tags)

        # Extract headers
        header_tags = site.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        headers = ''.join(tag.text for tag in header_tags)
        url = response.url
        try:
            writer.add_document(title=title, content=body, headers =headers, url = url)
            writer.commit()
        except Exception as e:
            print("\n"*5 + "*"*50)
            print(e)
            print("*"*50 + "\n"*5)

        link_extractor = LinkExtractor(allow=())
        for link in link_extractor.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_item)

        

        # fileName = response.url.split("/")[-2] + '.html'
        # route = "../indexer/storage/" + fileName
        # Path(route).write_bytes(response.body)






