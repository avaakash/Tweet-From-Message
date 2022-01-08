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
import validation as check

# Setting up the logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Global object to store last tweet data
tweet = models.Tweet(None, "", [])

def get_secret():
    """Fetches the secrets"""
    environ_secrets = get_env()
    return environ_secrets["telegram_secret"]

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

def start(update: Update, context: CallbackContext):
    """Start will listen to the /start command and send a message to the user"""
    if update.message is not None:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I am the tweet bot. Send me a message and I will tweet it for you!"
        )
    else:
        update_message(update, context, "start")

@check.restricted
def test(update: Update, context: CallbackContext):
    """Test function to test the bot"""
    if update.message is not None:
        print(check.check_tweet_length(update.message.text))
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="Test\n" + update.message.text)
    else:
        update_message(update, context, "test")


@check.restricted
def get_tweet_text(update: Update, context: CallbackContext):
    """get_tweet_text will get the text from the message and tweet it"""
    if update.message is not None:
        print("Message: " + update.message.text)
        if not check.check_tweet_length(update.message.text):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet too long!")
            return
        try:
            tweet.tweet_id, tweet.text = twitter.tweet(update.message.text)
            message = "Tweeted: " + tweet.text
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        except Exception as error:
            print(error)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text="Something went wrong!" + str(error))
    else:
        update_message(update, context)

def delete_tweet(update: Update, context: CallbackContext):
    """Delete a tweet command"""
    if update.message is not None:
        print(tweet.tweet_id, tweet.text, sep="\n")
        if tweet.tweet_id is not None:
            twitter.delete_tweet(tweet.tweet_id)
            tweet.tweet_id = None
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tweet deleted!")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No tweet to delete!")
    else:
        update_message(update, context, "delete")

def bot():
    """Main function to start the bot"""
    # Setting up the updater
    updater = Updater(token=get_secret(), use_context=True)
    # Setting up the dispatcher
    dispatcher = updater.dispatcher

    # Handlers
    start_handler = CommandHandler('start', start)
    message_handle = MessageHandler(Filters.text & ~Filters.command, get_tweet_text)
    delete_handle = CommandHandler('delete', delete_tweet)
    test_handle = CommandHandler('test', test)

    # Adding handlers to the dispatcher
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(message_handle)
    dispatcher.add_handler(delete_handle)
    dispatcher.add_handler(test_handle)

    # Starting the bot
    updater.start_polling()
