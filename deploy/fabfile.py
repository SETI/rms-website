from __future__ import print_function
import sys
import socket
import time
from fabric.api import env, cd, lcd, run, local, abort
from fabric.contrib.console import confirm
from secrets import PROD_DIR

import getpass
PROD_USR = getpass.getuser()

REPO = 'https://github.com/basilleaf/ringsnode_website.git'

def deploy():
    """ This script will deploy the website to production,
        pulling it from the github repo.
        You must have sudo access to the production web root.
    """

    # You are running this in /deploy so go a level up and git pull the latest repo
    with lcd("../"):
        print("\nPulling the latest site from github.com: \n-----> %s\n" % REPO)
        time.sleep(2.5)  # please remind people we are pulling from remote
        local("git pull")

    # build the website.
    with lcd("../website"):

        local("jekyll build --config _config.yml,_config.production.yml")

        # copy the website to the production directory
        rsync_cmd = "sudo rsync -r %s --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz _site/ %s. "

        # first do a dry run:
        local(rsync_cmd % ('--dry-run --itemize-changes ',PROD_DIR))
        if confirm("The above was a dry run. If the above looks good, push to production:"):
            local(rsync_cmd % ('',PROD_DIR))
            print("\n*** Production Website Has Been Updated! ***\n")
            sys.exit()
        else:
            print("\nDeployment Aborted\n")
