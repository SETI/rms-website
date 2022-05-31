#!/usr/bin/bash
source config_data
echo "You will be deploying the master website in ${MASTER_DIR}"
echo "to the website servers at"
echo "${SERVER1_HOST} and ${SERVER2_HOST}."
echo "The master website WILL NOT be updated with the current contents of the"
echo "pds-website repo."
echo
read -p "Do you want to continue? [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
sudo rsync -av --checksum _site/ ${MASTER_DIR}
echo "Updating ownership (takes awhile)"
sudo chown -R webmaster:www-data ${MASTER_DIR}
echo "Updating permissions (takes awhile)"
sudo chmod -R g+w ${MASTER_DIR}
echo "The above was a list of differences."
echo
echo "Dry run..."
echo
ssh ${WEBMASTER_USERNAME}@${SERVER1_HOST} "rsync -avn ${MASTER_DIR}/ ${WEBROOT_DIR}"
echo
read -p "If it looks good, copy to production sites: [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
echo Updating ${SERVER1_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER1_HOST} "rsync -av ${MASTER_DIR}/ ${WEBROOT_DIR}"
echo
echo Updating ${SERVER2_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER2_HOST} "rsync -av ${MASTER_DIR}/ ${WEBROOT_DIR}"
echo
echo "*** Production servers have been updated! ***"
