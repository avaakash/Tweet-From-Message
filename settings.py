"""
    Contains the global settings for the application.
"""
import json
import os

BASE_DIR = os.path.dirname(__file__)

# To get the file path in base dir
def base(filename):
    """Returns the file path in base dir"""
    return os.path.join(BASE_DIR, filename)

def get_env():
    """Loads the environment variables"""
    environ_secrets = {}
    with open(base("env.json"), encoding='utf-8') as file:
        env = json.load(file)
    environ_secrets["twitter_consumer_key"] = env.get("TWITTER_CONSUMER_KEY", "")
    environ_secrets["twitter_consumer_secret"] = env.get("TWITTER_CONSUMER_SECRET", "")
    environ_secrets["twitter_token"] = env.get("TWITTER_ACCESS_TOKEN", "")
    environ_secrets["twitter_secret"] = env.get("TWITTER_ACCESS_SECRET", "")
    environ_secrets["twitter_username"] = env.get("TWITTER_USERNAME", "")
    environ_secrets["telegram_secret"] = env.get("TELEGRAM_SECRET", "")
    environ_secrets["telegram_allowed_ids"] = env.get("TELEGRAM_ALLOWED_IDS", "")

    return environ_secrets
