#!/bin/bash

# This script update mirror repository on the server
# Usage: ./make_bare_repo.sh REPO_NAME

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
cd $REPO_PATH
sudo git remote update
cd - > /dev/null
sudo chown -R git:www-data $REPO_PATH

