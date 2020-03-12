#!/bin/bash

# This script registers new user notifies replicas
# Usage: ./register_user.sh USER_NAME USER_PASSWORD
#
# Example: ./register_user.sh <name> <password>

CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
USER_NAME=$1
USER_PASSWORD=$2

# add new credentials
htpasswd -b /var/www/html/git/.htpasswd $USER_NAME $USER_PASSWORD
# send message
python $CURR_FLDR/../messaging/send.py update_pwds
