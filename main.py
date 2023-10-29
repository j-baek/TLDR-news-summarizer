import textSoup as news_data
from flask import Flask, render_template
import json

'''
app = Flask(__name__)
@app.route('/')
def index():
    text = "string generated in Python"
    return render_template('page.html', text=text)
'''


if __name__ == "__main__" :
    try:
        with open('news_url.json', 'r') as file:
            url_data = json.load(file)
    except FileNotFoundError:
        print("json file not found!!!")

    file.close()

    for item in url_data:
        for i in range(10) :
            if item.get('id') == str(i + 1):
                news_json = news_data.get_data(item["url"])
                print("\n " + str(i + 1) + "\n ")
                print("Title : " + news_json["title"] + "\n")
                print(news_json["summary"])
                print("\n\n")


else:
    print(" imported")