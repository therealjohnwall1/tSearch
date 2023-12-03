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

def makeWriter():
    if not os.path.exists("../indexer/theINDEX"):
        stem_ana= StemmingAnalyzer()
        os.mkdir("../indexer/theINDEX")
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
    with open("util/prat.txt", "r") as links:
        urls = [site.strip() for site in links.readlines()]

    
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    rules = (
        Rule(callback = "parse_item"),
    )

    def parse_item(self,response):
        site = BeautifulSoup(response.body, 'lxml')
        writer = makeWriter()
        title = site.title.string
        bod = site.find_all('p')
        body = ""
        for i in bod:
            body += i.text
        head = site.find_all(['h1','h2','h3','h4','h5','h6'])
        headers = ""
        for i in head:
            headers += i.text


        writer.add_document(title=title, content=body, headers =headers, url = response.url)
        writer.commit()
        
        link_extractor = LinkExtractor(allow=())
        for link in link_extractor.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_item)
        

        # fileName = response.url.split("/")[-2] + '.html'
        # route = "../indexer/storage/" + fileName
        # Path(route).write_bytes(response.body)






