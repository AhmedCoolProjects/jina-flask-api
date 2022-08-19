from flask import Flask
from flask_cors import CORS
# initialize the api
app = Flask(__name__)
CORS(app)

# import the routes
from routes.endpoints import *

# run our server
if __name__ == "__main__":
    app.run(debug=True)  # for dev
    # app.run() # for prod
