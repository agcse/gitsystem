#!/bin/bash

# This script mirrors repository from the known server via HTTP
# Usage: ./mirror_repo.sh HTTP_URL REPO_NAME
#
# Example: ./mirror_repo.sh http://<server>/git/<repo>.git <repo>.git
#          <server> is the server IP (e.g. 1.2.3.4) or URL (e.g. my_server.com)
#          <repo> is the repository name (e.g. my_best_repo)

HTTP_URL=$1
# TODO: make it simpler. can parse REPO_NAME from URL
REPO_NAME=$2
cd /var/www/html/git/
git clone --mirror $HTTP_URL $REPO_NAME
# for git protocol:
touch $REPO_NAME/git-daemon-export-ok
cd - > /dev/null
