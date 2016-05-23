import logging
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from flask import Flask, render_template, request
from flask.ext.classy import FlaskView, route
import musicberry.server.api as MusicBerryApi

class MusicBerryWebApp:
    PORT = 8080
    def __init__(self, app):
        self.logger = logging.getLogger('musicberry')
        self.logger.info("* Initializing MusicBerry web application...")
        AppView.init(app)

class AppView(FlaskView):

    @classmethod
    def init(cls, app):
        webApp = Flask(__name__)
        cls.logger = logging.getLogger('musicberry')
        cls.app = app
        cls.register(webApp, route_base='/')
        webApp.run(host = '0.0.0.0', port = MusicBerryWebApp.PORT)

    @route('/admin', methods=['GET'])
    def index(self):
        return render_template('index.html', radio_stations = AppView.app.radio_stations())

    @route('/api/v1/controller/', methods=['POST'])
    def api_controller(self):
        jsonData = request.json
        AppView.logger.debug("POST /api/v1/controller " + str(jsonData))
        MusicBerryApi.process(jsonData, AppView.app)
        return ''
