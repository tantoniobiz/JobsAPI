# JobsAPI
This is a project to create an open API for job tracking and job searching. The goal of the API is to provide job data to new and innovative job search tools that help people get jobs after getting laid off due to Covid.

jobs.py - Currently this file is setup as a webscraping POC for a career page
There will two parts to this file (Work in progress):
1. A script that scrapes career pages and stores job data.
2. A REST API that will serve up company level and job level details as well as take requests to track specific career pages.

Stack:
Python
  BeautifulSoup - Webscraping
  Requests - Making requests to the career pages
  SQLAlchemy - To make querying the database easier
  Jsonify - To create the Rest APIs
  
 DB - I have not decided on a database yet, open to suggestions here.
  
Here is a Postman Collection and Docs for the API:
https://documenter.getpostman.com/view/11326734/Szme5Jou

Here is a working list of career pages the API is tracking:
https://docs.google.com/spreadsheets/d/1PZ5LP3xV5NDlYaQ-O7rkwBFLjaB7bz8NqZs0vHBU-Bk/edit?usp=sharing

Trello board for tasks:
https://trello.com/b/UEDQSk4s/jobs-api
