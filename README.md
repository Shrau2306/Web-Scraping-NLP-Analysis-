# Web-Scraping-NLP-Analysis-
In one of my projects, I designed a system to perform sentiment analysis on the content of a Wikipedia page, specifically focusing on the 'Data Science' page. The primary aim was to gauge the overall sentiment or tone of the content on that page.

Here's a brief walkthrough:

    Web Scraping: Using the requests library, I fetched the HTML content of the specified Wikipedia page. I then utilized BeautifulSoup to parse this content.
    Text Extraction: I focused on extracting text from the paragraphs, typically enclosed within <p> tags. This ensured I was capturing the main content and not any metadata or extraneous text.
    Text Tokenization: To break down the content into individual sentences, I used the TextBlob library, which also facilitated the subsequent sentiment analysis.
    Sentiment Analysis: For each extracted sentence, I computed a sentiment score, which ranges from -1 (negative sentiment) to 1 (positive sentiment).
    Result: I then calculated the average sentiment score for the entire page to provide a holistic view of the content's sentiment.

The final output is the average sentiment score, indicating whether the 'Data Science' Wikipedia page is written with a positive, negative, or neutral tone
