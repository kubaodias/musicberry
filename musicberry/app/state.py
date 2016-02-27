#!/usr/bin/env python

class AppState:
    def __init__(self, dbConn):
        self.index = 0
        self.volume = 50
        self.radioStations = dbConn.radio_stations()
        print("Application state initialized with", dbConn)

    def next(self):
        self.index += 1
        if self.index >= self.radioStations.size():
            self.index = 0
        self.printCurrentStation()

    def prev(self):
        self.index -= 1
        if self.index < 0:
            self.index = self.radioStations.size() - 1
        self.printCurrentStation()

    def volume_up(self):
        if self.volume < 100:
            self.volume += 1

    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1

    def printCurrentStation(self):
        print("Currently playing", self.radioStations[self.index].name)