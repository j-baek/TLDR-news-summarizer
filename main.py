import textSoup as textSoup

if __name__ == "__main__" :
    # CNN News: Why teachers in South Korea are scared of their pupils – and their parents
    # for this website, title is within <title> </title> tag
    url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'
    data = textSoup.get_data(url)
    article = data["title"] + "\n\n" + data["article_body"]
    print(article)

    
else:
    print(" imported")