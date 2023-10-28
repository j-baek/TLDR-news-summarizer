import requests
from bs4 import BeautifulSoup
import json

def get_data(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        # raw content not compatible with python 
        # so process it and organize it into a structured data format
        soup = BeautifulSoup(response.content, 'html.parser')

        data = {}
        data["title"] = soup.title.text

        script_tag = soup.find('script', type='application/ld+json')
        
        if script_tag: # if script_tag has valid script element
            script_content = script_tag.string
            try:
                json_data = json.loads(script_content) # parse the'script_content' string as JSON data (dictionary)
                article_body = json_data.get('articleBody', '') # empty string is a default value to be returned if 'articleBody' key is not found
                data["article_body"] = article_body
            except json.JSONDecodeError: #if error occurs during JSON parsing
                print("JSON parsing error")

        # this code removes all style and script tag 
        # so finding article body that is within script tag should be done earlier 
        for script in soup(["style", "script"]) :
            script.extract()
            data["html"] = data.get("html","") + str(script)

        return data
    else :
        print("ERROR: not successful request!!!!")
        print(response.status_code)