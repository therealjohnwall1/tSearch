from pathlib import Path
import scrapy
from fake_useragent import UserAgent
class mainSpider(scrapy.Spider):
    name = "tSpider"
    allowed_domains = []
# add ip rotation
    def start_requests(self):
        # reader = open("util/top-1000-websites.txt", "r")
        reader = open("../util/prat.txt", "r")
        # start_urls = reader.readlines()
        for line in reader:
            # if "https" not in line:
            #     line = "https://" + line
            yield scrapy.Request(url=line, callback=self.parse)
    
    def parse(self,response):
        fileName = response.url.split("/")[-2] + '.html'
        route = "../util/storage/" + fileName
        Path(route).write_bytes(response.body)
        for link in self.link_extractor(response):
            yield scrapy.Request(url=link, callback=self.parse)




    