#!/usr/bin/env python

'''
Script that receives repo-related messages through Kafka.
'''

import argparse
import json
from json import loads
import subprocess
import os
import sys


SUPPORTED_COMMANDS = ['GET_REPOS']


def parse_args():
    """Parse command-line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('message', help='Serialized command message')
    return parser.parse_args()


def interpret_as_get_repos():

    command = {
        'type': args['type']
    }
    
    repoList = []

    for repo in [e for e in os.listdir(
            '/var/www/html/git/') if e.endswith('.git')]:
        repoList.append(e)

    
    subprocess.check_call(
        "../repo_tools/send_repos_info.sh %s" %
        (str(
            repoList)), shell=True)

    return command



def deserialize_command(args):
    d = json.loads(args)
    command_type = d['type']
    if command_type not in SUPPORTED_COMMANDS:
        raise Exception('invalid command ' + d.command +
                        '. expected one of ' + str(SUPPORTED_COMMANDS))

    if command_type == 'GET_REPOS':
        return interpret_as_get_repos(d)

    return None


def main():

    from kafka import KafkaConsumer
    # Change the ip to your kafka server ip adress
    # Change REPLICA_NODE to the topic you created on kafka server
    consumer = KafkaConsumer(
        'REPLICA_NODE',
        bootstrap_servers=['10.0.2.6:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        try:
            cMsg = message.value
            deserialized = deserialize_command(cMsg['msg'])
            print('Deserialized command message: ' +
                  str(deserialized))
        except Exception as e:
            print('Error happened:')
            print(str(e))

if __name__ == '__main__':
    main()
