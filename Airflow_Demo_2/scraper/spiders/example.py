import scrapy

class SampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['https://httpbin.org/html']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'email': '123@example.com',
            'name': 'gy123'
        }
