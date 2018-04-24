#!/bin/bash
mkdir -p result
rm result/*
rm log.txt

scrapy crawl hackSpider -L WARNING --logfile=log.txt

python hidden_resource.py

python sql_injection.py

python directory_traversal.py

python open_redirect.py

python command_injection.py

chmod +x result/*.sh
