from pathlib import Path
import scrapy

count = 0
class mainSpider(scrapy.Spider):
    name = "mainSpider"

    def start_requests(self):
        reader = open("util/top-1000-websites.txt", "r")
        # start_urls = reader.readlines()
        for line in reader:
            if "https" not in line:
                line = "https://" + line
            yield scrapy.Request(url=line, callback=self.parse)
    
    def parse(self,response):
        fileName = count + response.url.split("/")[-2] + '.html'
        count+=1
        Path("util/storage/{fileName}").write_bytes(response.body)
        




    