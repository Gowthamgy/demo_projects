
import scrapy

class ScrapyProjectItem(scrapy.Item):
    title = scrapy.Field()
    email = scrapy.Field()
    name = scrapy.Field()
