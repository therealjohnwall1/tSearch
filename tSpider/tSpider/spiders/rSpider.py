from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from pathlib import Path

class rSpider(CrawlSpider):
    name = "rSpider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]
    rules = (
        Rule(LinkExtractor(allow = "catalogue/category")),
        Rule(LinkExtractor(allow = "catalogue", deny = "category"), callback = "parse_item"),
    )

    def parse_item(self,response):
        fileName = response.url.split("/")[-2] + '.html'
        route = "../util/storage/" + fileName
        Path(route).write_bytes(response.body)