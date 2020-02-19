#!/bin/bash

# This script mirrors repository from the known server via HTTP
# Usage: ./make_bare_repo.sh HTTP_URL REPO_NAME

HTTP_URL=$1
# TODO: make it simpler. can parse REPO_NAME from URL
REPO_NAME=$2
cd /var/www/html/git/
sudo git clone --mirror $HTTP_URL $REPO_NAME
# for git protocol:
sudo touch $REPO_NAME/git-daemon-export-ok
cd - > /dev/null
sudo chown -R git:www-data /var/www/html/git/$REPO_NAME

