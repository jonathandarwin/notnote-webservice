from flask import Flask
from flask_restful import Api, Resource, reqparse
from nltk.tokenize import word_tokenize

app = Flask(__name__)
api = Api(app)

class Note(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument("note")
            args = parser.parse_args()

            print(args["note"])

            listWord = word_tokenize(args["note"])
            result = {
                "status" : 200,
                "message" : "",
                "result" : listWord
            }
            return result,200
        except:
            return 'error',400

api.add_resource(Note, '/note')
app.run(debug=True)