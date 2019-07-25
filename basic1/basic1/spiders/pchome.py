# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import requests

class PchomeSpider(scrapy.Spider):
    name = 'pchome'
    allowed_domains = ['pchome.megatime.com.tw']
    start_urls = ['http://pchome.megatime.com.tw/stock/sto2/ock0/sid2330.html']
    # Request("http://pchome.megatime.com.tw/stock/sto2/ock0/sid2330.html", headers={'Referer':'http://pchome.megatime.com.tw/stock/sto3/ock1/sid6505.html'}, dont_filter=True)
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, headers={'Referer':'http://pchome.megatime.com.tw/stock/sto3/ock1/sid6505.html'})



    def parse(self, response):
        print(response.xpath("//tr[22]//td[position()>=2 and position()<=4]"))
