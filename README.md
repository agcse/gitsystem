# gitsystem

Repository of scripts and tools to deploy your own Git-based system.

## Contents

```
Tree:
server_bootstrap/ - bootstrap scripts for the apache2 web server running git backend through smart HTTP/GIT protocols
repo_tools/ - tools to aid with repositories on the server
messaging/ - tools to aid with messaging between git servers
server_tools/ - tools that the web server uses
kafka_setup/ - setup and startup scripts for Kafka server
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

## Kafka Server
Following are the instructions to setup kafka server for nodes communication

* Run intial_setup.sh in your home directory by 
```sh
. intial_setup.sh
```
* In config/server.properties uncomment and change
```sh
listeners=PLAINTEXT://<Machine ip adress>:9092

advertised.listeners=PLAINTEXT://<Machine ip adress>:9092
```
* Assuming your kafkaserver folder is in home directory, change logs.dir in config/server.properties to
```sh
logs.dir = /home/<user name>/kafkaServer/kafka_2.12-2.4.0/kafka-logs
```
* Assuming your kafkaserver folder is in home directory, change dataDir in config/zookeeper.properties to
```sh
dataDir = /home/<user name>/kafkaServer/kafka_2.12-2.4.0/zookeeper
```
* In kafkaServer/kafka_2.12-2.4.0/ run 
```sh
start_zookeeper.sh to start zookeeper
start_kafkaServer.sh to start kafkaServer
```
* After zookeeper and kafka server are running you can create the topic
```sh
bin/kafka-topics.sh --create --bootstrap-server <Machine_ip>:9092 --replication-factor 1 --partitions 1 --topic <topic>
```
* To check if topic is created
```sh
bin/kafka-topics.sh --list --bootstrap-server <Machine_ip>:9092
```

## Kafka Nodes

* On each node we need kafka python 
```sh
//If pip is not installed
sudo apt install python-pip
pip install kafka-python
```

## Notes

Tested on local virtual machines; OS: Ubuntu 16.04 LTS 64-bit
