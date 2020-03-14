#!/bin/bash

# This script notifies replicas about the repos on main server
# Usage: ./send_repos_info.sh REPOS_NAME
#  
# Example: ./send_repo_info.sh [<repo>.git]
#          <repo> is the repository name (e.g. [my_best_repo])
#
# REPLICA_NODE is the name of the kafka channel

CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
REPOS_NAME=$1
HOST=$(hostname -I)

# send message
python $CURR_FLDR/../messaging/send.py --channel REPLICA_NODE setup_repos $HOST $REPOS_NAME
