from flask import jsonify, request
from classes.functions import ApiFcts
from main import app

# endpoints
application_name = "template"


@app.route("/"+application_name+"/", methods=['GET'])
def welcome():
    return jsonify({"Ahmed Bargady": "Welcome to "+application_name+" 😃"})

# how to pass params from the route to the function


@app.route("/"+application_name+"/api/<semester>", methods=['GET'])
def getDataRoute(semester):
    apifcts_ = ApiFcts(semester)
    return apifcts_.sendFirstMessage()

# how to post data and get response


@app.route("/"+application_name+"/api/inbody", methods=['POST'])
def calculateFinalNoteRoute():
    semester = request.json['semester']
    apifcts_ = ApiFcts(str(semester))
    return apifcts_.sendFirstMessage()
