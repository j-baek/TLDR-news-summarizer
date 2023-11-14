import requests
from bs4 import BeautifulSoup
import json
import gpt_api as getSummary
import os

# get the current directory of this file
curr_dir = os.path.dirname(os.path.realpath(__file__)) # __file__ is a path to this current script
# move up one level to the whole directory
whole_dir = os.path.dirname(curr_dir)

# construct the path to the news_data.json
news_data_json = os.path.join(whole_dir, 'json_data', 'news_data.json')
# construct the path to the news_url.json
news_url_json = os.path.join(whole_dir, 'json_data', 'news_url.json')

# this funciton returns data from the url. If the data has already been processed, then return that data
# from json file directly. If not, create json objects and store them on news_url.json and nes_data.json file then return the data
def get_data(url):

    # check if data file already exists
    if os.path.exists(news_data_json):
        try:
            with open(news_data_json, 'r') as file:
                existing_data = json.load(file)
                file.close()
        except FileNotFoundError as error:
            print(f"An error occured while working with the file!!!: {str(error)}")
    else:
        print("news_data.json file not FOUND!!!")

    # check if the JSON object with specific url already exists
    jo_existing = False
    for item in existing_data:
        if item.get('url') == url:
            jo_existing = True
            return item

    # if JSON object doesn't exist, add a new json object
    if jo_existing == False:
        # if JSON object doesn't exist in news_data.jon file
        response = requests.get(url, timeout=10)
        if response.status_code == 200: # status code being 200 means successful request
            # raw content not compatible with python 
            # so process it and organize it into a structured data format using BeautifulSoup function
            soup = BeautifulSoup(response.content, 'html.parser')

            id_num = str(len(existing_data) + 1)
            # url dictionary
            url_data = {}
            url_data["id"] = id_num
            url_data["url"] = url
            # data dictionary
            data = {}
            data["id"] = id_num
            data["url"] = url
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
            
            # open news_url json file and get url dictionary
            if os.path.exists(news_url_json) :
                try:
                    with open(news_url_json, 'r') as file:
                        existing_url = json.load(file)
                        file.close()
                except FileNotFoundError as error:
                    print(f"An error occurred while working with the file!!!: {str(error)}")
                
                # append url dictionary to existing json object 
                # since python dictionary and json object look identical, it can be appended directly
                existing_url.append(url_data)
                # rewrite the whole object
                with open(news_url_json, 'w') as file:
                    json.dump(existing_url, file, indent=4)
                    file.close()
            else:
                print("news_url.json file not FOUND!!!")

            # append news data dictionary to existing json object
            existing_data.append(data)
            if os.path.exists(news_data_json):
                with open(news_data_json, 'w') as file:
                    # rewrite the whole object
                    json.dump(existing_data, file, indent=4)
                    file.close()
                return data
            else:
                print("news_data.json file not FOUND!!!")
        else :
            print("ERROR: not successful request!!!!")
            print(response.status_code)