import streamlit as st
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from PIL import Image
import seaborn as sns




consumerKey = '37D4EIzLHkrofHjKNfsQFeq4y'
consumerSecret = '404fGNFnFpsIULhIQpXKESh1aVe33Xj2o8ZDQb1uRxexrIcNXe'
accessToken = '1922379596-owUK0H7AdFUZCdNQKdemcQKYb8byvQ3UZdiTyn7'
accessTokenSecret = '6UFaMLxam0iOIaNXHjfItLAzXO8oa4RazYyPIKLuiLEYC'



def app():


	st.title("Real time Tweet Analyzer")
    


	activities=["Tweet Analyzer","Generate Twitter Data"]

	choice = st.sidebar.selectbox("Select Your Activity",activities)
    
    














if __name__ == "__main__":
	app()