from __future__ import print_function
import sys
from fabric.api import env, cd, lcd, run, local, abort
from fabric.contrib.console import confirm
from secrets import PROD_DIR, PROD_USR

env.hosts = ['pds-rings.seti.org']

def deploy():
    """ this will pull the website from github, build it locally, transfer
        it to production server, and move it into production directory on that server"""

    # You are in /deploy so go a level up and git pull
    with lcd("../"):
        local("git pull")

    # build the website. 
    # Note that _config.yml must not be excluding any files
    with lcd("../website"):
        local("jekyll build")
        print('Transfering to your remote home directory..')
        local("rsync -r --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz _site/ %s@pds-rings.seti.org:~/website/." % (PROD_USR))

    # on the server, copy the website to the production directory
    rsync_cmd = "sudo rsync -r %s --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz website/ %s. " 

    # first do a dry run:
    with cd('~/'):
        run(rsync_cmd % ('--dry-run --itemize-changes ',PROD_DIR))

    if confirm("The above was a dry run. If the above looks good, push to production:"):
        with cd('~/'):
            run(rsync_cmd % ('',PROD_DIR))

        print("Finished! \n")
        sys.exit()

    else:
        print("Deployment Aborted")
