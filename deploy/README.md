# Deploying the Website to Production

Deploying to production means first deploying to our Admin server website, making sure all changes look ok there, then deploying to production server.

The deploy script is run on the admin server so you must shell in to run this script. Note you must have VPN running to shell into all servers.

## Deploying:

_Note:_ If this is your first time, see **Initial Setup** below.

After you have reviewed/tested your changes locally and then pushed your changes to the github repo:

1. Log into admin server and change directory to this repo

        cd ~/ringsnode_website/deploy

1. Deploy to admin:

        fab deploy admin

2. Review the admin website in your web browser:

    https://admin.pds-rings.csc.seti.org/

3. If admin site looks good, deploy the admin site to the production server:

        fab deploy production


## Initial Setup:

1. Log into the admin server, be in your home directory for the next steps

2. grab a local copy of the remote repo

        cd ~/ringsnode_website/
        git clone https://github.com/SETI/pds-website.git
        cd pds-website/
        git checkout production

4. Create a secrets.py file

        cp secrets_template.py secrets.py

5. Edit the secrets.py file

    Edit the secrets.py to define the web root directory.
    (Web root must be accessible locally to this script)

6. Log into the **production server** and create the website_staging directory in your home directory

        mkdir ~/website_staging/
