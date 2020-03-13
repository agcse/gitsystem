#!/bin/bash

# This script adds new bare repository to the server
# Usage: ./make_bare_repo.sh REPO_NAME
#
# Example: ./make_bare_repo.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

mkdir -p $REPO_PATH
cd $REPO_PATH
git init --bare --shared

# enable git protocol:
touch git-daemon-export-ok

# enable hooks for timely updates:
$CURR_FLDR/add_hooks.sh $REPO_NAME

cd - > /dev/null
