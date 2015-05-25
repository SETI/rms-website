you can't use jekyll server
you have to deploy it locally
over and on top of the rest of the site that is not in the repo and not in jekyll

jekyll build --watch --destination <destination> keep_files: [DIR, FILE]

or jekyll build in _site and then rsync? 

there is complete backup of working site in ~/backups


# to serve: 
## navigate to here: 

    cd ~/sites/ringsnode/
    python -m SimpleHTTPServer 8000

## then load this in browser: 

    http://lisas-mbp:8000/
