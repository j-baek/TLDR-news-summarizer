from bs4 import BeautifulSoup
import requests

url = "https://edition.cnn.com/business/tech"

'''
def make_headline_json():
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headlines = soup.find_all('span', {"class" : "container__headline-text"})
        headlineurls = soup.find_all('a', {"class": "container__link container__link--type-article container_lead-plus-headlines-with-images__link"}, {"data-link-type": "article"})

        # make python dictionary containing headline and its url
        h_data = {}
        
        # count of id
        c = 1
        for head_line in headline_urls:
            h_data["id"] = str(c)
            h_data["headline"] = head_line




    else: print("request not SUCCESSFUL!")
'''

def get_headlines():
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        head_lines = soup.find_all('span', {"class" : "container__headline-text"})
        # set to check headline duplications
        h_set = set()
        for head_line in head_lines:
            dup = head_line in h_set
            if(not dup):
                print(head_line.text)
                h_set.add(head_line)
    else:
        print("reqeust not SUCCESSFUL!!!")

def get_headline_url():
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
                print(h_url)
            prev_url = h_url

get_headlines()
#get_headline_url()
