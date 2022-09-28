#!/usr/bin/bash
source config_data
branch=${1:-master}
echo "### Deploying pds-website repo, branch ${branch}, to staging server"
cd ~/pds-website
git checkout $branch
if [ $? -ne 0 ]; then exit -1; fi
git pull
if [ $? -ne 0 ]; then exit -1; fi
umask 002
cd website
jekyll build --config _config.yml,_config.production.yml
if [ $? -ne 0 ]; then exit -1; fi
echo '--- START DIFFS ---'
diff -rq _site ${WEBROOT_DIR} | grep -v "Only in ${WEBROOT_DIR}" | grep -v "Common subdirectories"
echo '--- END DIFFS ---'
echo 'The above was a list of differences.'
read -p 'If it looks good, push to staging site: [Y/n]' confirm
if [ x$confirm != 'xY' ] && [ x$confirm != 'x' ] && [ x$confirm != 'xy' ]
then
  exit 0
fi
rsync -av --checksum _site/ ${WEBROOT_DIR}
if [ $? -ne 0 ]; then exit -1; fi
#sudo chown -R webmaster:www-data ${WEBROOT_DIR}
#sudo chmod -R g+w ${WEBROOT_DIR}
echo "*** Staging website has been updated! ***"
echo Take a look: ${STAGING_WEBSITE}
