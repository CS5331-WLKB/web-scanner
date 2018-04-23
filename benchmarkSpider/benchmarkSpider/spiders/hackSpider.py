# -*- coding: utf-8 -*-
import scrapy
from benchmarkSpider.items import HackItem
from benchmarkSpider.utility import domain, start_url

class HackspiderSpider(scrapy.Spider):
    name = 'hackSpider'
    # allowed_domains = ['target.com']
    # start_urls = ['http://target.com/']
    allowed_domains = [domain]
    start_urls = [start_url]
    
    def parse(self, response):
        sel = scrapy.Selector(response)
        links = sel.xpath('//a[@href]') 
        inputs = sel.xpath('//input[@name]')

        for link_sel in links:
            item = HackItem()
            item['tag'] = 'link'
            link = str(link_sel.re('href="(.*?)"')[0])    
            if link:
                if not link.startswith('http'):
                    link = response.urljoin(link)
                yield scrapy.Request(link, callback=self.parse)  
                item['content'] = link
                yield item
        
        for input_sel in inputs:
            item = HackItem()
            item['tag'] ='input'
            name = str(input_sel.re('name="(*)"')[0])
            print name
            if name:
                item['content'] = name
                yield item
        
