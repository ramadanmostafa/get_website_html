# -*- coding: utf-8 -*-
import scrapy


class GetHtmlSpider(scrapy.Spider):
    name = "get_html"

    def __init__(self, website_url='', domain=None, *args, **kwargs):
        super(GetHtmlSpider, self).__init__(*args, **kwargs)
        self.start_urls = [website_url]

    def parse(self, response):
        f = open(str(response.url).replace(self.start_urls[0], "").replace("/", "_") + ".html", 'wb')
        f.write(response.body)
        f.close()
        new_urls = response.xpath('//a/@href').extract()
        for new_url in new_urls:
            if self.start_urls[0] in response.urljoin(new_url):
                yield scrapy.Request(response.urljoin(new_url), self.parse)
