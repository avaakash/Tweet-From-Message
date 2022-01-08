"""
    Telegram Bot
"""
import logging

# Importing telegram python module
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

# Importing app modules
from settings import get_env
from twitter import twitter, models

# Setting up the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Global object to store last tweet data
tweet = models.Tweet(None, "", [])

def get_secret():
    """
        Fetches the secrets
    """
    environ_secrets = get_env()
    return environ_secrets["telegram_secret"]

def start(update: Update, context: CallbackContext):
    """
        Start will listen to the /start command and send a message to the user
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I am the tweet bot. Send me a message and I will tweet it for you!"
    )

def get_tweet_text(update: Update, context: CallbackContext):
    """
        get_tweet_text will get the text from the message and tweet it
    """
    print("Message: " + update.message.text)
    try:
        tweet.tweet_id, tweet.text = twitter.tweet(update.message.text)
        message = "Tweeted: " + tweet.text
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    except Exception as error:
        print(error)
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Something went wrong!" + str(error))

def delete_tweet(update: Update, context: CallbackContext):
    """
        Delete a tweet command
    """
    print(tweet.tweet_id, tweet.text, sep="\n")
    if tweet.tweet_id is not None:
        twitter.delete_tweet(tweet.tweet_id)
        tweet.tweet_id = None
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet deleted!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="No tweet to delete!")

def main():
    """
        Main function to start the bot
    """
    # Setting up the updater
    updater = Updater(token=get_secret(), use_context=True)
    # Setting up the dispatcher
    dispatcher = updater.dispatcher

    # Handlers
    start_handler = CommandHandler('start', start)
    message_handle = MessageHandler(Filters.text & ~Filters.command, get_tweet_text)
    delete_handle = CommandHandler('delete', delete_tweet)

    # Adding handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handle)
    dispatcher.add_handler(delete_handle)

    # Starting the bot
    updater.start_polling()

if __name__ == '__main__':
    main()
