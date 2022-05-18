#!/usr/bin/bash
source config_data
branch=${1:master}
cd ~/pds-website
git checkout $branch
git pull
umask 002
jekyll build --config _config.yml,_config.production.yml
echo '--- START DIFFS ---'
diff -rq _site ${WEBROOT_DIR} | grep -v "Only in ${WEBROOT_DIR}" | grep -v "Common subdirectories"
echo '--- END DIFFS ---'
echo 'The above was a list of differences.'
read -p 'If it looks good, push to staging site: [Y/n]' confirm
if [[ $confirm -ne 'Y' ]] || [[ $confirm -ne '']]; then
  exit 0
sudo rsync -av --checksum _site/ ${WEBROOT_DIR}
sudo chown -R webmaster:www-data ${WEBROOT_DIR}
sudo chmod -R g+w ${WEBROOT_DIR}
