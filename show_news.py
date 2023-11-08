import json
import os
import textSoup as news_function

def news_pick(mode):
    print("\n\n")

    # user input taken as string, so convert 1 and 2 to strings
    if mode == str(1) or mode == str(2) :
        # mode 1 indicates showing today's news only
        if mode == str(1):
            # open today's news json file
            if os.path.exists('today_news.json'):
                try:
                    with open('today_news.json', 'r') as file:
                        today_data = json.load(file)
                        file.close()
                except FileNotFoundError:
                    print(f"An error occurred while working with the file!!!: {str(error)}")
            else:
                print("today_news.json file not FOUND!!!")

            num_id_len = len(today_data)
            for i in range(num_id_len):
                print("Title : " + today_data[i]["title"] +  "\n")
                print("\n" + today_data[i]["summary"]+ "\n\n\n")
            
        # mode 2 indicates displaying the whole news
        if mode == str(2):
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
            # (i = num_id_len; i > -1; i--)
            for i in range(num_id_len -1, -1, -1) :
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
    else:
        print("Invalid Input!")

