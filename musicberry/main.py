# MusicBerry application state processing functions

import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from musicberry.server.server import MusicBerryServer

logger = logging.getLogger('musicberry')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
fileHandler = logging.FileHandler('musicberry.log')
fileHandler.setFormatter(formatter)
fileHandler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(fileHandler)

if __name__ == '__main__':
    server = MusicBerryServer('/tmp/musicberry.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            server.start()
        elif 'stop' == sys.argv[1]:
            server.stop()
        elif 'restart' == sys.argv[1]:
            server.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print("usage: musicberry start|stop|restart")
        sys.exit(2)