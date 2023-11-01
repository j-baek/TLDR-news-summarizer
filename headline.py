from bs4 import BeautifulSoup
import requests

url = "https://edition.cnn.com/business/tech"

def get_headlines():
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        head_lines = soup.find_all('span', {"class" : "container__headline-text"})
        #print(head_lines)
        
        for head_line in head_lines:
            print(head_line.text)
    else:
        print("reqeust not SUCCESSFUL!!!")

def get_headline_url():
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headline_urls = soup.find_all('a', {"class": "container__link container__link--type-article container_lead-plus-headlines-with-images__link"}, {"data-link-type": "article"})
        
        for headline_url in headline_urls:
            h_url = "https://edition.cnn.com" + headline_url.get('href')

            print(h_url)

#get_headlines()
get_headline_url()


'''
<a href="/2023/10/31/tech/canada-china-wechat-ban-security-hnk-intl/index.html" class="container__link container__link--type-article container_lead-plus-headlines-with-images__link"
        data-link-type="article"
    >
                <div class="container__text container_lead-plus-headlines-with-images__text">
            <div class="container__headline  container_lead-plus-headlines-with-images__headline">
                    <span class="container__headline-text" data-editable="headline">Canada bans China’s Wechat from government devices citing security risks</span>
            </div>
        </div>
    </a>
    '''