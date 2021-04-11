import pickle
from flask import Flask, request, render_template
from flasgger import Swagger
import numpy as np
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('rf.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_iris():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    prediction = model.predict(final_features)
	
    return render_template('index.html', prediction_text='Type of the Iris is {}'.format(prediction[0]))

if __name__ == '__main__':
	app.run(debug=True)