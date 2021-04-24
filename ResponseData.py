from flask import jsonify


class ResponseData:
    def __init__(self, keys, values):
        self.keys = keys
        self.values = values

    def create_dict(self):
        response = {}

        for i, key in enumerate(self.keys):
            response[key] = self.values[i]

        return response

    def create_response(self):
        response = self.create_dict()

        return jsonify(response)
