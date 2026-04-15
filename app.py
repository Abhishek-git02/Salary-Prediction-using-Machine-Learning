from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model (NO TRAINING HERE)
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "ML Model API is running 🚀"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        area = data['area']
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']

        features = np.array([[area, bedrooms, bathrooms]])

        prediction = model.predict(features)[0]

        return jsonify({
            'predicted_price': float(prediction)
        })

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


