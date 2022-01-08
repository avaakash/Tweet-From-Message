"""
    Database actions
"""

from .connect import connect

redis_connect = connect()

def set_tweet(tweet_id, tweet_text):
    """Set a tweet in redis"""
    redis_connect.set("tweet_id", tweet_id)
    redis_connect.set("tweet_text", tweet_text)

def get_tweet():
    """Get a tweet from redis"""
    return (redis_connect.get("tweet_id").decode('UTF-8'),
        redis_connect.get("tweet_text").decode('UTF-8'))

def delete_tweet():
    """Delete a tweet from redis"""
    redis_connect.delete("tweet_id", "tweet_text")

def set_tweet_list(tweet_id):
    """Set a list of tweets in redis"""
    redis_connect.lpush("tweet_list", tweet_id)

def get_latest_tweet_list():
    """Get the latest tweet from redis"""
    return redis_connect.lrange("tweet_list", 0, -1)

def remove_last_tweet():
    """Remove the latest tweet from redis"""
    redis_connect.lpop("tweet_list")
