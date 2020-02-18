#!/bin/bash

#
# setup script for Ubuntu 16 server
# this script configures the following:
#   1. apache2 web server
#   2. git protocol on the server
#   3. http protocol on the server with simple authentication
#

# update and install basic software
sudo apt update -y
sudo apt install git -y
sudo apt install apache2 apache2-utils -y
sudo a2enmod cgi alias env

# initially start apache server
sudo service apache2 start

# utility variables:
GIT_FLDR=/var/www/html/git/
CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# create git folder
sudo mkdir -p $GIT_FLDR

# setup git user - TODO?
sudo adduser git
# ...
sudo chown -R git:www-data $GIT_FLDR

# add git daemon
sudo cp $CURR_FLDR/git-daemon.service /etc/systemd/system/git-daemon.service
sudo systemctl enable git-daemon
sudo systemctl start git-daemon

# enable HTTP for apache server
cat $CURR_FLDR/add_to_apache2.conf >> /etc/apache2/apache2.conf
echo "do: 'htpasswd -c $GIT_FLDR/.htpasswd <user>' to add new user to HTTP valid users"

# add GitWeb
cd ~
git clone git://git.kernel.org/pub/scm/git/git.git
cd git/
make GITWEB_PROJECTROOT="/var/www/html/git" prefix=/usr gitweb
sudo cp -Rf gitweb /var/www/

# reload apache2 server
sudo service apache2 reload

echo "  for smart HTTP do:"
echo "'htpasswd -c $GIT_FLDR/.htpasswd <user>'"
echo "  to add new user to HTTP valid users"

echo "Now you can start adding bare repositories to the webserver inside the $GIT_FLDR folder"
