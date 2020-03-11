#!/bin/bash

# This script adds new bare repository to the server
# Usage: ./make_bare_repo.sh REPO_NAME
#
# Example: ./make_bare_repo.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
mkdir -p $REPO_PATH
cd $REPO_PATH
git init --bare --shared
# for git protocol:
touch git-daemon-export-ok
cd - > /dev/null
