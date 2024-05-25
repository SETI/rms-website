# RMS Node Website Deployment Guide

## Introduction

This document describes the processes by which the PDS RMS Node website can be updated.

There are essentially four copies of the full website:

* The visible copy on the staging server (in `/var/www`)
* The visible copy on server1 (in `/var/www`)
* The visible copy on server2 (in `/var/www`)
* The “master” copy, which is stored on the RAID45 in the directory `/volumes/webserver_assets`

At any given time, the copies on the RAID45, server1, and server2 should be identical.

There are three sources for data for the website:

1. The primary website is stored in the `SETI/pds-website` repo and is processed by jekyll to generate HTML files.
2. Various support files, including those needed for Viewmaster, backup support, documents and holdings summaries, feedback, and the ephemeris tools, are stored in the `SETI/pds-webserver` repo. Updates to these files require special knowledge and procedures and are covered in the new server installation instructions in that repo.
3. Images or documents that are too large to keep in git are stored directly on the RAID45 in the `/volumes/webserver_assets` directory. At the moment, they are intermingled with the jekyll-generated files although a project to separate them is in progress.

Each of these data sources will be addressed separately in the following sections.

## Editing, Testing, and Deploying Jekyll-Generated Content

The general process for deployment of jekyll-generated content is:

1. Using your own clone of the pds-website repo on your personal computer, edit the necessary files, convert them with jekyll (if necessary), and use a local webserver to test the results.
2. Create a new git branch for your changes, commit them, and then push them to GitHub.
3. Open a pull request and ask another team member to review your changes.
4. If any problems are found, correct them, update the branch, and iterate until the pull request is approved.
5. Merge your branch onto the master branch.
6. Login to the staging server and deploy the changes to staging to view in-situ with all other web assets available; test the results.
7. Deploy the local copy to the production servers by way of the master copy stored on the RAID45.

### Set Up a Local Website and Make Changes

This is the basic flow for making changes to the website files that are stored in git in the pds-website repo. While the steps listed below appear to be a strict chronology, more complicated changes may require multiple iterations through subsets of steps or working on some steps out of order. It is assumed that you already have a basic knowledge of jekyll, git, and GitHub.

