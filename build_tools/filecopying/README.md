copy old directory structure and all media files to new structure

	# copy the directory from the old site to an empty directory
	mkdir ~/test_site_struct/website 
	cp -r original_site/ ~/test_site_struct/website


	# may be more.. 

	# get rid of somebody's editor cruft
	website/cassini/*/*.*~  # and more recursive

	# now copy in the converted markdown files into same dir struct
	cp -r converted_markdown/cassini/  ~/test_site_struct/website/cassini

	# and copy that into repo
	cp -r ~/test_site_struct/website/cassini/ website/cassini


--- 
a scripty way?

http://stackoverflow.com/questions/27792008/python-create-recursive-folder-structure


---
