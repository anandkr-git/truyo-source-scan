from transformers import pipeline

# Create a sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Analyze the sentiment of a text
result = sentiment_analyzer("I really enjoyed this book!")


from diffusers import DiffusionPipeline
import torch

# Load the Stable Diffusion pipeline
pipeline = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16)
pipeline.to("cuda")

# Generate an image from a text prompt
prompt = "A beautiful painting of a cat sitting on a windowsill, looking out at the rain."
image = pipeline(prompt).images[0]

# Save the image
image.save("cat_in_the_rain.png")

from huggingface_hub import hf_hub_download, HfApi

# Download a file from the Hugging Face Hub
file_path = hf_hub_download(repo_id="gpt2", filename="config.json")
print(file_path)

# Create a Hugging Face API client
api = HfApi()

# Upload a file to the Hugging Face Hub
api.upload_file(
    path_or_fileobj="local_file.txt",
    path_in_repo="uploaded_file.txt",
    repo_id="your-username/your-repo",
)

# This program adds two numbers

num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
