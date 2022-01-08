"""
    Handler function for tweets
"""
import logging

from telegram import Update
from telegram.ext import CallbackContext
import tweepy

from validation import restricted, check_tweet_length

from twitter import twitter

from redis_py import database

from .utils import update_message, get_tweet_url


@restricted
def send_tweet(update: Update, context: CallbackContext):
    """get_tweet_text will get the text from the message and tweet it"""
    if update.message is not None:
        logging.info("Message Received: %s", update.message.text)
        if not check_tweet_length(update.message.text):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet too long!")
            return
        try:
            tweet_id, text = twitter.tweet(update.message.text)
            logging.info("Tweet sent: %s", text)
            database.set_tweet(tweet_id, text)
            message = f"Tweeted: {text}\n{get_tweet_url(tweet_id)}"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        except tweepy.errors.BadRequest as error:
            logging.error(str(error))
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Something went wrong!" + str(error))
    else:
        update_message(update, context)

@restricted
def delete_tweet(update: Update, context: CallbackContext):
    """Delete a tweet command"""
    if update.message is not None:
        tweet_id, tweet_text = database.get_tweet()
        logging.info("Tweet Data in Redis: %s - %s", tweet_id, tweet_text)
        if tweet_id is not None:
            twitter.delete_tweet(tweet_id)
            database.delete_tweet()
            logging.info("Tweet Deleted")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet deleted!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No tweet to delete!")
    else:
        update_message(update, context, "delete")

@restricted
def comment_tweet(update: Update, context: CallbackContext):
    """Tweets as a comment to the last tweet"""
    if update.message is not None:
        tweet_id, tweet_text = database.get_tweet()
        logging.info("Tweet Data in Redis: %s - %s", tweet_id, tweet_text)
        if tweet_id is not None:
            try:
                # Send tweet
                tweet_message = " ".join(context.args)
                reply_tweet_id, reply_text = twitter.reply_to_tweet(
                    tweet_message, tweet_id=tweet_id)
                logging.info("Tweet reply sent: %s", reply_text)
                # Setup message for bot
                message = f"{reply_text}\n{get_tweet_url(reply_tweet_id)}"
                message = message + f"\n\nIn reply to: {get_tweet_url(tweet_id)}\n{tweet_text}"
                context.bot.send_message(chat_id=update.effective_chat.id, text=message)
            except tweepy.errors.BadRequest as error:
                logging.error(str(error))
                context.bot.send_message(
                    chat_id=update.effective_chat.id, text=str(error))
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="No tweet to comment to!")
    else:
        update_message(update, context, "comment")
