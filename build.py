from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from crawler.tSpider.spiders import crawlerSpider

configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)
runner.crawl(crawlerSpider.rSpider)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
