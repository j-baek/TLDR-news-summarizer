import textSoup as news_function
from flask import Flask, render_template
import json
import headline as headline_function
import os

if __name__ == "__main__" :

    headline_url = "https://edition.cnn.com/business/tech"
    headline_function.check_last_headline_update(headline_url)

    # open json file to get the data that has news urls
    if os.path.exists('news_url.json'):
        try:
            with open('news_url.json', 'r') as file:
                url_data = json.load(file)
                file.close()
        except FileNotFoundError as error:
            print(f"An error occurred while working with the file!!!: {str(error)}")
    else:
        print("news_url.json file not FOUND!!!")

    num_id_len = len(url_data)
    
    # display all news options with id and title
    for i in range(num_id_len) :
        if url_data[i].get("id") == str(i + 1):
            news_json = news_function.get_data(url_data[i]["url"])
            print("\n " + str(i + 1))
            print("Title : " + news_json["title"] + "\n")
    
    userPick = input("Pick a news to see the summary. Please enter a number: ")
    print("\n")

    NEWS_FOUND = False
    # get the news that user chooses and display the tile and summary
    for i in range(num_id_len) :
        if url_data[i].get("id") == userPick:
            news_json = news_function.get_data(url_data[i]["url"])
            print("Title: " + news_json["title"] + "\n")
            print("\n" + news_json["summary"]+ "\n")
            NEWS_FOUND = True
            break;
    # for invalid input, print out message 
    if NEWS_FOUND is False :
        print("Invalid input. \n")

# if __name__ is not "__main__", that means this main.py file is imported
else:
    print(" imported")