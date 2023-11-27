from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path
import random

class testSpider(CrawlSpider):
    #use crawlSpider, a subclass of spider that allows crawling
    name = "testSpider"
    allowed_domains = ["toscrape.com"]
    urls = ["http://books.toscrape.com/"]
    
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url, callback=self.parse)

    rules = ( #empty rules means all urls are visited
        Rule(callback='parse_item'),
    )

    def parse_item(self,response):
        fileName = response.url.split("/")[-2] + '.html'
        route = "../util/storage/" + fileName
        Path(route).write_bytes(response.body)
        count += 1