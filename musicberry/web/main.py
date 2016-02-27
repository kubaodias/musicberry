import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, render_template, request
from db.adapter import DbConnection
from app.state import AppState
import app.controller as MusicBerryController

app = Flask(__name__)
dbConn = DbConnection()
state = AppState(dbConn)

@app.route('/')
def index():
    radioStationsJson = [rs.__dict__ for rs in dbConn.radio_stations()]
    return render_template('index.html', radio_stations = radioStationsJson)

@app.route('/api/v1/controller', methods=['POST'])
def controller_api():
    MusicBerryController.process(request.json, state)
    return ''

if __name__ == '__main__':
    app.run()