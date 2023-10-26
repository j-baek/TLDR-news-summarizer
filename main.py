import textSoup as textSoup

def get_raw_source():
    soup = textSoup.get_soup()
    return soup

def get_text_file():
    text = textSoup.get_text()
    return text

def get_html_file():
    html_file = textSoup.get_html()
    return html_file


if __name__ == "__main__" :
    soup = get_raw_source()
    text = get_text_file()
    html_file = get_html_file()
    
else:
    print(" imported")