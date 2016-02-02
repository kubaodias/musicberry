import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from flask import Flask, render_template
from db.adapter import DbConnection, RadioStation

app = Flask(__name__)

@app.route('/')
def index():
    dbConn = DbConnection()
    radioStationsJson = [rs.__dict__ for rs in dbConn.radio_stations()]
    return render_template('index.html', radio_stations = radioStationsJson)

if __name__ == '__main__':
    app.run()