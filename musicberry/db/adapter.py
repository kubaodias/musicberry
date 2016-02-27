# MusicBerry DB adaptation layer

import sqlite3

class DbConnection:

    def __init__(self):
        self.conn = sqlite3.connect('musicberry.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS RADIO_STATIONS
                            (NAME      TEXT   PRIMARY_KEY   NOT NULL,
                             URL       TEXT                 NOT NULL,
                             IMAGE_URL TEXT                 NOT NULL);''')
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def store(self, radioStation):
        radioStation.store(self.conn)

    def radio_stations(self):
        cursor = self.conn.execute("SELECT NAME,URL,IMAGE_URL FROM RADIO_STATIONS")
        result = []
        for row in cursor:
            name = row[0]
            url = row[1]
            image_url = row[2]
            result.append(RadioStation(name, url, image_url))
        return result

class RadioStation:

    def __init__(self, name, url, image_url = None):
        self.name = name
        self.url = url
        self.image_url = image_url

    def store(self, conn):
        conn.execute("INSERT INTO RADIO_STATIONS (NAME,URL,IMAGE_URL) \
                      VALUES ('" + self.name + "', '" + self.url + "', '" + self.image_url + "')")
        conn.commit()