from flask import jsonify


class ApiFcts():
    def __init__(self, message):
        self.message = message

    def sendFirstMessage(self):
        return jsonify({"ahmed_says": "this is your message: "+self.message})
