# Deploying the Website

This script will fetch the latest version from the remote repo,
build the site locally, and rsync that into the web root.

## Deploying:

_Note:_ If this is your first time, see **Initial Setup** below.

Log into the webserver, pull the latest version from github, activate the virtualenv, and run the script:

    cd ~/ringsnode_website
    git pull
    cd deploy/
    source venv/bin/activate
    fab deploy


## Initial Setup:

1. While logged into the web server, grab a local copy of the remote repo

        cd ~/
        git clone https://github.com/basilleaf/ringsnode_website.git


2. Create the python virtual environment for the deploy script

        cd ringsnode_website/deploy/
        virtualenv venv --distribute

3. Activate the virtualenv and install the requirements

        source venv/bin/activate
        pip install -r requirements.txt

4. Create a secrets.py file

        cp secrets_template.py secrets.py


5. Edit the secrets.py file

    Edit the secrets.py to define the web root directory.
    (Web root must be accessible locally to this script)

6. Try it out!

    fab deploy
