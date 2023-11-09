import json
import os
import textSoup as news_function

# adding new line after n chars. After n chars, if it is not white space, put new line when seeing a white space
def add_newline_after_n_chars(string, n):
    lines = string.split('\n') # split string into list of lines whenever encountering new line
    updated_lines = []

    for line in lines:
        words = line.split() # split current line into list of words
        current_line = ''

        for word in words:
            if len(current_line) + len(word) <= n: # checking if adding the current word would exceed n
                current_line += word + ' ' # adding current word to current line
            else:
                updated_lines.append(current_line.strip()) # append the current line to the list
                current_line = word + ' ' # making a new current line

        updated_lines.append(current_line.strip()) # appending the last line

    return '\n'.join(updated_lines) # join all the modified lines into a string with new line between the lines

def news_pick(mode):
    #print("\n\n")

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
            result1 =""
            for i in range(num_id_len):
                result1 += ("Title : " + today_data[i]["title"] +  "\n" + "\n" + today_data[i]["summary"]+ "\n\n\n")
            
            news_string = result1.replace(".", ".\n")
            news_split = add_newline_after_n_chars(news_string, 250)

            return news_split
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
            result2 =""
            for i in range(num_id_len -1, -1, -1) :
                    news_json = news_function.get_data(url_data[i]["url"])
                    result2 +=  ("\n " + str(i + 1) + " Title : " + news_json["title"] + "\n")
            return result2
            userPick = input("Pick a news to see the summary. Please enter a number: ")
            print("\n")
            NEWS_FOUND = False
            # get the news that user chooses and display the tile and summary
            result2=""
            for i in range(num_id_len) :
                if url_data[i].get("id") == userPick:
                    news_json = news_function.get_data(url_data[i]["url"])
                    result2 += ("Title: " + news_json["title"] + "\n" + "\n" + news_json["summary"]+ "\n")
                    NEWS_FOUND = True
                    break;
            return result2
            # for invalid input, print out message 
            if NEWS_FOUND is False :
                print("Invalid input. \n")
    else:
        print("Invalid Input!")


print(add_newline_after_n_chars(news_pick(str(1)), 100))