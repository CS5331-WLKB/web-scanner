#!/bin/bash
rm -rf result/*
echo {} > result/DT_scope.json

scrapy crawl hackSpider -L WARNING

chmod +x result/DT_script.sh
