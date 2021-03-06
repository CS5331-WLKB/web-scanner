# -*- coding: utf-8 -*-
import scrapy
from benchmarkSpider.items import HackItem
from benchmarkSpider.utility import domain, start_url
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class HackspiderSpider(CrawlSpider):
    name = 'hackSpider'
    # allowed_domains = ['target.com']
    # start_urls = ['http://target.com/']
    allowed_domains = [domain]
    start_urls = [start_url]

    rules = [
        Rule(
            LinkExtractor(allow=(),
            restrict_xpaths=('//a[@href]')),
            callback='parse_item',
            follow=True
        )
    ]

    def parse_start_url(self,response):
        item = HackItem()
        sel = scrapy.Selector(response)

        content_list = sel.xpath('//input[@name]').xpath('@name').extract()
        item['link'] = start_url
        item['content'] = content_list
        item['content_type'] = 'input names'

        return item        

    def parse_item(self,response):
        item= HackItem()
        sel = scrapy.Selector(response)
        #input_names = sel.xpath('//input[@name]').xpath('@name').extract()
        #script = sel.xpath('//script').xpath("text()").extract()
        links = sel.xpath('//a[@href]')
        pre = sel.xpath("//pre").xpath("text()").extract()
        item['link'] = response.url
        item['content'] = pre
        item['content_type'] = 'pre'

        items = [item]
        
        for link_sel in links:
            l = str(link_sel.re('href="(.*?)"')[0])
            if l:
                if not l.startswith('http'):
                    link = response.urljoin(l)
                    temp_item = HackItem()
                    temp_item['link'] = link
                    temp_item['content'] = []
                    temp_item['content_type'] = 'input names'
                    items.append(temp_item)

        for item in items:
            yield item

        
    
    
    '''
    def parse(self, response):
        sel = scrapy.Selector(response)
        links = sel.xpath('//a[@href]') 
        input_names = sel.xpath('//input[@name]').xpath('@name').extract()

        item 
        print item['content']       
        for link_sel in links:
            link = str(link_sel.re('href="(.*?)"')[0])

            if link:
                if not link.startswith('http'):
                    link = response.urljoin(link)
                yield scrapy.Request(link,meta={'item':item},callback=self.parse)
    '''         

        
