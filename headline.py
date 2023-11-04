from bs4 import BeautifulSoup
import requests
import textSoup as news_function
from datetime import datetime
import os

url = "https://edition.cnn.com/business/tech"

# put headline page url as input and it adds json objects to headline_url.json file
def get_headline_url(url):
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
                data = news_function.get_data(h_url)
                
            prev_url = h_url


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
        get_headline_url(url)
    else:
        print("Today's headline already acquired\n\n\n")