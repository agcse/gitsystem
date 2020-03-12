#!/bin/bash

# This script adds new bare repository to the server and notifies replicas
# Usage: ./create_repo.sh REPO_NAME
#
# Example: ./create_repo.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPO_NAME=$1

# make bare repo
$CURR_FLDR/../repo_tools/make_bare_repo.sh $REPO_NAME.git
# send message
python $CURR_FLDR/../messaging/send.py new $(hosname -I) $REPO_NAME.git
