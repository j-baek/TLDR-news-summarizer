# TLDR News Summarizer

**For people who want the gist of the news without reading the entire article.**

---

## Purpose

The TLDR News Summarizer aims to provide users with concise summaries of news articles in just a few sentences. This tool is perfect for those who prefer to get the key points of news quickly and effortlessly.

---

## Inspiration

The idea stemmed from a personal need for shorter, to-the-point news summaries. Instead of wading through lengthy articles, this program uses technology to generate bite-sized news summaries, saving time and effort.

---

## Overview

This program scrapes news from a website (to be determined) using Python and Beautiful Soup. Then, it employs the OpenAI API to summarize the scraped news into a few user-defined sentences. 

---

## Features

### Core Functionalities
- Extracts the title and article body from a news webpage using Beautiful Soup and JSON functions.
- Retrieves headlines and their URLs from news headline pages.
- Updates headlines as the date changes to ensure fresh news content.
- Provides access to older headlines upon user request.
- Displays today’s news headlines and their summaries on a webpage.
- Links to the full news article for further reading.

### User Interaction
- Uses Flask to connect Python logic to an HTML webpage, presenting the summarized news in an intuitive interface.
- Allows customization of the summary length (number of sentences).

### Additional Features
- Easy access to full articles via embedded links.

---

## Dockerization

### Key Concepts

1. **Requirements File**:
   - Use `pipreqs` (recommended) to generate `requirements.txt`. It only includes libraries directly used in the project.
   - Alternatively, use `pip freeze` (not recommended), which lists all packages in the environment, even unused ones.

2. **Directory Management**:
   - Use `WORKDIR` in the Dockerfile to set and maintain the working directory.
   - Avoid `RUN cd` as it only changes the directory for a single command.

3. **Docker Ignore**:
   - Add irrelevant files and directories to `.dockerignore` to reduce the image size.
   - Use `*/` for files in any directory one level below the root, and `**/` for files in any directory at any level.

4. **Building Docker Image**:
  -  ```docker build -t tldr-news-summarizer:latest .```
      - ```-t``` flag tags the image with a name
      - ```tldr-news-summarizer```: name assigned to the image
      - ```latest```: tag for the image, indicating that it is a most recent version of an image
5. **Running Docker Container**
  -  ```docker run -d -p 3000:3000 \ --env-file /path/to/your/env/file \ --name tldr-news-summarizer \ tldr-news-summarizer:latest```
     - ```-d```: flag that runs the container in detached mode (container runs in the background and doesn't block the terminal
     - ```--name tldr-news-summarizer```: container name
     - ```tldr-news-summarizer:latest```: specifies the Docker image to use for the container
