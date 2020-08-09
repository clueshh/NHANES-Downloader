from util import get_file_path
from scrapy import Request
from scrapy.pipelines.files import FilesPipeline


class DownloaderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x, meta={'component': item.get('component')}) for x in item.get(self.files_urls_field)]

    def file_path(self, request, response=None, info=None):
        component = request.meta['component'][0]

        return get_file_path(request.url, component)
