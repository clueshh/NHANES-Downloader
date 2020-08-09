import scrapy


class NHANESDownloaderItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    component = scrapy.Field()


class NHANESDescriptor(scrapy.Item):
    values = scrapy.Field()
    file_url = scrapy.Field()
    component = scrapy.Field()
