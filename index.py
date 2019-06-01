from flask import Flask
from flask import request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split, cross_val_score
import pickle

app = Flask(__name__)

@app.route('/note', methods=['POST'])
def post():        
    note = request.form.get('note') 
    listWord = word_tokenize(note)  
    # listStopWords = stopwords.words('english')
    listTemp = []
    for word in listWord:
        # if(word.lower() not in listStopWords):
        listTemp.append(word)

    result = {
        'result' : listTemp
    }
    return json.dumps(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    