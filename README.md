# gitsystem

Repository of scripts and tools to deploy your own Git-based system.

## Contents

```
Tree:
server_bootstrap/ - bootstrap scripts for the apache2 web server running git backend through smart HTTP/GIT protocols
repo_tools/ - tools to aid with repositories on the server
```

## Fast start

* You can fast start on Ubuntu server with the following:
```sh
sudo apt-get install git
git clone https://github.com/agcse/gitsystem.git
cd gitsystem/server_bootstrap/
./setup_server.sh  # uses sudo inside
```
* To enable smart HTTP you need "valid" users. In the current setting, you can add new user on the server via:
```sh
sudo htpasswd -c /var/www/html/git/.htpasswd <user>
```
* GIT protocol (clone-only) is enabled by the setup routine.
* After a successful setup, you could see GitWeb app running on `http(s)://<server>/gitweb` url

## Managing repositories

You can find multiple scripts in [repo_tools](./repo_tools/) useful when managing repositories on the server

## Cloning from your server

There are several ways to be able to clone repositories from the server:
> Note: different protocols might have different pattern for valid git `<url>` (e.g. compare Smart HTTP and GIT)
* Smart HTTP: `git clone http(s)://<server>/git/<repo>.git`
* GIT: `git clone git://<server>/<repo>.git`

## Notes

Tested on local virtual machines; OS: Ubuntu 16.04 LTS 64-bit
