# Generating the Browse Pages

python script spiders directory and builds index.md files files for jekyll,
then moves them into the correct directory to appear on the website

directory navigation for web pages is simplified, does not depend to path to image'
ie:

  COISS_2xxx
    - COISS_2011
      - sub_directories
        <list of all jpegs>

Should be added to Fabric deployment script so gets run every time
(or optional to run at deployment)
and/or put it on cron/Celery

# todo

this adds a new directory to the web root
add a line for this in the _config.yml (a 'work on' line because this directory is big)
