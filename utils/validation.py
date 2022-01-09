"""
    Validation and Security checks
"""
from functools import wraps
import logging

from settings import get_env

def restricted(func):
    """Restrict usage of func to allowed users only"""
    allowed_ids = get_env()["telegram_allowed_ids"]
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = str(update.effective_user.id)
        if user_id not in allowed_ids:
            logging.warning("Unauthorized access denied for %s", user_id)
            update.message.reply_text('You are not allowed to use this bot! Please leave.')
            return None
        return func(update, context, *args, **kwargs)
    return wrapped

def check_tweet_length(tweet):
    """ Checks if the tweet is within the allowed length"""
    logging.info("Tweet Length: %s", str(len(tweet)))
    if len(tweet) > 240:
        return False
    return True
