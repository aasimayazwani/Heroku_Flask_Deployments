from flask import Flask, jsonify, request
import pandas as pd
import joblib
import pickle 
import xgboost


y_scaler  = joblib.load("model/y_scaler.pkl") 
model = pickle.load(open("model/model.sav", 'rb'))

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def do_prediction():
    json = request.get_json(force=True)
    df = pd.DataFrame(json, index=[0])
    df_x_scaled = pd.DataFrame(df, columns=df.columns)
    y_predict = model.predict(df_x_scaled)
    result = {"Predicted Energy/Miles is" : str(y_predict[0])}
    return jsonify(result)

if __name__ == "__main__":
    app.run(port='5000',debug=True)


