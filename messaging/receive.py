#!/usr/bin/env python

'''
Script that fakes the sending of a repo-related message.
'''

import argparse
import json


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
    args = parse_args()
    deserialized = deserialize_command(args.message)
    print('Deserialized command message: ' + str(deserialized))
    return


if __name__ == '__main__':
    main()
