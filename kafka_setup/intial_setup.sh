#!/bin/bash

sudo apt install default-jre

mkdir kafkaServer
cd ./kafkaServer

wget http://mirror.netinch.com/pub/apache/kafka/2.4.0/kafka_2.12-2.4.0.tgz

tar -xzf kafka_2.12-2.4.0.tgz
cd kafka_2.12-2.4.0


