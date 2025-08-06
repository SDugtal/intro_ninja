
import google.generativeai as genai
import os

# Set your API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()

for model in models:
    print(f"Model: {model.name}")
    print(f"  Supported Generation Methods: {model.supported_generation_methods}\n")
