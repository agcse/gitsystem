#!/usr/bin/env python

'''
Script that sends repo-related messages through Kafka.
'''

import argparse
import json
from json import dumps


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
    parser.add_argument(
        '--test', help='Run script in "test" mode (only print serialized message)',
        default=False, action='store_true')

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

    # change main server:
    parser_chsrv = subparsers.add_parser(
        'change_server', help='Send message that the main server must be changed')
    parser_chsrv.add_argument(
        'ip', help='IP address of a new main server')
    parser_chsrv.set_defaults(command='CHANGE_SERVER')

    # change main server:
    parser_upd_pwds = subparsers.add_parser(
        'update_pwds', help='Send message that the .htpasswd file needs to be updated')
    parser_upd_pwds.set_defaults(command='UPDATE_PWDS')

    return parser.parse_args()


def make_git_url(ip):
    """Make Git URL from IP address"""
    return 'git://' + ip


def interpret_as_new(args):
    message = {
        'type': args.command,
        'src': make_git_url(args.ip),
        'repo_name': args.repo_name
    }
    return message


def interpret_as_delete(args):
    message = {
        'type': args.command,
        'repo_name': args.repo_name
    }
    return message


def interpret_as_update(args):
    message = {
        'type': args.command,
        'repo_name': args.repo_name
    }
    return message


def interpret_as_change_server(args):
    message = {
        'type': args.command,
        'src': make_git_url(args.ip)
    }
    return message


def interpret_as_update_pwds(args):
    htpasswd_content = None
    with open('/var/www/html/git/.htpasswd', 'r') as pwd_file:
        htpasswd_content = pwd_file.read()

    message = {
        'type': args.command,
        'content': htpasswd_content
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
    if args.command == 'CHANGE_SERVER':
        return wrap(interpret_as_change_server(args))
    if args.command == 'UPDATE_PWDS':
        return wrap(interpret_as_update_pwds(args))
    return None


def main():
    args = parse_args()
    serialized = serialize_command(args)
    data = {'msg': serialized}
    print(data)

    # do not send message in case of --test option
    if args.test:
        return

    from kafka import KafkaProducer

    # Change the ip to your kafka server ip
    producer = KafkaProducer(bootstrap_servers=['10.0.2.6:9092'],
                             value_serializer=lambda x:
                             dumps(x).encode('utf-8'))

    # MAIN_NODE is the topic, Change it to the topic you created on
    # kafka
    producer.send('MAIN_NODE', value=data)

    return


if __name__ == '__main__':
    main()
