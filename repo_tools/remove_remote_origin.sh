#!/bin/bash

# This script removes remote origin of the repository on the server
# Usage: ./remove_remote_origin.sh REPO_NAME
#
# Example: ./remove_remote_origin.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
cd $REPO_PATH
git remote remove origin
cd - > /dev/null
