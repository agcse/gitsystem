#!/bin/bash

# This script adds repository hooks
# Usage: ./add_hooks.sh REPO_NAME
#
# Example: ./add_hooks.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
REPO_PATH=/var/www/html/git/$REPO_NAME
CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cp -r $CURR_FLDR/hooks/ $REPO_PATH/
