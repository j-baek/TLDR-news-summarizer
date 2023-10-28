import os
import openai

# Access the GitHub secret as an environment variable
api_key = os.getenv('MY_API_KEY')
# setting openai api key
openai.api_key = api_key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role" : "user", "content": "what is the difference between Celsius and Fahrenheit?"}
    ]
)

print(response)