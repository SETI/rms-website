import os
import glob
from jinja2 import Template
from scrape import Scraper

base_path = '../../converted_markdown/saturn/cassini/'  # converted markdown files
scraper = Scraper(base_path=base_path)

all_files = glob.glob(base_path + '2*.html')

for file_to_scrape in all_files:
    data = scraper.scrape(file_to_scrape=file_to_scrape)

    if not data:
        print "nope: "
        print "{}".format(file_to_scrape)
    # header = template.render()
