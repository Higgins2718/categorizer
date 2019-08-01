from flask import (
    Flask,
    render_template,
    request,
    make_response,
)
import numpy as np
import requests
import pandas as pd
from IPython.display import display, HTML
import json

import pickle
import io

from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer


app = Flask(__name__)

@app.route("/api/")
def default(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    content = body['text']
    data = pd.read_csv("train_test.csv", header=0)
    labels = ['environment', 'safety', 'community', 'roads']
    Naive = pickle.load(open("pickle_model.pkl", 'rb'))

    # Load it later
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open("vocabulary.pkl", "rb")))

    # text = ["this playground is dangerous. someone could break an arm on the jungle gym"]
    tfidf = transformer.fit_transform(loaded_vec.fit_transform(np.array([content])))
    prediction = Naive.predict(tfidf)

    return labels[prediction[0]]


if __name__ == "__main__":
    app.run(debug=True)
