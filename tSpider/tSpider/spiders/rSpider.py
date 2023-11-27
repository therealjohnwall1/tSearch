# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from pathlib import Path
# # from ../util/checkProx import 

# class rSpider(CrawlSpider):
#     #set crawler depth to 10
#     name = "rSpider"
    
#     sites = open("../util/top-1000-websites.txt", "r")
#     urls = sites.readlines()
#     proxy = ProxyChecker()
#     proxy.runner() #ensures proxy's are checked before spider starts
#                     #will check new proxies on the clock

#     def start_requests(self):
#         for url in self.urls:
#             yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': self.proxy.getProxy()})

#     rules = (
#         Rule(callback = "parse_item")
#     )

#     def parse_item(self,response):
#         fileName = response.url.split("/")[-2] + '.html'
#         route = "../util/storage/" + fileName
#         Path(route).write_bytes(response.body)

        