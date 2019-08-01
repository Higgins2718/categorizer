import os

from flask import (
    Flask,
    render_template,
    request,
    make_response,
)
import requests
import pandas as pd
import json

import pickle
#import io
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer

# TODO Fix robots.txt
app = Flask(__name__)

@app.route("/api/", methods=['GET', 'POST'])
def default():
    body_unicode = request.data.decode('utf-8')
    print(request.get_data())
    #body = json.loads(body_unicode)
    content = request.get_data()
    #content = body['text']
    data = pd.read_csv("models/train_test.csv", header=0)
    labels = ['environment', 'safety', 'community', 'roads']
    Naive = pickle.load(open("models/pickle_model.pkl", 'rb'))

    # Load it later
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open("models/vocabulary.pkl", "rb")))

    # text = ["this playground is dangerous. someone could break an arm on the jungle gym"]
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array([content])))
    prediction = Naive.predict(tfidf)

    return labels[prediction[0]]

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
