#!/bin/bash

# This script removes existing bare repository to the server and notifies replicas
# Usage: ./delete_repo.sh REPO_NAME
#
# Example: ./delete_repo.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPO_NAME=$1

# delete bare repo
$CURR_FLDR/../repo_tools/delete_bare_repo.sh $REPO_NAME
# send message
python $CURR_FLDR/../messaging/send.py delete $REPO_NAME
