import requests
from bs4 import BeautifulSoup

url = 'https://www.theverge.com/2023/10/24/23930669/humane-ai-pin-trust-light-camera'

response = requests.get(url)

# if it is a successful request
if response.status_code == 200:
    # raw content is not compatible with python
    # so process it and organize it into a structured data format
    soup = BeautifulSoup(response.content, 'html.parser')
    # get text from html
    text = soup.get_text()
    print(text)

else : 
    print("unsuccessful request")