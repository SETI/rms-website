#!/usr/bin/bash
source config_data
echo "You will be deploying the website from the staging server"
echo "generated in ${STAGING_REPO}"
echo "to the website servers at"
echo "${SERVER1_HOST} and ${SERVER2_HOST}."
echo
read -p "Do you want to continue? [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
cd ~/pds-website/website
echo "--- START DIFFS ---"
diff -rq _site ${MASTER_DIR} | grep -v "Only in ${MASTER_DIR}" | grep -v "Common subdirectories"
echo "--- END DIFFS ---"
echo "The above was a list of differences."
read -p "If it looks good, push to production sites: [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
sudo rsync -av ${EXCLUDE} --checksum _site/ ${MASTER_DIR}
if [ $? -ne 0 ]; then exit -1; fi
echo "Updating ownership (takes awhile)"
sudo chown -R webmaster:www-data ${MASTER_DIR}
echo "Updating permissions (takes awhile)"
sudo chmod -R g+w ${MASTER_DIR}
echo
echo "*** Master directory has been updated! ***"
echo
echo Updating ${SERVER1_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER1_HOST} "rsync -av ${EXCLUDE} ${MASTER_DIR}/ ${WEBROOT_DIR}"
if [ $? -ne 0 ]; then exit -1; fi
echo
echo Updating ${SERVER2_HOST} ...
ssh ${WEBMASTER_USERNAME}@${SERVER2_HOST} "rsync -av ${EXCLUDE} ${MASTER_DIR}/ ${WEBROOT_DIR}"
if [ $? -ne 0 ]; then exit -1; fi
echo
echo "*** Production servers have been updated! ***"
