#!/usr/bin/env python3

import click
import logging

@click.command()
@click.option('-a', '--exampleoption', default=None, help='example')
@click.argument('examplearg', default=None)
def run(examplearg, exampleoption):
    """Example CLI app"""

    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stderr)
    logger.setLevel(getattr(logging, log.upper()))
    logger.addHandler(log_handler)
    logger.debug('Debug logging enabled')


if __name__ == '__main__':
    run()
