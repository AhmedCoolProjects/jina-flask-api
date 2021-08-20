from flask import jsonify, request
from classes.functions import ApiFcts
from main import app

# endpoints
application_name = "template"

@app.route("/"+application_name+"/",methods=['GET'])
def welcome():
    return jsonify({"Ahmed Bargady":"Welcome to "+application_name+" 😃"})

# how to pass params from the route to the function
# @app.route("/"+application_name+"/api/v1/data/<semester>",methods=['GET'])
# def getDataRoute(semester):
#     apifcts_ = ApiFcts(int(semester))
#     return apifcts_.gettingJsonData()

# how to post data and get response
# @app.route("/"+application_name+"/api/v1/cfn",methods=['POST'])
# def calculateFinalNoteRoute():
#     semester = request.json['semester']
#     apifcts_ = ApiFcts(int(semester))
#     user_el_modules_notes = request.json['user_el_modules_notes']
#     return apifcts_.calcNotes(user_el_modules_notes)
