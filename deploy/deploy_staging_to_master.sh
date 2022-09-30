#!/usr/bin/bash
source config_data
echo "You will be deploying the staging website in ${WEBROOT_DIR}"
echo "to the master website at ${MASTER_DIR}."
echo
read -p "Do you want to continue? [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
echo "Dry run..."
echo
rsync -avn ${EXCLUDE} ${WEBROOT_DIR}/ ${MASTER_DIR}
if [ $? -ne 0 ]; then exit -1; fi
echo
read -p "If it looks good, copy to master: [Y/n]" confirm
if [ x$confirm != "xY" ] && [ x$confirm != "x" ] && [ x$confirm != "xy" ]
then
  exit 0
fi
rsync -av ${EXCLUDE} ${WEBROOT_DIR}/ ${MASTER_DIR}
echo "*** Master website directory has been updated! ***"
