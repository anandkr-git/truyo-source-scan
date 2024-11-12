from google.cloud import automl_v1beta1 as automl

project_id = "your_project_id"
model_id = "your_model_id"
content = "path_to_your_image.jpg"

# Initialize client and define model path
client = automl.PredictionServiceClient()
model_full_id = client.model_path(project_id, "us-central1", model_id)

# Read image and prepare payload
with open(content, "rb") as image_file:
    content = image_file.read()
payload = {"image": {"image_bytes": content}}

# Get prediction
response = client.predict(name=model_full_id, payload=payload)
for result in response.payload:
    print("Predicted label:", result.display_name, ", Confidence:", result.classification.score)
