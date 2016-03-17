import logging
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from flask import Flask, render_template, request
from flask.ext.classy import FlaskView, route
import musicberry.server.api as MusicBerryApi

logger = logging.getLogger('musicberry')

class MusicBerryWebApp:
    PORT = 5000
    def __init__(self, app):
        logger.info("* Initializing MusicBerry web application...")
        AppView.init(app)

class AppView(FlaskView):

    @classmethod
    def init(cls, app):
        webApp = Flask(__name__)
        cls.app = app
        cls.register(webApp, route_base='/')
        webApp.run()

    @route('/', methods=['GET'])
    def index(self):
        return render_template('index.html', radio_stations = AppView.app.radio_stations())

    @route('/api/v1/controller/', methods=['POST'])
    def api_controller(self):
        jsonData = request.json
        logger.debug("POST /api/v1/controller " + str(jsonData))
        MusicBerryApi.process(jsonData, AppView.app)
        return ''