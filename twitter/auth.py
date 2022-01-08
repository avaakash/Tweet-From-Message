"""
    Performs twitter API authentication
"""
import logging
import tweepy
from utils.settings import get_env

def authenticate():
    """Authenticates the twitter API"""
    # Getting the tokens and keys
    environ_secrets = get_env()
    # Setting up variables
    consumer_key = environ_secrets["twitter_consumer_key"]
    consumer_secret = environ_secrets["twitter_consumer_secret"]
    access_token = environ_secrets["twitter_token"]
    access_token_secret = environ_secrets["twitter_secret"]

    # Creating Auth object
    auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)
    # Setting access token to access API
    auth.set_access_token(access_token, access_token_secret)

    # Getting the API object to make API calls
    api = tweepy.API(auth)

    # Verifying API and returning the API object
    try:
        api.verify_credentials()
        logging.info("Twitter API Verified")
        return api
    except tweepy.errors.Unauthorized:
        logging.error("Wrong Twitter API Credentials")
        return None
