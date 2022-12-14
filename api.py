"""
API does functions for kNode to function, such as validation of token, node functions, etc.
"""

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Index(Resource):
    @staticmethod
    def get():
        return jsonify({'status': 'online'})

    @staticmethod
    def post():
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
