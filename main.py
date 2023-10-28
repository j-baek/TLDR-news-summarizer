import textSoup as textSoup

url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'

def get_raw_source(url):
    soup = textSoup.get_soup(url)
    return soup

def get_text_file():
    text = textSoup.get_text()
    return text

def get_html_file():
    html_file = textSoup.get_html()
    return html_file

def get_html_modified():
    title = textSoup.get_html_modified()
    return title

if __name__ == "__main__" :
    url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'

    soup = get_raw_source(url)
    text = get_text_file()
    html_file = get_html_file()
    title = get_html_modified()

    tilte_w_text = title + "\n" + text
    print(tilte_w_text)
    
else:
    print(" imported")