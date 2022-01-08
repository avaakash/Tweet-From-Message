"""
    Twitter bot to tweet messages
"""
from .auth import authenticate

# Authenticating the twitter API client
api = authenticate()

def tweet(message) -> int:
    """Tweet a message"""
    tweet_data = api.update_status(message)
    return tweet_data.id, tweet_data.text

def delete_tweet(tweet_id):
    """Delete a tweet"""
    api.destroy_status(id=tweet_id)

def reply_to_tweet(message, tweet_id):
    """Reply to a tweet"""
    tweet_data = api.update_status(
        message, in_reply_to_status_id=str(tweet_id), auto_populate_reply_metadata=True
    )
    return tweet_data.id, tweet_data.text
