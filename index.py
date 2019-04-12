from flask import Flask
app = Flask(__name__)
from flask import Flask
from flask import request
app = Flask(__name__)
import os

@app.route('/postjson', methods=['POST'])
def post():    
    content = request.get_json()    
    note = content['note']
    
    return note,200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)