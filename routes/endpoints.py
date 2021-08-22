from flask import jsonify, request
from utils.json_encoder import JSONEncoder
from main import app, db
from bson import ObjectId

application_name = "template"

# endpoints

@app.route("/"+application_name+"/",methods=['GET'])
def welcome():
    return jsonify({"Ahmed Bargady":"Welcome to "+application_name+" 😃"})

@app.route("/"+application_name+"/api/v1/comments",methods=['GET'])
def GetComments():
    comments = db.comments.find()
    return JSONEncoder().encode(list(comments))

@app.route("/"+application_name+"/api/v1/comment/<id>",methods=['GET'])
def GetComment(id):
    comment = db.comments.find_one({"_id" :ObjectId(id)})
    return JSONEncoder().encode(comment)

@app.route("/"+application_name+"/api/v1/newuser",methods=['POST'])
def AddNewUser():
    data = request.json['data']
    db.newusers.insert_one(data)
    return jsonify({"status":"success"})

@app.route("/"+application_name+"/api/v1/newuser/updateone/<id>",methods=['POST'])
def UpdateNewUser(id):
    data = request.json['data']
    db.newusers.update_one({"_id" :ObjectId(id)}, {"$set": data})
    return jsonify({"status":"success"})

@app.route("/"+application_name+"/api/v1/newuser/updatemany/<key>/<value>",methods=['POST'])
def UpdateManyNewUsers(key,value):
    data = request.json['data']
    db.newusers.update_many({key :value}, {"$set": data})
    return jsonify({"status":"success"})

@app.route("/"+application_name+"/api/v1/newuser/delete/<id>",methods=['POST'])
def DeleteNewUser(id):
    db.newusers.delete_one({"_id" :ObjectId(id)})
    return jsonify({"status":"success"})

@app.route("/"+application_name+"/api/v1/newuser/deletemany/<key>/<value>",methods=['POST'])
def DeleteManyNewUsers(key,value):
    db.newusers.delete_many({key :value})
    return jsonify({"status":"success"})
