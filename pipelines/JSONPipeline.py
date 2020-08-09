import os
import json
from util import get_file_path


class JSONPipeline:
    def __init__(self):
        pass

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        file = get_file_path(item['file_url'], item['component'], extension='.JSON')
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'w') as f:
            f.write(json.dumps(item['values'], indent=4))

        return item
