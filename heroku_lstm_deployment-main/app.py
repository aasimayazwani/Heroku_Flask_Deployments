from flask import Flask, jsonify, request
import pandas as pd
import joblib
from tensorflow.keras.models import load_model


mod_dir   = "model/model.h5"
y_scaler  = joblib.load("model/y_scaler.pkl") 
model = load_model(mod_dir)
app = Flask(__name__)

@app.route("/", methods=['POST'])
def predict():
    json = request.get_json(force=True)
    df = pd.DataFrame(json, index=[0])
    df_x_scaled = pd.DataFrame(df, columns=df.columns)
    X_test = df_x_scaled.values
    test_X = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))
    predicted_y = model.predict(test_X)
    y_predict = y_scaler.inverse_transform(predicted_y)[0][0]
    result = {"Predicted Energy/Miles is" : str(y_predict)}
    return jsonify(result)

if __name__ == "__main__":
    app.run(port='5000',debug=True)