1. First time:
    1. If you are going to be editing Jekyll files:
        1. Install Ruby and Jekyll: [https://jekyllrb.com/docs/installation/](https://jekyllrb.com/docs/installation/)
        2. Install other Jekyll packages:

            ```
            gem install jekyll-redirect-from webrick
            ```

    2. Create a clone of the pds-website repo on your local computer:

        ```
        git clone https://github.com/SETI/pds-website.git
        ```

2. Make sure you have the current version of the website:

    ```
    cd pds-website
    git checkout master
    git pull
    ```

3. Create a new branch for your changes:

	  ```
    git checkout -b <branch_name>
    ```

4. Start a local webserver. Note that web assets that are not stored in git (such as large graphics or large documents) or dynamically-generated content (like the ephemeris tools) will not be available.
    1. If you are editing jekyll files, start the jekyll server:

        ```
        cd website
        jekyll serve --config _config.yml,_config.production.yml
        ```      
        
        The website will be available at [http://127.0.0.1:4000/](http://127.0.0.1:4000/)

    2. If you are not editing jekyll files, start the built-in Python webserver:
    
        ```
        cd website
        python3 -m http.server
        ```      
        
        The website will be available at [http://127.0.0.1:8000/](http://127.0.0.1:4000/)

5. Edit files. If you are running the jekyll server, as files are changed, jekyll will automatically update the website files (which may take 10-20 seconds). When the new website files are available, refresh your browser to check the new content. If you are running the python webserver, you will just need to refresh your browser after each change.
6. When finished, exit the jekyll or python server (^C), add the files to git, and push the branch to GitHub:

    ```
    git add .
    git commit -m "<description of changes>"
    git push -u origin <branch_name>
    ```

7. Optional: Test your branch on staging
    1. Login to `staging` as webmaster
    2. Deploy changes to the local apache directory. This script will automatically pull the changes from GitHub and checkout the appropriate branch.

        ```
        cd ~/pds-website/deploy
      	./deploy_website_to_staging.sh <branch_name>
            [View the diffs and if all looks OK enter “Y”]
        ```
        

    3. View the changes on [http://staging.pds.seti.org](http://staging.pds.seti.org)

8. Create a pull request on GitHub
    1. Navigate your browser to: [https://github.com/SETI/pds-website/pulls](https://github.com/SETI/pds-website/pulls)
    2. There should be a notification at the top that says something like “&lt;branch_name> had recent pushes less than a minute ago”. Press the button to the right that says “Compare & pull request”.
    3. Fill in the title and description
    4. Select a reviewer
    5. Press “Create pull request”
9. Work with the reviewer to approve the changes.
10. Once the pull request is approved, merge your changes onto the master branch by going to the pull request page on GitHub and selecting “Merge pull request”.

### Deploy the Changes to the Production Servers

This procedure will deploy the current “master” branch on the pds-website repo to staging, then copy them to `/volumes/webserver_assets`, then deploy them to `server1` and `server2`.

Note: This procedure pertains only to HTML source documents.  For other “asset” files, which are not controlled by Git, see instructions **below**.

1. Login to `staging` as webmaster. **NOTE: Do not attempt to do this procedure logged in as anyone else!**
2. Deploy changes to the local apache directory. This script will automatically pull the changes from GitHub and checkout the **master** branch.

    ```
    cd ~/pds-website/deploy
    ./deploy_website_to_staging.sh
        [View the diffs and if all looks OK enter “Y”]
    ```

3. View the changes on [http://staging.pds.seti.org](http://staging.pds.seti.org)
4. Assuming everything is OK, deploy the changes to the production servers.
NOTE: This will deploy the _current contents_ of the `pds-website/_site` directory without updating it from GitHub or checking out a branch or running jekyll gain. Make sure the `website` directory is in the state you want it to be in, ideally by performing the above steps first.
The steps performed by this step are:
    1. Show the differences between the `pds-website/_site` and `/volumes/webserver_assets/documents` directories
    2. Copy the contents of `pds-website/_site` to `/volumes/webserver_assets/documents`
    3. Copy the contents of `/volumes/webserver_assets/documents` to `/var/www/documents` on `server1`
    4. Copy the contents of `/volumes/webserver_assets/documents` to `/var/www/documents` on `server2`

        ```
        cd ~/pds-website/deploy
        ./deploy_website_to_production.sh
            [View the diffs and if all looks OK enter “Y”]
            [Enter the password for “webmaster” when asked]
        ```

5. Verify the changes on the main website: [https://pds-rings.seti.org/](https://pds-rings.seti.org/)

## Updating and Deploying non-Jekyll Websites

Certain parts of the website (specifically the Reviews directory, containing websites intended for doing the work of peer review that are then kept for posterity) are not currently part of the Jekyll workflow.  We edit these HTML files directly, rather than using Markdown.  **However,** these website source files are still in the `pds-website` repo!

Therefore, revisions to non-Jekyll websites should be done by way of the GitHub repo, and should be deployed according to the instructions **above**. 

## Updating and Deploying non-Git Assets

Examples of non-Git assets include graphics and PDFs and other files that support the websites.  Because these assets are not primarily composed of text, GitHub is not suited as a platform for managing them.  Instead, the following instructions are to be used when changing these files. 

The general process for deployment of non-Git content is:

1. Update the non-jekyll files as necessary on the staging server under `/var/www/documents`.
2. Test the results, ideally asking someone else to verify the changes.
3. Sync `/var/www/documents` with the master website at `/volumes/webserver_assets`.
4. Deploy the master website to the production servers.

How you update the files on staging will depend on exactly what needs to be done and won’t be discussed here.

To sync the local `/var/www/documents` with `/volumes/webserver_assets`:

  ```
  cd ~webmaster/pds-website/deploy
  ./deploy_staging_to_master.sh
  ```

Then to sync `/volumes/webserver_assets` to the production servers:

  ```
  ./deploy_master_to_production.sh
  ```
