# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
from basic1.items import Basic1Item

df = pd.read_csv("stock50.csv", encoding="big5", header=None)


class B1Spider(scrapy.Spider):
    name = 'b1'
    allowed_domains = ['tw.stock.yahoo.com']
    start_urls = []
    codes = df[0]
    for code in codes:
        start_urls.append("https://tw.stock.yahoo.com/d/s/company_" + str(code) + ".html")

    def parse(self, response):
        code = response.url[-9:-5]
        item = Basic1Item()
        content_list = response.xpath("//table[2]//tr[position()>=2 and position() <=6]/td[2]//text()").extract()
        item['code'] = code
        item['qgr'] = content_list[0]
        item['qopr'] = content_list[1]
        item['qnir'] = content_list[2]
        item['qroa'] = content_list[3]
        item['qroe'] = content_list[4]
        yield item
