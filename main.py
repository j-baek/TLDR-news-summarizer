import textSoup as textSoup

url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'

if __name__ == "__main__" :
    url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'
    data = textSoup.get_data(url)
    #article = data["title"] + data["article_body"]

    
else:
    print(" imported")