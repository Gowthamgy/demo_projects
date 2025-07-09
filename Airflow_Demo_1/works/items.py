# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WorksItem(scrapy.Item):
    employee_id = scrapy.Field()      # Optional, skip if auto-incremented
    first_name = scrapy.Field()
    last_name = scrapy.Field()
    email = scrapy.Field()
    phone_number = scrapy.Field()
    hire_date = scrapy.Field()
    job_id = scrapy.Field()
    salary = scrapy.Field()
    commission_pct = scrapy.Field()
    manager_id = scrapy.Field()
    department_id = scrapy.Field()
