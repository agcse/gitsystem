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


SUPPORTED_COMMANDS = ['SETUP_REPOS']


def parse_args():
    """Parse command-line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('message', help='Serialized command message')
    return parser.parse_args()


def interpret_as_setup_repos(args):
    def make_full_git_url(
        src, repo_name): return src + '/' + repo_name
    command = {
        'type': args['type'],
        'repos': args['repos']
    }

    for repo in command['repos']:
        src = make_full_git_url(args['src'], repo)
        subprocess.check_call(
        "/var/www/git_tools/repo_tools/mirror_repo.sh %s %s" %
        (str(
            src), str(
            repo)), shell=True)

    

    return command



def deserialize_command(args):
    d = json.loads(args)
    command_type = d['type']
    if command_type not in SUPPORTED_COMMANDS:
        raise Exception('invalid command ' + d.command +
                        '. expected one of ' + str(SUPPORTED_COMMANDS))

    if command_type == 'SETUP_REPOS':
        return interpret_as_setup_repos(d)

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
