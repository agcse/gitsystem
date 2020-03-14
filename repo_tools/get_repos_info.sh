#!/bin/bash

# This script notifies main server to send all repos info to replica server
# Usage: ./get_repos_info.sh 
#
# REPLICA_NODE is the name of the channel for kafka

CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# send message
python $CURR_FLDR/../messaging/send.py --channel REPLICA_NODE get_repos 
