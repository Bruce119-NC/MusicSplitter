import os
from flask import Flask, send_file
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
app.secret_key = 'secret'
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('file_name', type=str)


class StartProcess(Resource):
    @staticmethod
    def post():
        try:
            args = parser.parse_args()
            file_name = str(args['file_name'])
            os.system(f'''bash run_spleeter.sh {file_name}''')
            return send_file(f'/home/nabarun/Projects/MusicSplitter/output/{file_name.split(".")[0]}/accompaniment.wav',
                             mimetype="audio/wav", as_attachment=True, attachment_filename=file_name)
        except Exception as e:
            print(e)
            return {'data': -999}


api.add_resource(StartProcess, '/startProcess')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
