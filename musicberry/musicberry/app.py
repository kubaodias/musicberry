# MusicBerry application state processing functions

import subprocess

class MusicBerryApp:
    def __init__(self, dbConn):
        self.index = 0
        self.volume = 50
        self.radioStations = dbConn.radio_stations()
        self.player = None
        print("MusicBerry application initialized")

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
        radioStation = self.radioStations[self.index]
        print("Play '", radioStation.name, "'", "(", radioStation.url, ")")
        self.player = subprocess.Popen(["cvlc", radioStation.url], stdout=subprocess.PIPE, shell=False)

    def pause(self):
        self.player.terminate()
        self.player = None
