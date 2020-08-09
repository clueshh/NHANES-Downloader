from scrapy.crawler import CrawlerProcess
from spiders import JSONSpider, NHANESSpider
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    process = CrawlerProcess(settings=get_project_settings())
    process.crawl(NHANESSpider)
    process.crawl(JSONSpider)
    process.start()
