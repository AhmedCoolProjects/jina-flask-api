from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

load_dotenv()

# initialize the api
app = Flask(__name__)
CORS(app)

# get db infos
host = os.getenv("MONGO_DB_URL")

# connect to the database
mongodb_client = PyMongo(app, uri=host)
db = mongodb_client.db

from routes.endpoints import *

# run our server
if __name__ == "__main__":
    app.run(debug=True)