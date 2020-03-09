#!/usr/bin/env python

'''
Script that fakes the sending of a repo-related message.
'''

import argparse
import json
from kafka import KafkaConsumer
from json import loads
import subprocess


SUPPORTED_COMMANDS = ['NEW', 'DELETE', 'UPDATE']


def parse_args():
    """Parse command-line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('message', help='Serialized command message')
    return parser.parse_args()


def interpret_as_new(args):
    # TODO: add actual logic
    def make_full_git_url(src, repo_name): return src + '/' + repo_name
    command = {
        'type': args['type'],
        'src': make_full_git_url(args['src'], args['repo_name']),
        'repo_name': args['repo_name']
    }

    subprocess.check_call("../repo_tools/./mirror_repo.sh %s %s" % (str(command['src']), str(command['repo_name'])),   shell=True)

    return command


def interpret_as_delete(args):
    # TODO: add actual logic
    command = {
        'type': args['type'],
        'repo_name': args['repo_name']
    }
    return command


def interpret_as_update(args):
    # TODO: add actual logic
    command = {
        'type': args['type'],
        'repo_name': args['repo_name']
    }
    
    subprocess.check_call("../repo_tools/./update_mirror.sh %s" % (str(command['repo_name'])),   shell=True)
    return command


def deserialize_command(args):
    d = json.loads(args)
    command_type = d['type']
    if command_type not in SUPPORTED_COMMANDS:
        raise Exception('invalid command ' + d.command +
                        '. expected one of ' + str(SUPPORTED_COMMANDS))

    if command_type == 'NEW':
        return interpret_as_new(d)
    if command_type == 'DELETE':
        return interpret_as_delete(d)
    if command_type == 'UPDATE':
        return interpret_as_update(d)

    return None


def main():
    #Change the ip to your kafka server ip adress
    #Change MAIN_NODE to the topic you created on kafka server
    consumer = KafkaConsumer(
        'MAIN_NODE',
        bootstrap_servers=['10.0.2.6:9092'],
        auto_offset_reset='latest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))


    for message in consumer:
        cMsg = message.value
        deserialized = deserialize_command(cMsg['msg'])
        print('Deserialized command message: ' + str(deserialized))


	'''
    args = parse_args()
    deserialized = deserialize_command(args.message)
    print('Deserialized command message: ' + str(deserialized))
    return
	'''

if __name__ == '__main__':
    main()
