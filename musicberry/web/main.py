import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, render_template, request
from db.adapter import DbConnection
from musicberry.app import MusicBerryApp
import musicberry.api as MusicBerryApi

webApp = Flask(__name__)
dbConn = DbConnection()
app = MusicBerryApp(dbConn)

@webApp.route('/')
def index():
    radioStationsJson = [rs.__dict__ for rs in dbConn.radio_stations()]
    return render_template('index.html', radio_stations = radioStationsJson)

@webApp.route('/api/v1/controller', methods=['POST'])
def controller_api():
    MusicBerryApi.process(request.json, app)
    return ''

if __name__ == '__main__':
    webApp.run()