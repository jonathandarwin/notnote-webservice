# NotNote Web Service
Web Service for NotNote apps (python).
<br>
This python code is used to predict whether the note is categorized as food, secret, or to-do-list note.

# How it works?
This web service has 2 main function : <b>train</b> and <b>predict</b>
<br>
## Train function 
Train function is used to train the model so later the model can help us to predict the note.
Step of training the model :
1. Load all dataset
2. Labeled the dataset
3. Vectorized the dataset by using TF-IDF
4. Train the dataset using Multinomial Logistic Regression
5. Save the vectorizer and the model in .pickle form
