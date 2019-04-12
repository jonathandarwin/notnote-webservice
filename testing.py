from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

note = 'The Quick Brown Fox Jumps Over the Lazy Dog'
listStopWords = stopwords.words('english')
lemmatizer = WordNetLemmatizer()

# tokenize 
listWord = word_tokenize(note)

# remove stopwords and lemmatize
listTemp = []
for word in listWord:
    if(word.lower() not in listStopWords):
        listTemp.append(lemmatizer.lemmatize(word))
listWord = listTemp

print(listWord)