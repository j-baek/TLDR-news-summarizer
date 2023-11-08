from bs4 import BeautifulSoup
import requests
import textSoup as news_function
from datetime import datetime
import os
import json

# get today's news and store them in today_news.json file
def get_today_news(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headline_urls = soup.find_all('a', {"class": "container__link container__link--type-article container_lead-plus-headlines-with-images__link"}, {"data-link-type": "article"})
        # for CNN news source code, there are some duplicated urls in a row
        # to prevent getting duplicated urls, compare  previous url and current url
        prev_url = "https://edition.cnn.com" 
        TODAY_NEWS = False
        EMPTY_FILE = True
        if os.path.exists('today_news.json'):
            for headline_url in headline_urls:
                # the url doesn't included https://edition.cnn.com so add them manually
                h_url = "https://edition.cnn.com" + headline_url.get('href')
                # there are some duplications so exclude them
                if prev_url != h_url:
                    data = news_function.get_data(h_url)
                    # delete previous data in today_news file and rewrite the whole file with 
                    # most up-to-date news
                    # first, delete previous data if the data is not today's data
                    if TODAY_NEWS == False:
                        try:
                            # using 'w' mode wipes the whole data in the file to write new data
                            # so opening the file with 'w' and closing the file will just wipe the whole memory
                            open('today_news.json', 'w').close() 
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                        TODAY_NEWS = True
                    # write today's news data 
                    
                    existing_data ="" # if this variable doesn't store data, don't write it in the json file
                    
                    if EMPTY_FILE == False: # if it is an empty file, json.load function will throw an exception error so check it
                        try:
                            with open('today_news.json', 'r') as file:
                                existing_data = json.load(file)
                                file.close()
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                    else: # if writing the first news in the empty file
                        try:
                            with open('today_news.json', 'a') as file:
                                jsonfile = [] # create a list and put python dictionary within the list. Otherwise, the dictionaries will not be within '[]'
                                jsonfile.append(data)
                                json.dump(jsonfile, file, indent=4)
                                EMPTY_FILE = False
                                file.close()
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                    
                    if len(existing_data) != 0: # when there is a data in existing_data
                        try:
                            with open('today_news.json', 'w') as file:
                                existing_data.append(data)
                                json.dump(existing_data, file, indent=4)
                                file.close()
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                        
                # set current url to be previous url after processing it
                prev_url = h_url
        else:
            print("today_news.json file not FOUND!!!")

    else: 
        print("ERROR: not successful request!!!!")
        print(response.status_code)


# check if today's headline has been updated. If not, update it
def check_last_headline_update(url): 
    # get today's date
    today = datetime.today().date()
    if os.path.exists('last_url_update.txt'):
        try:
            with open('last_url_update.txt', "r") as file:
                # strptime function converts string to date object
                last_date_called = datetime.strptime(file.read(), "%Y-%m-%d").date()
                file.close()
            # using "W", delete the previous data and write over it
            with open('last_url_update.txt', "w") as file:
                # stftime converts date object to string 
                file.write(today.strftime("%Y-%m-%d"))
                file.close()

        except FileNotFoundError as error:
            print(f"An error occurred while working with the file!!!: {str(error)}")
    else:
        print("last_url_update file not FOUND!!!")

    # if the headline has not been updated, update it 
    if today != last_date_called:
        print("New data processing")
        get_today_news(url)
    else:
        print("Today's headline already acquired\n\n\n")