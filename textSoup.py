import requests
from bs4 import BeautifulSoup

url = 'https://www.theverge.com/2023/10/24/23930669/humane-ai-pin-trust-light-camera'
response = requests.get(url, timeout=10)

def get_soup() :
    # if it is a successful request (status_code being 200)
    if response.status_code == 200:
        # raw content not compatible with python 
        # so process it and organize it into a structured data format
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else :
        print("ERROR: not successful request")


def get_text():
    soup = get_soup()
    text = soup.get_text()
    return text

def get_html():
    soup = get_soup()
    for script in soup(["script", "style"]) :
        script.extract()
    return soup