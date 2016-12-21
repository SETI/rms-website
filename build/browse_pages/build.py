from __future__ import print_function
import os
import yaml
from shutil import copyfile
from secrets import BASE_PATH_IMAGES

data_dir = "../../website/_data/browse/"  # paths relative to this script
browse_dir = "../../website/browse/"

# the jekyll markdown pages will all look the same, there are 4 different kinds tho
# use these as the base copy from which to copy into all the other directories
page_templates = {  # paths relative to this script
    'index': '../../website/browse/index.html',  # the main index. a list of volume groups
    'volumes': '../../website/browse/COISS_2xxx/index.html',  # a page listing all volumes in a group
    'sub_dirs': '../../website/browse/COISS_2xxx/COISS_2069/index.html',  # list of all sub_dirs in a volume
    'images': '../../website/browse/COISS_2xxx/COISS_2069/1688230146_1688906749/index.html'
}

class BuildBrowsePages:

    def spider_images(self):
        """
        builds the yaml file that describes the directory structure and image paths
        """
        # walk the browse images directory trees and create a data structure for jekyll data pages
        all_images = {}
        for root, dirs, files in os.walk(BASE_PATH_IMAGES):

            for fname in files:
                if 'jpg' in fname or 'png' in fname or 'jpeg' in fname:
                    # We've found the images, build a page to navigate them
                    # and also their enclosing directories, here
                    # print(fname)
                    volume_group = root.split('/')[5]
                    volume_id = root.split('/')[6]
                    volume_subdir = root.split('/')[-1]

                    if volume_group not in all_images:
                        all_images[volume_group] = {}

                    if volume_id not in all_images[volume_group]:
                        all_images[volume_group][volume_id] = {}

                    url_path = '/'.join(root.split('/')[4:])
                    all_images[volume_group][volume_id].setdefault(volume_subdir, []).append("%s/%s" % (url_path, fname))

        return all_images


    def build_dirs(self, all_images):
        """  build the _data pages and browse/ pages """

        for enclosing_vol in all_images:

            # create the enclosing volume directories (ie COISS_2xxx)
            if not os.path.exists("%s%s/" % (data_dir, enclosing_vol)):
                os.makedirs("%s%s/" % (data_dir, enclosing_vol))
            if not os.path.exists("%s%s/" % (browse_dir, enclosing_vol)):
                os.makedirs("%s%s/" % (browse_dir, enclosing_vol))

            # copy the html file to browse
            if page_templates['volumes'] != "%s%s/index.html" % (browse_dir, enclosing_vol):
                copyfile(page_templates['volumes'], "%s%s/index.html" % (browse_dir, enclosing_vol))

            for volume_id in all_images[enclosing_vol]:

                # create the volume_directories (ie COISS_2xxx/COISS_2098)
                if not os.path.exists("%s%s/%s/" % (data_dir, enclosing_vol, volume_id)):
                    os.makedirs("%s%s/%s/" % (data_dir, enclosing_vol, volume_id))
                if not os.path.exists("%s%s/%s/" % (browse_dir, enclosing_vol, volume_id)):
                    os.makedirs("%s%s/%s/" % (browse_dir, enclosing_vol, volume_id))

                # copy the html file to browse
                if page_templates['sub_dirs'] != "%s%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id):
                    copyfile(page_templates['sub_dirs'], "%s%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id))

                for volume_subdir in all_images[enclosing_vol][volume_id]:

                    # write the yaml file to the data directory
                    with open("%s%s/%s/%s.yml" % (data_dir, enclosing_vol, volume_id, volume_subdir), 'w') as outfile:
                        yaml.dump(all_images[enclosing_vol][volume_id][volume_subdir], outfile, default_flow_style=False)

                    # write the images to browse
                    if not os.path.exists("%s%s/%s/%s/" % (browse_dir, enclosing_vol, volume_id, volume_subdir)):
                        os.makedirs("%s%s/%s/%s/" % (browse_dir, enclosing_vol, volume_id, volume_subdir))

                    # here copy the template file into place
                    if page_templates['images'] != "%s%s/%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id, volume_subdir):
                        copyfile(page_templates['images'], "%s%s/%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id, volume_subdir))



if __name__ == '__main__':
    build = BuildBrowsePages()
    all_images = build.spider_images()
    build.build_dirs(all_images)
    print("ok")
