import textSoup as textSoup
from flask import Flask, render_template
import test as gptSummarizer

'''
app = Flask(__name__)
@app.route('/')
def index():
    text = "string generated in Python"
    return render_template('page.html', text=text)
'''


if __name__ == "__main__" :
    # CNN News: Why teachers in South Korea are scared of their pupils – and their parents
    # for this website, title is within <title> </title> tag
    url = 'https://edition.cnn.com/2023/10/27/asia/south-korea-teachers-strike-analysis-intl-hnk/index.html'
    #url = 'https://edition.cnn.com/2023/10/27/world/abandoned-golf-courses-reclaimed-by-nature-c2e-spc-scn-intl/index.html'
    data = textSoup.get_data(url)
    article = data["title"] + "\n\n" + data["article_body"]
    #app.run()

    # get summarized news 
    summary = gptSummarizer.summarize_data(article)
    print("\n")
    print("Title : " + data["title"] + "\n")
    print(summary)

    #print(summary)

else:
    print(" imported")