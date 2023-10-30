import textSoup as data_function
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
    num_id_len = len(url_data)
    
    for i in range(num_id_len) :
        if url_data[i].get("id") == str(i + 1):
            news_json = data_function.get_data(url_data[i]["url"])
            print("\n " + str(i + 1))
            print("Title : " + news_json["title"] + "\n")
    
    userPick = input("Pick a news to see the summary. Please enter a number: ")
    print("\n")

    NEWS_FOUND = False
    for i in range(num_id_len) :
        if url_data[i].get("id") == userPick:
            news_json = data_function.get_data(url_data[i]["url"])
            print("Title: " + news_json["title"] + "\n")
            print("\n" + news_json["summary"]+ "\n")
            NEWS_FOUND = True
            break;

    if NEWS_FOUND is False :
        print("Invalid input. \n")

else:
    print(" imported")