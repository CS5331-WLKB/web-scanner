# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
import os
from scanner import Scanner

class hackPipeLine(object):
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.file = open(path+'/result/'+'url_result.json', 'w+')
        self.seen = set()  

    def process_item(self, item, spider):
        if item['link'] in self.seen:
            raise DropItem('Duplicate link %s' % item['link'])
        self.seen.add(item['link'])

        myScanner = Scanner(item['link'])
        myScanner.scan()
        
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
