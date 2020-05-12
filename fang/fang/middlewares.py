# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random

class UserAgentDownloadMiddleware(object):
    USER_AGENT =[
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1b1pre) Gecko/20080929020931 Minefield/3.1b1pre',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9) Gecko',
        'Opera/6.12 (Linux 2.4.20-4GB i686; U) [en]',
        'Mozilla/5.0 (Windows NT 6.1; rv:25.5) Gecko/20150609 Firefox/31.9 PaleMoon/25.5.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
        'FAST-WebCrawler/3.6/FirstPage (atw-crawler at fast dot no;http://fast.no/support/crawler.asp)'
    ]

    def process_request(self, request, spider):
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent