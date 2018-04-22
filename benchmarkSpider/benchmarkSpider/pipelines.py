# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.exceptions import DropItem
import os
import codecs

class hackPipeLine(object):
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))+'/result/'+'url_result.json'
        self.seen = set()  

    def process_item(self, item, spider):
        if item['link'] in self.seen:
            raise DropItem('Duplicate link %s' % item['link'])
        self.seen.add(item['link'])

        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        with open(self.path, 'a') as f:
            f.write(line)
        return item
