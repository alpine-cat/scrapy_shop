import scrapy
import shop.items as items
from scrapy_redis.spiders import RedisSpider
import json


class PorterSpider(RedisSpider):
    name = 'net-a-porter'
    allowed_domains = ['www.net-a-porter.com']

    def parse_page_info(self, response):
        urls = response.xpath(
            "//div[@id='product-list']/ul[contains(@class, 'products')]/li/div[@class='product-image']/a/@href"
        ).extract()

        for u in urls:
            yield scrapy.Request(url='https://www.net-a-porter.com'+u, callback=self.parse_product_info,
                                 meta={'category': response.meta['category']})

    def parse(self, response):
        category = response.url[response.url.find("Clothing/")+len("Clothing/"): ]
        pages = int(response.xpath(
            "//div[contains(@class, 'page-numbers')]/div[contains(@class,'pagination-links')]/@data-lastpage"
        ).extract_first())

        for p in range(1, pages+1):
            p_url = response.url + '?pn=' + str(p)
            yield scrapy.Request(url=p_url, callback=self.parse_page_info,
                                 meta={'category': category})

    def parse_product_info(self, response):
        item = items.ProductItem()
        item['url'] = response.url
        item['category'] = response.meta['category']
        item['title'] = response.xpath(
            "//div[@id='main-product']/div[contains(@class, 'container-title')]/h2/text()"
        ).extract_first()
        item['images'] = response.xpath(
            "//div[contains(@class, 'main-carousel-wrapper')]/div[@id='main-image-carousel']/ul/li/img[contains(@class, 'first-image')]/@src"
        ).extract_first()

        price_data = response.xpath(
            "//div[contains(@class, 'container-title')]/nap-price[@class='product-price']/@price"
        ).extract_first()
        _ = json.loads(price_data)
        price = _["amount"]*0.01

        item['price'] = price

        sizes_data = response.xpath(
            "//div[contains(@class,'sizing-container')]/select-dropdown/@options"
        ).extract_first()
        _ = json.loads(sizes_data)
        sizes = ''
        for i in range(0, len(_)):
            sizes += _[i]['displaySize']+'\n'

        item['sizes'] = sizes

        item['description'] = ''.join(response.xpath(
            "//div[contains(@class, 'container-details')]/div[@id='product-details-accordion']//text()"
        ).extract()).strip().replace('\n', '').replace('\r', '')

        return item
