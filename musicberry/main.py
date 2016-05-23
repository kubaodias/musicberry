"""MusicBerry

Usage:
musicberry server start [-d|--daemon]
musicberry server stop
musicberry control (play|pause|menu|next|prev|up|down)
musicberry (-h|--help)
musicberry (-v|--version)

Options:
  -d --daemon   Run as a daemon.
  -h --help     Show this screen.
  -v --version  Show application version.
"""
from docopt import docopt
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from musicberry.server.server import MusicBerryServer
from musicberry.web.client import MusicBerryClient

if __name__ == '__main__':
    arguments = docopt(__doc__, version='MusicBerry 1.0')

    if arguments['server']:
        server = MusicBerryServer('/tmp/musicberry.pid')

        if arguments['start']:
            if arguments['--daemon']:
                server.start()
            else:
                # run thread function
                server.run()
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
        elif arguments['menu']:
            client.request({'event': 'menu'})
        elif arguments['next']:
            client.request({'event': 'next'})
        elif arguments['prev']:
            client.request({'event': 'prev'})
        elif arguments['up']:
            client.request({'event': 'up'})
        elif arguments['down']:
            client.request({'event': 'down'})
