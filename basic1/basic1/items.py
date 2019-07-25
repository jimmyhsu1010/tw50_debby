# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Basic1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    code = scrapy.Field()
    qgr = scrapy.Field()
    qopr = scrapy.Field()
    qnir = scrapy.Field()
    qroa = scrapy.Field()
    qroe = scrapy.Field()


