import re
import os
import sys
import pandas as pd
import numpy as np
from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from time import strftime
import datetime
import time
import json

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('value',type=str)
parser.add_argument('lookfor',type=str)
parser.add_argument('instance',type=str)
parser.add_argument('memory',type=str)

class startProcess(Resource):
    def post(self):
        try:
            args = parser.parse_args()
            print(args)
            command = str(args['value'])
            lookfor = str(args['lookfor'])
            instance = str(args['instance'])
            memoryVal = str(args['memory'])

        except Exception as e:
            print(e)
            return {'data': -999}

api.add_resource(startProcess, '/startProcess')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
