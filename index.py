from flask import Flask
from flask_restful import Api, Resource, reqparse
import os
from nltk.tokenize import word_tokenize

app = Flask(__name__)
api = Api(app)

class Note(Resource):
    def post(self):
        return 'haha', 200
        # try:
        #     parser = reqparse.RequestParser()
        #     parser.add_argument("note")
        #     args = parser.parse_args()

        #     print(args["note"])

        #     listWord = word_tokenize(args["note"])
        #     result = {
        #         "status" : 200,
        #         "message" : "",
        #         "result" : listWord
        #     }
        #     return result,200
        # except:
        #     return 'error',400

api.add_resource(Note, '/note')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


# import os
# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello World",200

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)