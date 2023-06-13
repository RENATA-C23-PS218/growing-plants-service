import os
import json
import vertexai
import base64
from src.content_string import example_prompt
from dotenv import load_dotenv
from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

load_dotenv()
GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID')

def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_k: int,
    top_p: float,
    plant: str,
    soil: str,
    location: str = "us-central1",
    tuned_model_name: str = "",
    ) :
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
      model = model.get_tuned_model(tuned_model_name)
    plant = example_prompt + "input: teach me to plant " + plant + " using the " + soil +",  Don't use complicated language, and provide me the tips for growing\noutput:"
    print((f"Content: {plant}"))
    response = model.predict(
        plant,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    print(f"Response from Model: {response.text}")
    return response.text
