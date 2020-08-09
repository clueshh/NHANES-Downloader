import scrapy

from util import get_component
from items import NHANESDescriptor
from spiders.start_urls import start_urls


class JSONSpider(scrapy.Spider):
    name = "nhanes_json"
    start_urls = start_urls

    custom_settings = {
        'ITEM_PIPELINES': {
            'pipelines.JSONPipeline': 1
        }
    }

    def parse(self, response):
        component = get_component(response.url)

        table_rows = response.css('table#GridView1 tr')

        htm_selectors = [selector for selector in
                         table_rows.css('td:nth-child(3) a::attr(href)') if selector.get().endswith('.htm')]

        self.logger.info(f'Scraping {len(htm_selectors)} .htm files from component: {component}')

        for link in htm_selectors:
            absolute_url = response.urljoin(link.get())
            yield scrapy.Request(url=absolute_url, callback=self.parse_htm, cb_kwargs=dict(component=component))

    @staticmethod
    def parse_htm(response, component):
        div_text = response.css('#CodebookLinks a::text').extract()
        labels = [value.split(' - ', 1) for value in div_text]

        item = NHANESDescriptor()
        item['component'] = component
        item['file_url'] = response.url
        item['values'] = {label[0]: label[1] for label in labels}

        yield item
