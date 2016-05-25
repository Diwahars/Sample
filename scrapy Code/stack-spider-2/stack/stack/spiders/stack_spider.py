from scrapy import Spider
from scrapy.selector import Selector

from stack.items import StackItem


class StackSpider(Spider):
    name = "stack"
    allowed_domains = ["flipkart.com"]
    start_urls = [
       "http://www.flipkart.com/mobiles/pr?p%5B%5D=facets.operating_system%255B%255D%3DAndroid&sid=tyy%2C4io&otracker=ch_vn_mobile_brand_Android",
    ]

    def parse(self, response):
        questions = hxs.xpath('//div[@class="pu-details lastUnit"]')
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="pu-title fk-font-13"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="pu-final"]/div/text()').extract()[0]
            yield item
