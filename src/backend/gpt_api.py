import openai
import creds
import os
openai.api_key = os.getenv('OPENAI_API') 

def summarize_data(article):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "you summarize the whole thing that the user sends in 3 sentences"},
            {"role": "user", "content": article}
        ]
    )
    #completion.choices[0].message
    return completion.choices[0].message["content"]