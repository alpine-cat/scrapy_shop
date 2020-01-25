# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProductItem(scrapy.Item):
    url = scrapy.Field()
    category = scrapy.Field()
    title = scrapy.Field()
    images = scrapy.Field()
    price = scrapy.Field()
    sizes = scrapy.Field()
    description = scrapy.Field()


