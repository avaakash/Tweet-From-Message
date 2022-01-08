"""
    Twitter response classes
"""
class Tweet:
    """
        Tweet object
    """
    def __init__(self, tweet_id, text, hashtags):
        self.tweet_id = tweet_id
        self.text = text
        self.hashtags = hashtags
    def __str__(self):
        return f"Tweet ID: {self.tweet_id}\nText: {self.text}"
    def get_text(self):
        """
            Returns the text of the tweet
        """
        return self.text
    def get_tweet_id(self):
        """
            Returns the id of the tweet
        """
        return self.tweet_id
    def get_hashtags(self):
        """
            Returns the hashtags in the tweet
        """
        return self.hashtags
