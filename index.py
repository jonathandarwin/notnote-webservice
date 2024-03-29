from flask import Flask
from flask import request, jsonify
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split, cross_val_score
import pickle
from os import path

app = Flask(__name__)

@app.route('/train', methods=['POST'])
def postTrain():                
    vectorizer = TfidfVectorizer()
    classifier = LogisticRegression()
    
    data = load_files('train')    
    dataset, label = data.data, data.target
    
    dataset_train = vectorizer.fit_transform(dataset)    
    classifier.fit(dataset_train, label)

    with open('model.pickle', 'wb') as classifier_file:
        pickle.dump(classifier, classifier_file)        

    with open('vectorizer.pickle', 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)        
        
    return "Train Success"
    

@app.route('/note', methods=['POST'])
def postPredict():        
    # note = request.form.get('note')    
    data = request.get_json()
    note = data['note']

    category = ''
    # STEP 1 : Remove stopwords
    listWord = word_tokenize(note)  
    listStopWords = stopwords.words('english')
    listTemp = []
    for word in listWord:
        if(word.lower() not in listStopWords):
            listTemp.append(word)
    listWord = listTemp

    # STEP 2 : Lematizing
    listTemp = []
    lemmatizer = WordNetLemmatizer()
    for word in listWord:
        listTemp.append(lemmatizer.lemmatize(word))
    listWord = listTemp

    # STEP 3 : Load Vectorizer and Model (Train if there are no model.pickle or vectorizer.pickle)    
    if(path.exists('model.pickle') == False or path.exists('vectorizer.pickle') == False):
        postTrain()

    with open('model.pickle', 'rb') as classifier_file:        
        with open('vectorizer.pickle', 'rb') as vectorizer_file:
            # vectorizer = pickle.load(vectorizer_file, encoding='latin1')
            # model = pickle.load(classifier_file, encoding='latin1')    

            vectorizer = pickle.load(vectorizer_file)
            model = pickle.load(classifier_file)    
            word = note
            # STEP 4 : Transform word with tfidf
            transform_word = vectorizer.transform([word])
            predictions = model.predict(transform_word)

            if predictions[0] == 0:
                category = 'food'
            elif predictions[0] == 1:
                category = 'secret'
            else:
                category = 'todo'    
    

    result = {
        'result' : category
    }
    # return json.dumps(result)
    return jsonify(result)


if __name__ == "__main__":
    # abis di push, tambahin command ini
    # heroku ps:scale web=1
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    