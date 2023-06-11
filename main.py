from flask import Flask, request, jsonify
from flask_cors import CORS
from src.task import predict_large_language_model_sample

# create the main function use the /api/predict endpoint for calling the task.py function
app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
	data = request.get_json()
	content = data['content']
	predict_large_language_model_sample("renata-386011", "text-bison@001", 0.1, 89, 0.1, 5, content, "us-central1")
