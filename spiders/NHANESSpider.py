import scrapy
from scrapy.loader import ItemLoader

import urllib.parse

from items import NHANESDownloaderItem

start_urls = ['http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Demographics',
              'http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Dietary',
              'http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Examination',
              'http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Laboratory',
              'http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Questionnaire',
              'http://wwwn.cdc.gov/nchs/nhanes/search/datapage.aspx?Component=Non-Public']


class NHANESSpider(scrapy.Spider):
    name = "nhanes"
    start_urls = start_urls

    custom_settings = {
        'ITEM_PIPELINES': {
            'pipelines.DownloaderPipeline': 1
        }
    }

    def parse(self, response):
        url = response.url
        parsed = urllib.parse.urlparse(url)
        component = urllib.parse.parse_qs(parsed.query).get('Component')[0]

        table_rows = response.css('table#GridView1 tr')

        xpt_selectors = [selector for selector in
                         table_rows.css('td:nth-child(4) a::attr(href)') if selector.get().endswith('.XPT')]

        self.logger.info(f'Scraping {len(xpt_selectors)} .xpt files files from component: {component}')

        for link in xpt_selectors:
            loader = ItemLoader(item=NHANESDownloaderItem(), selector=link)

            absolute_url = response.urljoin(link.get())
            loader.add_value('file_urls', absolute_url)
            loader.add_value('component', component)

            yield loader.load_item()
