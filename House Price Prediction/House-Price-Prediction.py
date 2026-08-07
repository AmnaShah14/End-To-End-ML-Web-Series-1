from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import webbrowser
import threading

app = Flask(__name__)

# Load trained model
model = joblib.load('house_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        area = float(data.get('area'))
        input_data = pd.DataFrame([[area]], columns=["Area"])
        prediction = model.predict(input_data)[0]
        return jsonify({'prediction': round(float(prediction), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def open_browser():
    # Automatically opens the web page in your default browser
    webbrowser.open_new('http://127.0.0.1:5001/')

if __name__ == '__main__':
    # Open browser in a separate thread so it doesn't block the server startup
    threading.Timer(1.2, open_browser).start()
    app.run(port=5001, debug=False)