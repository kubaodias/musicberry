# MusicBerry HTTP client functions

import http.client
import json
import logging
import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from musicberry.web.app import MusicBerryWebApp

logger = logging.getLogger('musicberry')

class MusicBerryClient:

    def __init__(self):
        self.connection = http.client.HTTPConnection('localhost', MusicBerryWebApp.PORT)
        self.headers = {'Content-type': 'application/json'}

    def request(self, jsonData):
        self.connection.request('POST', '/api/v1/controller/', json.dumps(jsonData), self.headers)