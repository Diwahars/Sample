# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['flipkart.com']
    start_urls = [
"http://www.flipkart.com/mobiles/pr?p%5B%5D=facets.operating_system%255B%255D%3DAndroid&sid=tyy%2C4io&otracker=ch_vn_mobile_brand_Android"
    ]

    rules = [
        Rule(LinkExtractor(allow=r'questions\?page=[0-9]&sort=newest'),
             callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        questions = hxs.xpath('//div[@class="pu-details lastUnit"]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="pu-title fk-font-13"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="pu-final"]/div/text()').extract()[0]
            yield item
