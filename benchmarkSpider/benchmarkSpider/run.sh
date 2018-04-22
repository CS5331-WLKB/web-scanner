#!/bin/bash
rm result.json
rm log.txt

scrapy crawl hackSpider -L WARNING --logfile=log.txt

python hidden_resource.py

python sql_injection.py

python directory_traversal.py

python open_redirect.py