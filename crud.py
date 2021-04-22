from flask import Flask
from flask_restful import Api, Resource, reqparse
import random


class Quote(Resource):

    def get(self, id=0):
        if id == 0:
            return random.choice(ai_quotes), 200

        for quote in ai_quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

app = Flask(__name__)
api = Api(app)