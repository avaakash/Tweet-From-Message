"""
    Utils for the telegram bot
"""
from telegram import Update
from telegram.ext import CallbackContext

from settings import get_env

def get_secret():
    """Fetches the secrets"""
    return get_env()["telegram_secret"]

def get_username():
    """Fetches the username"""
    return get_env()["twitter_username"]

def get_tweet_url(tweet_id):
    """Returns the url of a tweet"""
    return f"t.co/{get_username()}/status/{tweet_id}"

def update_message(update: Update, context: CallbackContext, command: str = None):
    """sends a message if an old message was edited"""
    if command is None:
        message = "You edited an old message."
    else:
        message = f"You edited an old message with the /{command} command."
    return context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )
