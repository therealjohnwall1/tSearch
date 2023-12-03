import requests 
from bs4 import BeautifulSoup

from scrapy.http import HtmlResponse

r = requests.get("https://marriott.com")
res = HtmlResponse(url=r.url, body=r.content, encoding = 'utf-8')
# print(r.response)
# print(type(r.response))



def html_index(response):
    url = response.url
    site = BeautifulSoup(response.body, 'html.parser')
    # print(site.prettify())
    x = site.find_all('p')
    print(x)
    print("*"* 10)
    links = site.find_all('a')
    print(links)




html_index(res)