import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('obesity_level')

@app.route('/predict', methods=['POST'])
def predict():
    individual = request.get_json()

    X = dv.transform([individual])
    obesity_level = model.predict(X)[0]
    y_pred = model.predict_proba(X)

    result = {
        'obesitiy_level': int(obesity_level),
        'level probality': float(y_pred[0, obesity_level])
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)