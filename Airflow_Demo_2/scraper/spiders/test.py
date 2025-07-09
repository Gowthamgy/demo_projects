import scrapy

class SampleSpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://httpbin.org/html']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'email': '456@example.com',
            'name': '456gy'
        }
