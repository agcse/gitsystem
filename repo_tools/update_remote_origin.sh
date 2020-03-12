#!/bin/bash

# This script updates remote origin of the repository on the server
# Usage: ./update_remote_origin.sh REPO_NAME NEW_ORIGIN_URL
#
# Example: ./update_remote_origin.sh <repo>.git <new_origin>
#          <repo> is the repository name (e.g. my_best_repo)
#          <new_origin> is the new origin url (e.g. git://my_server.com)

REPO_NAME=$1
NEW_ORIGIN=$2
REPO_PATH=/var/www/html/git/$REPO_NAME
cd $REPO_PATH
#TODO git remote should not be here but it is. usage: main node demoted to replica
git remote add origin git://non-existent.com/non_existent.git
git remote set-url origin $NEW_ORIGIN
cd - > /dev/null
