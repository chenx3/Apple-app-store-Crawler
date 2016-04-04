# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    category = scrapy.Field()
    updated = scrapy.Field()
    size = scrapy.Field()
    languages = scrapy.Field()
    seller = scrapy.Field()
    rating = scrapy.Field()
    compatibility = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()
    href = scrapy.Field()