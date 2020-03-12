#!/bin/bash

# This script deletes existing bare repository from the server
# Usage: ./delete_bare_repo.sh REPO_NAME
#
# Example: ./delete_bare_repo.sh <repo>.git
#          <repo> is the repository name (e.g. my_best_repo)

REPO_NAME=$1
rm -rf /var/www/html/git/$REPO_NAME
