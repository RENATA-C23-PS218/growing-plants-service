import os
import vertexai
import base64
from dotenv import load_dotenv
from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

load_dotenv()
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = base64.b64decode(os.getenv('GOOGLE_APPLICATION_CREDENTIALS')).decode('utf-8')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
PROJECT_ID = os.getenv('PROJECT_ID')

def predict_large_language_model_sample(
    project_id: str,
    model_name: str,
    temperature: float,
    max_decode_steps: int,
    top_p: float,
    top_k: int,
    content: str,
    location: str = "us-central1",
    tuned_model_name: str = "",
    ) :
    """Predict using a Large Language Model."""
    vertexai.init(project=project_id, location=location)
    model = TextGenerationModel.from_pretrained(model_name)
    if tuned_model_name:
      model = model.get_tuned_model(tuned_model_name)
    response = model.predict(
        content,
        temperature=temperature,
        max_output_tokens=max_decode_steps,
        top_k=top_k,
        top_p=top_p,)
    print(f"Response from Model: {response.text}")

# TODO: remove the content query
predict_large_language_model_sample(PROJECT_ID, "text-bison@001", 0.1, 89, 0.1, 5, '''Growing a plantation in easy steps, using the provided info such as soil type

input: How to plant a rose in aluvial soil?
output: 1. Prepare the soil by tilling it and adding compost or manure.
2. Plant the rose bushes in the soil, spacing them 24 inches apart.
3. Water the bushes regularly.
4. Fertilize the bushes every two weeks.
5. Deadhead the flowers to encourage more blooms.
6. Protect the bushes from frost in the winter.

input: teach me to plant rose using the aluvial soil, Don\'t use complicated language
output: To plant a rose in aluvial soil, you will need:

* A rose bush
* A shovel
* A trowel
* Compost or manure
* Water

1. Dig a hole in the soil that is twice the size of the rose bush\'s root ball.
2. Add compost or manure to the bottom of the hole.
3. Place the rose bush in the hole and fill in the hole with soil.
4. Water the rose bush thoroughly.
5. Mulch around the rose bush to help keep the soil moist.

Water the rose bush regularly, especially during dry periods. Fertilize the rose bush every two weeks with a water-soluble fertilizer. Deadhead the flowers to encourage more blooms. Protect the rose bush from frost in the winter.

input: give me a brief step to plant a lettuce
output:
''', "us-central1")