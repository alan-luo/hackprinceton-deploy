from flask import Flask, render_template
from newsapi import NewsApiClient
import math
import datetime
import json
import re

app = Flask(__name__)

@app.route('/')
def main():
    articles = []
    messages = []
    for topic in top_topics:
        articles.append(get_topic(topic))
        messages.append("<a href='/topic/"+topic+"'>topic: <b>"+topic+"</b></a>")

    return "hello"

if __name__ == '__main__':
    app.run()
