
import scrapy

class SampleSpider(scrapy.Spider):
    name = 'checking'
    start_urls = ['https://httpbin.org/html']

    def parse(self, response):
        yield {
            'title': response.xpath('//h1/text()').get(),
            'email': '7892@example.com',
            'name': '9908'
        }