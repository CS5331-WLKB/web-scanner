#!/bin/bash
rm result.json
rm log

scrapy crawl hackSpider -L WARNING --logfile=log

python hidden_resource.py

python sql_injection.py

python directory_traversal.py

python open_redirect.py