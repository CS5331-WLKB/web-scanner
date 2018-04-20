# -*- coding: utf-8 -*-
import scrapy
from benchmarkSpider.items import hackItem

class HackspiderSpider(scrapy.Spider):
    name = 'hackSpider'
    allowed_domains = ['target.com']
    start_urls = ['http://target.com/']
    
    def parse(self, response):
        sel = scrapy.Selector(response)
        links_in_a_page = sel.xpath('//a[@href]') 

        for link_sel in links_in_a_page:
            item = hackItem()
            link = str(link_sel.re('href="(.*?)"')[0])    
            if link:
                if not link.startswith('http'):  
                    link = response.url + link 
                yield scrapy.Request(link, callback=self.parse)  
                item['link'] = link
                link_text = link_sel.xpath('text()').extract()  
                if link_text:
                    item['link_text'] = str(link_text[0].encode('utf-8').strip())
                else:
                    item['link_text'] = None
                print item['link'],   
                print item['link_text']
                yield item
