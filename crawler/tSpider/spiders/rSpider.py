import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path

class rSpider(CrawlSpider):
    #set crawler depth to 10
    name = "rSpider"
    # DEPTH_LIMIT = 10
    
    sites = open("util/prat.txt", "r")
    urls = sites.readlines()
    
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse_item)

    rules = (
        Rule(callback = "parse_item"),
    )

    def parse_item(self,response):
        link_extractor = LinkExtractor(allow=())
        for link in link_extractor.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_item)

        fileName = response.url.split("/")[-2] + '.html'
        route = "../indexer/storage/" + fileName
        Path(route).write_bytes(response.body)

        