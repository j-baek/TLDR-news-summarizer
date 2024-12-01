import textSoup as news_function
from flask import Flask, render_template
import json
import headline as headline_function
import os
import show_news as show_news

if __name__ == "__main__" :

    headline_url = "https://edition.cnn.com/business/tech"
    headline_function.check_last_headline_update(headline_url)

    mode = input("If you want to see today's news, type 1. If you want to see whole news, type 2.\n")

    show_news.news_pick(mode)

# if __name__ is not "__main__", that means this main.py file is imported
else:
    print(" imported")