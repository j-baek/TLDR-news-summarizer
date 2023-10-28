import requests
from bs4 import BeautifulSoup
import json

# CNN News: Why teachers in South Korea are scared of their pupils – and their parents
# for this website, title is within <title> </title> tag
# 
url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'
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
    script_tag = soup.find('script', type='application/ld+json')

    if script_tag:
        script_content = script_tag.string
        try: 
            json_data = json.loads(script_content)
            article_body = json_data.get('articleBody', '')
            return article_body
        except json.JSONDecodeError:
            return "JSON parsing error"
    return "not successful to extract article body"

def get_html():
    soup = get_soup()
    for script in soup(["script", "style"]) :
        script.extract()
    return soup

def get_html_modified():
    soup = get_soup()
    title = soup.title
    return str(title)