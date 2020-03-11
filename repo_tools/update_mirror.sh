#!/bin/bash

# This script updates mirror repository on the server
# Usage: ./update_mirror.sh REPO_NAME
#
# Example: ./update_mirror.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
cd $REPO_PATH
git remote update
cd - > /dev/null
