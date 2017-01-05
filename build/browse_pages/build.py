from __future__ import print_function
import os
import yaml
from shutil import copyfile
from secrets import BASE_PATH_IMAGES

data_dir = "../../website/_data/browse/"  # paths relative to this script
browse_dir = "../../website/browse/"

markdown_template = """
---
layout: %s
---

""".strip()

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

        # first build the main browse index file
        with open("%s/index.html" % (browse_dir), 'w') as f:
            print(markdown_template % 'browse_index', file=f)

        for enclosing_vol in all_images:

            # create the enclosing volume directories (ie COISS_2xxx)
            if not os.path.exists("%s%s/" % (data_dir, enclosing_vol)):
                os.makedirs("%s%s/" % (data_dir, enclosing_vol))
            if not os.path.exists("%s%s/" % (browse_dir, enclosing_vol)):
                os.makedirs("%s%s/" % (browse_dir, enclosing_vol))

            # copy the html file to browse
            with open("%s%s/index.html" % (browse_dir, enclosing_vol), 'w') as f:
                print(markdown_template % 'browse_volumes', file=f)

            for volume_id in all_images[enclosing_vol]:

                # create the volume_directories (ie COISS_2xxx/COISS_2098)
                if not os.path.exists("%s%s/%s/" % (data_dir, enclosing_vol, volume_id)):
                    os.makedirs("%s%s/%s/" % (data_dir, enclosing_vol, volume_id))
                if not os.path.exists("%s%s/%s/" % (browse_dir, enclosing_vol, volume_id)):
                    os.makedirs("%s%s/%s/" % (browse_dir, enclosing_vol, volume_id))

                # copy the html file to browse
                with open("%s%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id), 'w') as f:
                    print(markdown_template % 'browse_subdirs', file=f)

                for volume_subdir in all_images[enclosing_vol][volume_id]:

                    # write the yaml file to the data directory
                    with open("%s%s/%s/%s.yml" % (data_dir, enclosing_vol, volume_id, volume_subdir), 'w') as outfile:
                        yaml.dump(all_images[enclosing_vol][volume_id][volume_subdir], outfile, default_flow_style=False)

                    # write the images to browse
                    if not os.path.exists("%s%s/%s/%s/" % (browse_dir, enclosing_vol, volume_id, volume_subdir)):
                        os.makedirs("%s%s/%s/%s/" % (browse_dir, enclosing_vol, volume_id, volume_subdir))

                    # here copy the template file into place
                    with open("%s%s/%s/%s/index.html" % (browse_dir, enclosing_vol, volume_id, volume_subdir), 'w') as f:
                        print(markdown_template % 'browse_images', file=f)


if __name__ == '__main__':
    build = BuildBrowsePages()
    all_images = build.spider_images()
    build.build_dirs(all_images)
    print("ok")
