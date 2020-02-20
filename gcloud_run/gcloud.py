#!/usr/bin/env python3

import click
import docker
import dockerpty
import sys
import pwd
import getpass
import os
from pathlib import Path
import sys

def start_container(client, image, name, uid, gid, config_dir, home, cmd):

    """
    Start container
    """

    host_config = client.create_host_config(binds={config_dir: {'bind': config_dir, 'mode': 'rw'}})

    container = client.create_container(
                    image,
                    name=name,
                    user=f'{uid}:{gid}',
                    environment={'HOME':home},
                    volumes=[config_dir],
                    command=cmd,
                    tty=True,
                    stdin_open=True,
                    host_config=host_config
                )

    dockerpty.start(client, container)

    client.remove_container(container, force=True)

@click.command()
@click.option('-s', '--docker-socket', 'docker_socket', default='unix://var/run/docker.sock')
@click.argument('args', nargs=-1)
def run(args, docker_socket):
    """Example CLI app"""


    home = str(Path.home())
    client = docker.APIClient(base_url=docker_socket)
    uid = int(pwd.getpwnam(getpass.getuser()).pw_uid)
    gid = int(pwd.getpwnam(getpass.getuser()).pw_gid)
    app = (Path(sys.argv[0]).name)
    cmd = f'{app} {" ".join(args)}'


    if app == 'gcloud':
        config_dir = f'{home}/.config/gcloud'
    elif app == 'kubectl':
        config_dir = f'{home}/.kube'

    start_container(client, 'google/cloud-sdk:latest', app, uid, gid, config_dir, home, cmd)

if __name__ == '__main__':
    run()
