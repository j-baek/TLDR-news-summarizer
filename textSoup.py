import requests
from bs4 import BeautifulSoup
import json

# CNN News: Why teachers in South Korea are scared of their pupils – and their parents
# for this website, title is within <title> </title> tag
# 
url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'

def get_soup(url) :
    # if it is a successful request (status_code being 200)
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        # raw content not compatible with python 
        # so process it and organize it into a structured data format
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else :
        print("ERROR: not successful request!!!!")

def get_text():
    soup = get_soup(url)
    script_tag = soup.find('script', type='application/ld+json')

    if script_tag: # if script_tag has valid script element
        script_content = script_tag.string 
        try: 
            json_data = json.loads(script_content) # parse the'script_content' string as JSON data (dictionary)
            article_body = json_data.get('articleBody', '') # empty string is a default value to be returned if 'articleBody' key is not found
            return article_body
        except json.JSONDecodeError: #if error occurs during JSON parsing
            return "JSON parsing error"
    return "no valid script tag"

def get_html():
    soup = get_soup(url)
    for script in soup(["script", "style"]) :
        script.extract()
    return soup

def get_html_modified():
    soup = get_soup(url)
    title = soup.title.text
    return title