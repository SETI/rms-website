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
echo "Updating ownership (takes awhile)"
echo "(If asked for password, it is for the staging server)"
sudo chown -R webmaster:www-data ${MASTER_DIR}
if [ $? -ne 0 ]; then exit -1; fi
echo "Updating permissions (takes awhile)"
sudo chmod -R g+w ${MASTER_DIR}
if [ $? -ne 0 ]; then exit -1; fi
echo
echo "Dry run..."
echo
ssh ${WEBMASTER_USERNAME}@${SERVER1_HOST} "rsync -avn ${EXCLUDE} ${MASTER_DIR}/ ${WEBROOT_DIR}"
if [ $? -ne 0 ]; then exit -1; fi
echo
echo "The above was a list of differences on ${SERVER1_HOST}."
echo
read -p "If it looks good, copy to production sites: [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
echo Updating ${SERVER1_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER1_HOST} "rsync -av ${EXCLUDE} ${MASTER_DIR}/ ${WEBROOT_DIR}"
if [ $? -ne 0 ]; then exit -1; fi
echo
echo Updating ${SERVER2_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER2_HOST} "rsync -av ${EXCLUDE} ${MASTER_DIR}/ ${WEBROOT_DIR}"
if [ $? -ne 0 ]; then exit -1; fi
echo
echo "*** Production servers have been updated! ***"
