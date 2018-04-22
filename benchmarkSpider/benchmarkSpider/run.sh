#!/bin/bash
rm -rf result/*
scrapy crawl hackSpider -L WARNING --logfile=log
python hack.py
