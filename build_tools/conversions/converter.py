import os
import re
import sys
import html2text  # https://github.com/aaronsw/html2text
from shutil import copyfile
from django.utils.encoding import smart_str
from template_snippets import template_begin

exclude_contains = ['_v[0-9]', '~$', '.css']
base_path_original = "/Users/lballard/projects/ringsnode_website/original_site/"
base_path_new = "/Users/lballard/projects/ringsnode_website/converted_markdown/"

class Converter():

    def deep_copy_dry_run(self, base_path):
        """ spider site site and copy all directories and files, 
            excluding exclude_contains """

        c = 0
        for root, dirs, files in os.walk(base_path):

            # print (len(path) - 1) *'---' , os.path.basename(root)       
            
            for f in files:
                if [re.search(ex, f) for ex in exclude_contains if re.search(ex, f)]:
                    continue  # this is being excluded

                full_path = os.path.join(root, f)

                new_path = full_path.replace(base_path_original,base_path_new)

                c += 1
                print c
                yield (full_path, new_path)


    def deep_copy(self, base_path):
        """ spider site site and copy all directories and files, 
            excluding exclude_contains """

        for (full_path, new_path) in self.deep_copy_dry_run(base_path):
    
            file_split = [ a for a in new_path.split('/') if a.strip() ]

            for k, file_part in enumerate(file_split):
                
                # print file_part 

                if k < len(file_split)-1:
                    this_dir = '/' + '/'.join(file_split[0: file_split.index(file_part) + 1])

                    if not this_dir:
                        continue

                    if not os.path.isdir(this_dir):
                        os.makedirs(this_dir)
                        print "creating directory" + this_dir

            copyfile(full_path, new_path)
            print "copied %s \nto %s \n" % (full_path, new_path)


    def html_to_md(self, base_path):

        c = 0
        for (full_path, new_path) in self.deep_copy_dry_run(base_path):

            if 'html' in new_path:
                # this is an html file so try to convert it and put in new place
                try:
                    content = template_begin + "\n\n" + self.convert_page(full_path)

                    if 'PDS_VERSION_ID' in content:
                        # these are PDS documents for some reason named .html, 
                        # leave them as is
                        continue 

                except UnicodeDecodeError:
                    # these html files could not be converted, do nothing 
                    continue    


                self.create_file(new_path, content)
                c += 1
                print 'created file: ' + str(c) + "\n" + new_path



    def create_file(self, filepath, content):

        content = smart_str(content)

        # write content to file_path
        text_file = open(filepath, "w")
        text_file.write(content)
        text_file.close()


    def convert_page(self, filename):
    	"""  convert html page to markdown """

    	with open(filename) as f:
    		return html2text.html2text(f.read())




if __name__ == "__main__":
    
    c = Converter()

    try:
        task = sys.argv[1] 
    except: 
        task = ''


    if task == 'deep_copy':
        c.deep_copy(base_path_original)

    elif task == 'html_to_md':
        c.html_to_md(base_path_original)

    else:
        for i in c.deep_copy_dry_run(base_path_original):
            print "\n".join(i) + "\n" 
        

        print """
            This has been a dry run!

            pass 'deep_copy' or 'html_to_md' as first argv

            we will be copying from:

                %s

            to: 

                %s

            """ % (base_path_original, base_path_new)

    # spider_site(base_path_original, 'html')



