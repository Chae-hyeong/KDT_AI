import scrapy

class WikipediaSpider(scrapy.Spider):
    name = "wikipedia_python"
    start_urls = [
        'https://ko.wikipedia.org/wiki/파이썬',
    ]

    def parse(self, response):
        # 목차 항목 추출
        items = response.css('#mw-content-text > div.mw-content-ltr.mw-parser-output > div.main-pane > div.main-pane-right > div.wikipedia-ko.main-recommended.main-box').get()
        yield {
            'items': items,
        }