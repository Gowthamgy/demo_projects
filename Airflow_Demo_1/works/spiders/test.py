import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["http://httpbin.org/"]

    def parse(self, response):
        yield {
            # "title": response.xpath("//title/text()").get(),
            # "email": "okoi@gmail.com",
            # "name": "ara",
            # "url": response.url,
            # ========================================
            "first_name": "yuvarani",
            "last_name": "gy",
            "email": "yuv.doe@example.com",
            "phone_number": "+48293492349",
            "hire_date": "2025-07-05",  # Should be in YYYY-MM-DD format
            "job_id": "DEV007",
            "salary": 90000.00,
            "commission_pct": 0.08,
            "manager_id": 102,
            "department_id": 5
        }           