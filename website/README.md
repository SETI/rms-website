## Local deployment:

You will need 3 shell windows/tabs running 3 processes:

1. run a small local web server with python SimpleHTTPServer
- run the jekyll watch command
- rsync the site built by jekyll (2) into the directory served by python (1)

### Details:

1. Navigate to the directory where you have a copy of the current website  which includes all its image assets and start the SimpleHTTTPServer on port 8000. For example I keep this in ~/sites/ringsnode:

        cd ~/sites/ringsnode/
        python -m SimpleHTTPServer 8000

	Then load this in a browser:

    	http://127.0.0.1:8000


2. Tell Jekyll to start watching local changes. First open and edit the _config.yml for what directory you want to work on. Then in the jekyll website directory issue the jekyll build --watch command:

        cd ~/projects/ringsnode_website/website/
        jekyll build --watch


3. In another tab, in the same directory as step 2, start rsyncing that jekyll build directory to the local deployment directory served by SimpleHTTPServer (see __Note__ below)

	__On a Mac__:

        while :; do clear; rsync -a -v _site/ /Users/lballard/sites/ringsnode; sleep 2; done

	In __Linux__ you have the watch command:

		watch -n 2 rsync -a -v _site/ /Users/lballard/sites/ringsnode

	In __Windows__ try something like this: write a small batch file, call it rsyncer.bat

		@ECHO OFF
		:loop
		  rsync -a -v _site/ /Users/lballard/sites/ringsnode;
		  timeout /t 2
		goto loop

	then run it like so:

		rsyncer

__Note:__ Before doing step 3 putting that rsync on repeat, make sure you've done the full rsync at least once:

	rsync -a -v _site/ /Users/lballard/sites/ringsnode


To run a simple DEBUG envinroment on windows:
You will need 2 shell windows:
1) cd website
   jekyll build --watch

2) cd website\_site
   python -m http.server 4000   <or whatever socket you prefer>
