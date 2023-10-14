import requests
from bs4 import BeautifulSoup
import re
from textblob import TextBlob
import nltk

# Specify the URL of the Wikipedia page you want to scrape
url = 'https://en.wikipedia.org/wiki/Data_science'

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the paragraphs (usually in <p> tags) containing text on the page
    paragraphs = soup.find_all('p')

    # Initialize a list to store sentences from the scraped text
    sentences = []

    # Loop through each paragraph and extract text
    for paragraph in paragraphs:
        text = paragraph.text

        # Tokenize the text into sentences using TextBlob
        blob = TextBlob(text)
        for sentence in blob.sentences:
            sentences.append(sentence)

    # Perform sentiment analysis on each sentence
    sentiment_scores = []
    for sentence in sentences:
        sentiment = sentence.sentiment
        sentiment_scores.append(sentiment.polarity)

    # Calculate the average sentiment score
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores)

    # Print the average sentiment score
    print(f"Average Sentiment Score: {avg_sentiment}")

else:
    print(f'Failed to fetch the Wikipedia page. Status code: {response.status_code}')


