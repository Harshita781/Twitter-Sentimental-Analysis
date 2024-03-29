# Twitter-Sentiment-Analysis
A webapp built using streamlit to display the sentiments of people regarding any events happening in the world by analyzing tweets related to that event. 

- It will search for tweets about any topic and analyze each tweet to see whether the emotion is Negtive, Neutral or Positive. 
- It also fetches tweets from the profile of the entered username.
- It also shows a word cloud for easy visualization.

## What does this webapp do
- Can Fetch upto **100 Tweets**.
- Gives a **detailed Analysis** of the tweets.
- Gives the most **trending** **#Hashtag**, **Most used words**,**Wordcloud** and **@mentions** of the fetched tweets.
- Gives the Overall **Sentiment Analysis** of the **Tweets** in form of **graph**.

## Built With

* Python 3.6
* tweepy
* textblob
* matplotlib

## How to run the project

1. Clone this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt]file with the command `pip install -r requirements.txt`
3. Create a file name `config.ini`
4. Paste the code in `config.ini` and insert key details taken from here [developer.twitter.com](https://developer.twitter.com/en)
```
[twitter]
api_key = Your Keys
api_key_secret = Your Keys
access_token = Your Keys
access_token_secret = Your Keys
```
5. Open your terminal/command prompt from your project directory and run the file `app.py` by executing the command `streamlit run app.py`.

## Authors

Harshita Sharma
