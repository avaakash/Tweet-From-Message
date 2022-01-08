# Tweet From Message
This application will tweet anything you forward to your Telegram bot.
- How to create Telegram Bot: [Telegram Botfather](https://core.telegram.org/bots#6-botfather)
- How to get Twitter API keys: [Twitter API docs](https://developer.twitter.com/en/docs/twitter-api)

### Steps to Run
1. Give the tokens and keys to the env.json file (a sample is given, follow that naming convention only)
2. Run the start.sh script (or you can run the main.py file)
3. Send a message to bot and it will tweet it.
4. Run stop.sh to stop the bot server

### Telegram bot commands
- /start: displays an info message
- \<tweet\>: tweets the message
- /delete: deletes the last tweet done through the bot
- /comment \<tweet\>: adds a comment to the last tweet done through the bot

*Note*: change "\<tweet\>" with your tweet message

### Security
The bot will only respond to specified telegram user ids only. Enter your telegram user ids in the env.json file. 
## Upcoming Features
- Option to reply to comment tweet
- Option to reply to any of the last 7 tweets
- Last 7 tweet stats
- Popular hashtag auto-addition
- Option to like all retweets of the last 7 tweets