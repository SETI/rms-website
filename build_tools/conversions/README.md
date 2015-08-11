
dry run:	
	
	python converter.py 

copy all files and folders to new directory, ignoring some cruft:
	
	python converter.py deep_copy

convert all html files to markdown and copy those to new directory
(also ignoring some cruft)

	python converter.py html_to_md


then copy this directory structure into the website folder

cp -r  ~/projects/ringsnode_website/converted_markdown/ ~/projects/ringsnode_website/website
