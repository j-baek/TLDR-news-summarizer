# TLDR-news-summarizer
***
for people who are too lazy to read entire news but want to get some information
<br />
<br />

## Purpose
<br />
to give users news summarized in a few sentences.

## Inspiration
<br />
I always felt a bit lazy to read the whole news, and wanted shorter news just for important information.
<br />
Then, I thought I could write a program to interact with chatGPT to get summarization of news.

## Simple explanation
This program scrapes news from a certain website (tbd) using Python and Beautiful Soup.
<br />
Then it uses OpenAI API to give scraped news to chatGPT to summarize the news in a few sentences (number of sentences can be defined by the user)
<br />

## Steps
### Basics
- [x] Use Beautiful Soup to extract source code from a webpage
- [x] extract title and article body (use json functions to extract article body)
- [x] use OPEN AI API to send the extracted data and ask it to summarize the data
- [X] from news headline pages, get all head lines and their urls
- [X] as date changes, the news headlines get updated so update the data accordingly
- [X] show today's news headlines and show older news headlines as requested
- [X] build webpage
- [X] use Flask or Django to connect python to html file so that summarized news data can be shown on web page
- [X] display whole news or link website if a user wants to see the whole news

## notes


### Architecture Diagram
