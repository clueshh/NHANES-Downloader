import os

USER_AGENT = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'

LOG_LEVEL = 'INFO'

COOKIES_ENABLED = False

DOWNLOAD_TIMEOUT = 1200

FILES_STORE = os.path.dirname(os.path.realpath(__file__))

# 120 days of delay for files expiration
FILES_EXPIRES = 120
