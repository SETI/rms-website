from __future__ import print_function
import sys
from fabric.api import env, cd, lcd, run, local, abort
from fabric.contrib.console import confirm
from secrets import PROD_DIR, PROD_USR

env.hosts = ['pds-rings.seti.org']

def deploy():
    """ You are in /deploy so go a level up and git pull """

    # You are in /deploy so go a level up and git pull
    with lcd("../"):
        local("git pull")

    # build the website. 
    # Note that _config.yml must not be excluding any files
    with lcd("../website"):
        local("jekyll build")
        local("rsync -rv --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz _site/ %s@pds-rings.seti.org:~/website/." % (PROD_USR))

    # on the server, copy the website to the production directory
    with cd('~/'):
        run("sudo rsync -rv --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz website/ %s/. " % (PROD_DIR))
