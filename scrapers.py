import os
import re
import html2text  # https://github.com/aaronsw/html2text
# from bs4 import BeautifulSoup

base_path_original = "/Users/lballard/projects/rn_scrape/original-site/"
base_path_new = "/Users/lballard/projects/rn_scrape/new/"

exclude_contains = ['_v[0-9]', '~$', '.css']

def spider_site(base_path_original, file_type):
    """ spider site to find directory structure and files """

    print base_path_original
    for root, dirs, files in os.walk(base_path_original):
        path = '/'.join(root.split('/')) + '/'
        # print (len(path) - 1) *'---' , os.path.basename(root)       
        for f in files:
            
            if [re.search(ex, f) for ex in exclude_contains if re.search(ex, f)]:
                continue  # these are old versions and other things to exclude

            if 'html' in f:
                # this is an html file so try to convert it and put in new place

                full_path =  path + f
                new_path = full_path.replace('original-site','new')

                try: 
                    content = convert_page(full_path)
                    if 'PDS_VERSION_ID' in content:
                        continue  # these are PDS indexes named like html files

                except UnicodeDecodeError:
                    # these html files could not be converted, copy them over as they are 
                    with open (full_path, "r") as myfile:
                        content = myfile.read()

                create_file(new_path, content)


def create_file(filepath, content):

    file_split = [ a for a in filepath.split('/') if a.strip() ]

    for k, file_part in enumerate(file_split):
        
        # print file_part 

        if k < len(file_split)-1:
            this_dir = '/' + '/'.join(file_split[0: file_split.index(file_part) + 1])

            if not this_dir:
                continue

            if not os.path.isdir(this_dir):
                os.makedirs(this_dir)
                print "creating directory" + this_dir

        else:
            # write content to file_path
            text_file = open(filepath, "w")
            text_file.write(content)
            text_file.close()


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


if __name__ == "__main__":
    spider_site(base_path_original, 'html')



