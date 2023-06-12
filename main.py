import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from src.task import predict_large_language_model_sample

PROJECT_ID = os.getenv('PROJECT_ID')

app = Flask(__name__)
CORS(app)

@app.route('/api/growing-plants-service')
def home():
	return jsonify({'status': 200,'success': True, 'message': 'Server running well', 'data': None }), 200

@app.route('/api/predict', methods=['POST'])
def predict():
	data = request.get_json()
	if 'plant' not in data or 'soil' not in data:
		return jsonify({'status': 400,'success': False, 'message': 'Bad Request, provide the right body to get the steps', 'data': None }), 400
	plant = data['plant']
	soil = data['soil']
	result = predict_large_language_model_sample(PROJECT_ID, "text-bison@001", 0.2, 200, 5, 0.3, plant, soil, "us-central1")
	return jsonify({'status': 200,'success': True, 'message': 'Successfully Get Growing Plant Prediction', 'data': result }), 200
