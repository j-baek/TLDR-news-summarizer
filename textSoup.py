import requests
from bs4 import BeautifulSoup
import json
import gpt_api as getSummary

# this funciton returns data from the url. If the data has already been processed, then return that data
# from json file directly. If not, create json objects and store them on news_url.json and nes_data.json file then return the data
def get_data(url):

    # check if data file already exists
    try:
        with open('news_data.json', 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        print("data file not FOUND!")

    # close file
    file.close()

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
            
            # open news_url json file and get url objects
            try:
                with open('news_url.json', 'r') as file:
                    existing_url = json.load(file)
                    file.close()
            except FileNotFoundError:
                print("data file not FOUND!")
            
            # add new url object to json file
            existing_url.append(url_data)
            with open('news_url.json', 'w') as file:
                json.dump(existing_url, file, indent=4)
                file.close()

            # since python dictionary and json object look identical, append it to json object right away
            existing_data.append(data)
            with open('news_data.json', 'w') as file:
                json.dump(existing_data, file, indent=4)
                file.close()
            return data
        else :
            print("ERROR: not successful request!!!!")
            print(response.status_code)

# put headline page url as input and it adds json objects to headline_url.json file
def get_headlines_from_main_page(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headline_urls = soup.find_all('a', {"class": "container__link container__link--type-article container_lead-plus-headlines-with-images__link"}, {"data-link-type": "article"})
        prev_url = "https://edition.cnn.com" 
        for headline_url in headline_urls:
            # the url doesn't included https://edition.cnn.com so add them manually
            h_url = "https://edition.cnn.com" + headline_url.get('href')
            # there are some duplications so exclude them
            if prev_url != h_url:
                get_data(h_url)
            prev_url = h_url
