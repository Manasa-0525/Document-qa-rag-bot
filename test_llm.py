import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.0-flash")

# Generate response
response = model.generate_content(
    "Explain what a RAG pipeline is in simple words."
)

# Print output
print("\nResponse:\n")
print(response.text)