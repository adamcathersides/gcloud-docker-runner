#!/usr/bin/env python3

import click
import docker
import logging
import sys
import pwd
import getpass
from pathlib import Path


def start_container(client, image, name, uid, config_dir, home, cmd):

    """
    Start container
    """

    container = client.containers.run(
                    image,
                    detach=True,
                    command='sleep 60',
                    name=name,
                    user=uid,
                    volumes={config_dir: {'bind': config_dir, 'mode': 'rw'}},
                    environment={'HOME':home},
                )

    res = container.exec_run(f'gcloud {cmd}', stream=True, demux=False)
    # container.wait()
    for n in res.output:
        print(n.decode('utf-8'))
    container.stop()
    container.remove()

@click.command()
@click.argument('args', nargs=-1)
def run(args):
    """Example CLI app"""

    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(log_handler)


    home = str(Path.home())
    client = docker.from_env()
    uid = int(pwd.getpwnam(getpass.getuser()).pw_uid)
    config_dir = f'{home}/.config/gcloud'
    cmd = " ".join(args)

    start_container(client, 'google/cloud-sdk:latest', 'gcloud', uid, config_dir, home, cmd)

if __name__ == '__main__':
    run()
