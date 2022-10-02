from flask import Flask, jsonify, request
import pandas as pd
import joblib
#from sklearn.preprocessing import StandardScaler
import pickle 
import xgboost

model = pickle.load(open("model/model.sav", 'rb'))

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json()
    #model = joblib.load('model/model.pkl')
    df = pd.DataFrame(json, index=[0])
    df_x_scaled = pd.DataFrame(df, columns=df.columns)
    y_predict = model.predict(df_x_scaled)

    result = {"Predicted Energy/Miles is" : str(y_predict[0])}
    
    #return result
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)



