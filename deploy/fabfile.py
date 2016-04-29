from __future__ import print_function
import sys
import socket
from fabric.api import env, cd, lcd, run, local, abort
from fabric.contrib.console import confirm
from secrets import PROD_DIR, PROD_USR

env.hosts = ['pds-rings.seti.org']

def deploy():
    """ this will pull the website from github, build it locally, transfer
        it to production server, and move it into production directory on that server"""

    # is this your laptop or logged into the web server? (want this script to work on both)
    web_server = False
    if 'pds-rings' in socket.gethostname():
        web_server = True

    # You are in /deploy so go a level up and git pull
    with lcd("../"):
        print("pulling the latest site from github: https://github.com/basilleaf/ringsnode_website")
        local("git pull")

    # build the website. 
    # Note that _config.yml must not be excluding any files!!!! 
    # TODO: make this impossible to fail
    with lcd("../website"):
        
        local("jekyll build")

        if web_server:
            # we are on the web server, 
            # transfer _site to a local directory called "website" 
            local("rsync -r --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz _site/ ~/website/.")
        else: 
            # copy the local _site to the remote directory on pds-rings called "website"
            print('Transfering to your remote home directory..')
            local("rsync -r --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz _site/ %s@pds-rings.seti.org:~/website/." % (PROD_USR))

    # on the server, copy the website to the production directory
    rsync_cmd = "sudo rsync -r %s --exclude=*.tif --exclude=*.tiff --exclude=*.tgz --exclude=*.tar.gz website/ %s. " 
    if web_server: 
        with lcd('~/'):
            # first do a dry run:
            local(rsync_cmd % ('--dry-run --itemize-changes ',PROD_DIR))
            if confirm("The above was a dry run. If the above looks good, push to production:"):
                local(rsync_cmd % ('',PROD_DIR))
                print("\n*** Production Website Has Been Updated! ***\n")
                sys.exit()
            else:
                print("\nDeployment Aborted\n")        
    else: 
        with cd('~/'):
            # first do a dry run:
            run(rsync_cmd % ('--dry-run --itemize-changes ',PROD_DIR))
            if confirm("The above was a dry run. If the above looks good, push to production:"):
                run(rsync_cmd % ('',PROD_DIR))
                print("\n*** Production Website Has Been Updated! ***\n")
                sys.exit()
            else:
                print("\nDeployment Aborted\n")        


