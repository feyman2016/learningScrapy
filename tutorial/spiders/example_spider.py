import scrapy

class MySpider(scrapy.Spider):
    name = 'myspider'
    start_urls = [
        "http://example.com",
        "http://example.org",
        "http://example.net",
    ]

    def parse(self, response):
        if ".org" in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response,self)