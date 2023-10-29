import requests
from bs4 import BeautifulSoup
import json
import test as getSummary

def get_data(url):

    # check if data file already exists
    try:
        with open('news_data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        print("data file not FOUND!")

    # check if the JSON object with specific url already exists
    jO_existing = False
    for item in existing_data:
        if item.get('url') == url:
            jO_existing = True
            return item


        
    if jO_existing == False:
        # if JSON object doesn't exist in news_data.jon file
        response = requests.get(url, timeout=10)
        if response.status_code == 200: # status code being 200 means successful request
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
                    summary = getSummary.summarize_data(article_body) # use open ai api to get summarized data
                    data["summary"] = summary
                except json.JSONDecodeError: #if error occurs during JSON parsing
                    print("JSON parsing error")
    



            # this code removes all style and script tag 
            # so finding article body that is within script tag should be done earlier 
            # not currently in use
            '''
            for script in soup(["style", "script"]) :
                script.extract()
                data["html"] = data.get("html","") + str(script)
            '''

            json_object = json.dumps(data) # convert python dictionary to json object

            # add jsonObject to news_data.json file
            existing_data.append(json_object)
            with open('news_data.json', 'w') as file:
                json.dump(existing_data, file, indent=4)
            return json_object
        else :
            print("ERROR: not successful request!!!!")
            print(response.status_code)