# MusicBerry application state processing functions

import logging
import os.path
import subprocess
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from musicberry.db.adapter import DbConnection
from musicberry.server.daemon import Daemon
from musicberry.web.app import MusicBerryWebApp

class MusicBerryApp:
    dbConn = None

    def __init__(self, dbConn):
        self.index = 0
        self.volume = 50
        self.dbConn = dbConn
        self.radioStations = dbConn.radio_stations()
        self.player = None
        self.logger = logging.getLogger('musicberry')

        self.logger.info("* Initializing MusicBerry application...")

    def radio_stations(self):
        radioStationsJson = [rs.__dict__ for rs in self.radioStations]
        return radioStationsJson

    def next(self):
        self.index += 1
        if self.index >= len(self.radioStations):
            self.index = 0
        if self.player:
            self.pause()
            self.play()

    def prev(self):
        self.index -= 1
        if self.index < 0:
            self.index = len(self.radioStations) - 1
        if self.player:
            self.pause()
            self.play()

    def volume_up(self):
        if self.volume < 100:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def play(self):
        if (self.player == None):
            radioStation = self.radioStations[self.index]
            self.logger.info("Play '" + radioStation.name + "' (" + radioStation.url + ")")
            self.player = subprocess.Popen(["cvlc", radioStation.url], stdout=subprocess.PIPE, shell=False)
        else:
            self.logger.debug("Already playing...")

    def pause(self):
        if (self.player != None):
            self.player.terminate()
            self.player = None
        else:
            self.logger.debug("Already paused...")


class MusicBerryServer(Daemon):
    def __init__(self, pidfile):
        self.init_logger()
        super(MusicBerryServer, self).__init__(pidfile)

    def run(self):
        self.dbConn = DbConnection()
        self.app = MusicBerryApp(self.dbConn)
        self.webApp = MusicBerryWebApp(self.app)
        while True:
            time.sleep(1)

    def init_logger(self):
        self.logger = logging.getLogger('musicberry')
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        fileHandler = logging.FileHandler('/var/log/musicberry.log')
        fileHandler.setFormatter(formatter)
        fileHandler.setLevel(logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(fileHandler)