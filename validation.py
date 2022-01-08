"""
    Validation and Security checks
"""
from functools import wraps

from settings import get_env

def restricted(func):
    """Restrict usage of func to allowed users only and replies if necessary"""
    allowed_ids = get_env()["telegram_allowed_ids"]
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = str(update.effective_user.id)
        if user_id not in allowed_ids:
            print(f"WARNING: Unauthorized access denied for {user_id}")
            update.message.reply_text('You are not allowed to use this bot! Please leave.')
            return  None # quit function
        return func(update, context, *args, **kwargs)
    return wrapped

def check_tweet_length(tweet):
    """ Checks if the tweet is within the allowed length"""
    print("Tweet Length: " + str(len(tweet)))
    if len(tweet) > 240:
        return False
    return True
