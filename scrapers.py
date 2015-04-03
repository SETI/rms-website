import os
import re
import html2text  # https://github.com/aaronsw/html2text
# from bs4 import BeautifulSoup

base_path_original = "/Users/lballard/projects/rn_scrape/original/rn_site/"
base_path_new = "/Users/lballard/projects/rn_scrape/new/rn_site/"

exclude_contains = ['_v[0-9]', '~$', '.css']

def spider_site(base_path_original, file_type):
    """ spider site to find directory structure and files """

    for root, dirs, files in os.walk(base_path_original):
        path = '/'.join(root.split('/')) + '/'
        # print (len(path) - 1) *'---' , os.path.basename(root)       
        print '--------------------'
        print path + os.path.basename(root)       
        print '--------------------'
        for f in files:
            print f
            
            if [re.search(ex, f) for ex in exclude_contains if re.search(ex, f)]:
                continue

            if 'html' in f:
                # print len(path)*'---', f
                print path + f

                try: 
                    md = convert_page(path + f)

                    if 'PDS_VERSION_ID' in md:
                        continue

                    """
                        todo: 
                        figure out where to put this markdown in the /new structure
                        create directories if needed
                        keep figures and images along side? 
                    """

                    print md

                except UnicodeDecodeError:
                    """
                        todo:
                        these html files could not be converted, copy them over as they are 
                    """
                    print 'NOPE'



def convert_page(filename):
	"""  convert html page to markdown """

	with open(filename) as f:
		return html2text.html2text(f.read())

		"""
		soup = BeautifulSoup(f)

		html_title = soup.title
		page_intro = soup.h2
		all_links = soup.find_all('a')
		tabs = soup.find(id="header")
		"""







