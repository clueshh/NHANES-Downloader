import os
import urllib.parse


def get_file_path(url, component, extension=None):
    year, name = url.split('/')[-2:]
    path = os.path.join('data', component, year)
    if extension:
        return os.path.join(path, os.path.splitext(name)[0] + extension)
    else:
        return os.path.join(path, name)


def get_component(url):
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.parse_qs(parsed.query).get('Component')[0]
