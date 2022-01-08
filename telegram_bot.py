"""
    Telegram Bot
"""
import logging

# Importing telegram python module
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Importing app modules
from twitter import models
import telegram_handler.utils as utils
import telegram_handler as handler

# Setting up the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Global object to store last tweet data
tweet = models.Tweet(None, "", [])

def bot():
    """Main function to start the bot"""
    # Setting up the updater
    updater = Updater(token=utils.get_secret(), use_context=True)
    # Setting up the dispatcher
    dispatcher = updater.dispatcher

    # Handlers
    start_handler = CommandHandler('start', handler.start)
    message_handle = MessageHandler(Filters.text & ~Filters.command, handler.send_tweet)
    delete_handle = CommandHandler('delete', handler.delete_tweet)
    comment_handle = CommandHandler('comment', handler.comment_tweet, pass_args=True)
    test_handle = CommandHandler('test', handler.test)

    # Adding handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handle)
    dispatcher.add_handler(delete_handle)
    dispatcher.add_handler(test_handle)
    dispatcher.add_handler(comment_handle)

    # Starting the bot
    updater.start_polling()
