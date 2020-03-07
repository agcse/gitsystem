#!/usr/bin/env python

'''
Script that fakes the sending of a repo-related message.
'''

import argparse
import json


def git_repo_name(s):
    if not s.endswith('.git'):
        msg = 'invalid repo name format: ' + s + '. must end with .git'
        raise argparse.ArgumentTypeError(msg)
    return s


def ip(s):
    parts = [int(e) for e in s.strip().split('.')]
    if len(parts) != 4:
        msg = 'invalid IP format: ' + s + '. must consist of 4 integer values'
        raise argparse.ArgumentTypeError(msg)
    return s


def parse_args():
    """Parse command-line"""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='Send message commands')

    # add commands for each type of message
    # add new repo:
    parser_new = subparsers.add_parser(
        'new', help='Send message that a new repository is created')
    parser_new.add_argument(
        'ip', help='IP address of a source of the repository', type=ip)
    parser_new.add_argument(
        'repo_name', help='Name of the new repository (must end to .git)', type=git_repo_name)
    parser_new.set_defaults(command='NEW')

    # delete old repo:
    parser_delete = subparsers.add_parser(
        'delete', help='Send message that repository is deleted')
    parser_delete.add_argument(
        'repo_name', help='Name of the repository to be deleted', type=git_repo_name)
    parser_delete.set_defaults(command='DELETE')

    # update current repo:
    parser_update = subparsers.add_parser(
        'update', help='Send message that an existing repository is updated')
    parser_update.add_argument(
        'repo_name', help='Name of the repository to update', type=git_repo_name)
    parser_update.set_defaults(command='UPDATE')

    return parser.parse_args()


def interpret_as_new(args):
    def make_git_ip(ip): return 'http://' + ip + '/git/'
    message = {
        'type': args.command,
        'src': make_git_ip(args.ip),
        'repo': args.repo_name
    }
    return message


def interpret_as_delete(args):
    message = {
        'type': args.command,
        'repo': args.repo_name
    }
    return message


def interpret_as_update(args):
    message = {
        'type': args.command,
        'repo': args.repo_name
    }
    return message


def serialize_command(args):
    def wrap(s): return json.dumps(s)  # json based serializer

    if args.command == 'NEW':
        return wrap(interpret_as_new(args))
    if args.command == 'DELETE':
        return wrap(interpret_as_delete(args))
    if args.command == 'UPDATE':
        return wrap(interpret_as_update(args))
    return None


def main():
    args = parse_args()
    serialized = serialize_command(args)
    print('Serialized command message: ' + serialized)
    return


if __name__ == '__main__':
    main()
