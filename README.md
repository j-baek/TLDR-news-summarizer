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

## Dockerization
- Dockerfile
  -  For requirements.txt, use either ```pip freeze``` or ```pipreqs``` (recommended)
      - ```pip freeze``` saves all packages and dependencies in the environment including those that are not used in the current project
      - ```pipreqs``` only puts those libraries in the requirements file which have been used in the project through imports. 
  -  Difference between ```RUN CD``` and ```WORKDIR```
      - ```RUN CD``` only changes directory for that command, and goes back to the default working directory
      - ```WORKDIR``` changes directory and stays in that directory
- .dockerignore
  -  Since .dockerignore file only checks the current working directory, a wildcard needs to be used for the files that should not be included
  -  '*/' is used for a file in any directory one level below the build context root.
  -  For specifying a file in any directory, '**/' needs to be used
- Building an image
  -  ```docker build -t tldr-news-summarizer:latest .```
    - ```-t``` flag tags the image with a name
    - ```tldr-news-summarizer```: name assigned to the immage
    - ```latest```: tag for the image, indicating that it is a most recent version of an image
- Running a docker with an api key
  -  ```docker run -d -p 3000:3000 \ --env-file /path/to/your/env/file \ --name tldr-news-summarizer \ tldr-news-summarizer:latest```
    - ```d```: flag that runs the container in detached mode (container runs in the background and doesn't block the terminal
    - ```--name tldr-news-summarizer```: container name
    - ```tldr-news-summarizer:latest```: specifies the Docker image to use for the container
