"""
    Twitter bot to tweet messages
"""
from .auth import authenticate

# Authenticating the twitter API client
api = authenticate()

def tweet(message) -> int:
    """
        Tweet a message
    """
    tweet_data = api.update_status(message)
    print(tweet_data.id, tweet_data.text, tweet_data.entities["hashtags"], sep="\n")
    return tweet_data.id, tweet_data.text

def delete_tweet(tweet_id):
    """
        Delete a tweet
    """
    api.destroy_status(id=tweet_id)
