#!/bin/bash

#
# setup script for Ubuntu 16 server
# this script configures the following:
#   1. apache2 web server
#   2. git protocol on the server
#   3. http protocol on the server with simple authentication
#

# update and install basic software
sudo add-apt-repository ppa:ondrej/php
sudo apt update -y
sudo apt install git vim -y
sudo apt install apache2 apache2-utils libapache2-mod-php -y
sudo a2enmod cgi alias env php*

# initially start apache server
sudo service apache2 start

# utility variables:
GIT_FLDR=/var/www/html/git/
CURR_FLDR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# create git folder
sudo mkdir -p $GIT_FLDR

# add git user
sudo adduser git

# add git and www-data to this user's group. this will enable git and www-data to access files
# created by current user
sudo usermod -a -G $(whoami) git
sudo usermod -a -G $(whoami) www-data
# add user to www-data group (for later stuff with creating repos through website)
sudo usermod -a -G www-data $(whoami)

# add git daemon
sudo cp $CURR_FLDR/git-daemon.service /etc/systemd/system/git-daemon.service
sudo systemctl enable git-daemon
sudo systemctl start git-daemon

# enable HTTP for apache server
cat $CURR_FLDR/add_to_apache2.conf | sudo tee -a /etc/apache2/apache2.conf

# add GitWeb
cd ~
git clone git://git.kernel.org/pub/scm/git/git.git
cd ~/git/
make GITWEB_PROJECTROOT="/var/www/html/git" prefix=/usr gitweb
sudo cp -Rf gitweb /var/www/
sudo chown -R www-data:www-data /var/www/gitweb/

# add GitWeb to server sub-url
cat $CURR_FLDR/replace_000-default.conf | sudo tee /etc/apache2/sites-available/000-default.conf

# reload apache2 server
sudo service apache2 reload

# some additional stuff for Git:
git config --global http.receivepack true

# reload apache2 server
sudo service apache2 reload

# copy gitsystem local files to web server
sudo mkdir -p /var/www/git_tools/
sudo cp -r $CURR_FLDR/../repo_tools/ /var/www/git_tools/
sudo cp -r $CURR_FLDR/../messaging/ /var/www/git_tools/
sudo cp -r $CURR_FLDR/../server_tools/ /var/www/git_tools/
sudo chown -R $(whoami):$(whoami) /var/www/git_tools/

# create .htpasswd
sudo touch /var/www/html/git/.htpasswd
sudo chmod 660 /var/www/html/git/.htpasswd

# delete index.html and copy index.php to web server
sudo rm -f /var/www/html/index.html
sudo cp $CURR_FLDR/index.php /var/www/html/index.php
sudo chown -R $(whoami):$(whoami) /var/www/html/index.php

# change permissions of git folder and add group id bit:
sudo chown -R www-data:$(whoami) $GIT_FLDR
sudo chmod 774 $GIT_FLDR
sudo chmod g+s $GIT_FLDR

# install python, python-pip and kafka-python
sudo apt install python python-pip -y
sudo pip install kafka-python

echo "  for smart HTTP do:"
echo "'htpasswd $GIT_FLDR/.htpasswd <user>'"
echo "  to add new user to HTTP valid users"

echo "Now you can start adding bare repositories to the webserver inside the $GIT_FLDR folder"
