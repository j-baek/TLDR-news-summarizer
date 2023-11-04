from bs4 import BeautifulSoup
import requests
import textSoup as news_function
from datetime import datetime
import os
import json

# put headline page url as input and it adds json objects to headline_url.json file
def get_headline_url(url):
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        headline_urls = soup.find_all('a', {"class": "container__link container__link--type-article container_lead-plus-headlines-with-images__link"}, {"data-link-type": "article"})
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
                            open('today_news.json', 'w').close()
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                        TODAY_NEWS = True
                    # write today's news data 
                    else:
                        
                        try:
                            with open('today_news.json', 'r') as file:
                                if EMPTY_FILE == False: # if it is an empty file, json.load will throw an exception error
                                    existing_data = json.load(file)
                                file.close()
                        except FileNotFoundError as error:
                            print(f"An error occurred while working with the file!!!: {str(error)}")
                        if EMPTY_FILE == True:
                            with open('news_url.json', 'w') as file:
                                json.dump(data, file, indent=4)
                                EMPTY_FIle = False
                                file.close()
                        else:
                            existing_data.append(data)
                            with open('news_url.json', 'w') as file:
                                json.dump(existing_data, file, indent=4)
                                file.close()
                        

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
        get_headline_url(url)
    else:
        print("Today's headline already acquired\n\n\n")