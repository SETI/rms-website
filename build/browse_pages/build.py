from __future__ import print_function
import os
import yaml
from shutil import copyfile

base_path = '/volumes/TINY/pdsdata/browse/'

class BuildBrowsePages:

    def build_yaml(self):
        """
        builds the yaml file that describes the directory structure and image paths
        """
        # walk the browse images directory trees
        all_images = {}
        for root, dirs, files in os.walk(base_path):

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
                    all_images[volume_group][volume_id].setdefault(volume_subdir, []).append(url_path + fname)

        # now we have all the images, build the jekyll data files from that
        for enclosing_vol in all_images:

            if not os.path.exists("../../website/_data/browse/%s/" % enclosing_vol):
                os.makedirs("../../website/_data/browse/%s/" % enclosing_vol)

            for volume_id in all_images[enclosing_vol]:

                if not os.path.exists("../../website/_data/browse/%s/%s/" % (enclosing_vol, volume_id)):
                    os.makedirs("../../website/_data/browse/%s/%s/" % (enclosing_vol, volume_id))

                for volume_subdir in all_images[enclosing_vol][volume_id]:

                    with open("../../website/_data/browse/%s/%s/%s.yml" % (enclosing_vol, volume_id, volume_subdir), 'w') as outfile:
                        yaml.dump(all_images[enclosing_vol][volume_id][volume_subdir], outfile, default_flow_style=False)


if __name__ == '__main__':
    build = BuildBrowsePages()
    build.build_yaml()
    print("ok")
