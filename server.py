from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

app = Flask(__name__)
api = Api(app)


class Cheese(Resources):
    def get(self):
        data = pd.read_csv('data/cheese.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code



api.add_resource(Cheese, "/cheese")

if __name__ == '__main__':
    app.run(debug=True)