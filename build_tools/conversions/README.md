
dry run:	
	
	python converter.py 

copy all files and folders to new directory, ignoring some cruft:
	
	python converter.py deep_copy

convert all html files to markdown and copy those to new directory
(also ignoring some cruft)

	python converter.py html_to_md


then when ur happy: 

cp -r  ~/projects/ringsnode_website/converted_markdown/ ~/projects/ringsnode_website/website
