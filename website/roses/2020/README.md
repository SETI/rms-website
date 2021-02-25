The current year files are kept in the base directory roses/
For current year use mod_rewrite so they also appear in a YYYY subdirectory, something like:

Redirect 302 /roses/2016/*.html /roses/*.html

(issue a 302 since it will change in one year) 

Every year you will archive the current year and start a new.. 

to update the main pages move the previous year into its own directory and update the rewrite rule for the next year.. 

You will also have to update the navigation tabs for the year too, as they will will have been pointing to the base diretory and you now want them to point to /roses/YYYY/... 

For example when you want to go archive 2016 in prep for new pages for 2017, move all the html files at roses/*.html into roses/2016/*.html then open _data/tabs/roses_2016.yaml and make those links point into the roses/2016/ directory.. 






