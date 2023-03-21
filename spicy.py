import openai
import requests

# Set up the OpenAI API credentials
openai.api_key = "YOUR_API_KEY"

# Set up the OpenAI API endpoint
endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Define a function to generate a response from OpenAI
def generate_response(prompt):
    # Set up the request payload
    data = {
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.5,
        "n": 1,
        "stop": None
    }

    # Send the request to the OpenAI API
    response = requests.post(endpoint, headers={"Authorization": f"Bearer {openai.api_key}"}, json=data)

    # Parse the response
    response_text = response.json()["choices"][0]["text"]

    # Append "daddy" to the end of the response
    response_text += "cutie"

    return response_text
