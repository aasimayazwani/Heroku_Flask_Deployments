import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd 

app = Flask(__name__)
model = pickle.load(open("XGB_Sep_02_2022.sav", 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    new_df = pd.DataFrame(int_features).T
    #print(new_df)
    prediction = model.predict(new_df)
    print(prediction)
    output = round(prediction[0], 2)
    print(output)
    return render_template('index.html', prediction_text='Energy Demand Per Mile should be $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    input_var = [np.array(list(data.values()))]
    new_df = pd.DataFrame(input_var).T
    prediction = model.predict(new_df)
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)








