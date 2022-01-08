"""
    Basic handler functions
"""
from telegram import Update
from telegram.ext import CallbackContext

from .utils import update_message

def start(update: Update, context: CallbackContext):
    """Start will listen to the /start command and send a message to the user"""
    if update.message is not None:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="I am the tweet bot. Send me a message and I will tweet it for you!"
        )
    else:
        update_message(update, context, "start")

def test(update: Update, context: CallbackContext):
    """Test function to test the bot"""
    if update.message is not None:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="This command does nothing, it is for testing purposes only."
        )
    else:
        update_message(update, context, "test")
