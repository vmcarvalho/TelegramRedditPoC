import praw

from telegram import InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

platform = 'python'
appId = 'telegramRedditBot'
user_agent = platform + ':' + appId + ':' 'v0.1' + '(by /u/victorcarvalho)'
telegram_token = open("telegram.ini","r").read()


#bot = telegram.Bot(telegram_token)
def start(bot, update):
	reply_message = 'Retrieving hot topics...\n'

	for submission in  reddit.subreddit('brasil').hot(limit=4):
		reply_message = reply_message + submission.title + ' ' + submission.shortlink + '\n'

	update.message.reply_text(reply_message)
   
def help(bot, update):
	update.message.reply_text("Use /start to test this bot.")

reddit = praw.Reddit(appId, user_agent = user_agent)

# Create the Updater and pass it your bot's token.
updater = Updater(telegram_token)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))

# Start the Bot
updater.start_polling()

# Run the bot until the user presses Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT
updater.idle()