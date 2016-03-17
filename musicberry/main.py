"""MusicBerry

Usage:
musicberry server (start|stop|restart)
musicberry control (play|pause|menu|next|prev|up|down)
musicberry (-h|--help)
musicberry (-v|--version)

Options:
  -h --help     Show this screen.
  -v --version  Show application version.
"""
from docopt import docopt
import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from musicberry.server.server import MusicBerryServer
from musicberry.web.client import MusicBerryClient

logger = logging.getLogger('musicberry')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
fileHandler = logging.FileHandler('musicberry.log')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='MusicBerry 1.0')

    if arguments['server']:
        server = MusicBerryServer('/tmp/musicberry.pid')

        if arguments['start']:
            server.start()
        elif arguments['stop']:
            server.stop()
        elif arguments['restart']:
            server.restart()

    elif arguments['control']:
        client = MusicBerryClient()

        if arguments['play']:
            client.request({'event': 'play'})
        elif arguments['pause']:
            client.request({'event': 'pause'})
        elif arguments['next']:
            client.request({'event': 'next'})
        elif arguments['prev']:
            client.request({'event': 'prev'})