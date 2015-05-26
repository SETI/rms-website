Local deployment: 

## navigate to here: 

    cd ~/sites/ringsnode/
    python -m SimpleHTTPServer 8000

## then load this in browser: 

    http://lisas-mbp:8000/


To watch local changes:

	cd ~/projects/ringsnode_website/website/


first edit the _config.yml for what directory you want to work on.
remove the directory name from the 'excludes' list: 

	subl config.yml


Then in one tab start auto-building the website:
	
	jekyll build --watch


And in another start rsyncing that build to local deployment directory: 

	while :; do clear; rsync -a -v _site/ /Users/lballard/sites/ringsnode; sleep 2; done

but make sure before doing that rsync on repeate that you've done the full rsync at least once: 
	
	rsync -a -v _site/ /Users/lballard/sites/ringsnode




