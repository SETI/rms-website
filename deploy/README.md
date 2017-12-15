# Deploying the Website to Production

Deploying to production means first deploying to our Admin server,
making sure all changes look ok, then deploying to production server.

## Deploying:

_Note:_ If this is your first time, see **Initial Setup** below.

After you have reviewed/tested your changes locally and then pushed your
changes to the github remote:

1. Deploy to admin:

    cd ringsnode_website/deploy  
    
    source venv/bin/activate

    fab deploy admin

2. Review the admin website:

    http://admin.pds-rings.csc.seti.org/

3. If admin site looks good, deploy the admin site to the production server:

    fab deploy production


## Initial Setup:

1. Log into the admin server, grab a local copy of the remote repo

        cd ~/
        git clone https://github.com/basilleaf/ringsnode_website.git
        cd ringsnode_website/
        git checkout production

2. On the machine where you will be working/making changes in the Jekyll repo,
   Create the python virtual environment for the deploy script

        cd ringsnode_website/deploy/
        virtualenv venv --distribute

3. Activate the virtualenv and install the requirements

        source venv/bin/activate
        pip install -r requirements.txt

4. Create a secrets.py file

        cp secrets_template.py secrets.py

5. Edit the secrets.py file

    Edit the secrets.py to define the production web root directory.

6. Log into the production server, create the website_staging directory in your  
   user root.

    mkdir ~/website_staging/
