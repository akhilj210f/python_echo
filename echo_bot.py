

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('നമസ്കാരം!')
    update.message.reply_text('എന്ത് ഉണ്ട് വിശേഷം 😋')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('എന്ത് സഹായം ആണ് വേണ്ടത്?')
    update.message.reply_text('@Akhil_R143 ചോദിക്ക് അവൻ പറഞ്ഞ് തരും')

def who(update, context):
    update.message.reply_text('iam a super duper bot to bring to hell')


def echo(update, context):
    """Echo the user message."""
    print(update.message.chat.first_name,":",update.message.text)
    """user input"""
    user_input=update.message.text
    """user input ends """
    fullstring = update.message.text
    substring = "@lostlover_bot"
    if substring in fullstring:
        print("Found!")
        update.message.reply_text(user_input)
    else:
        print("Not found!")
    """update.message.reply_text(update.message.text)"""
    """update.message.replay_text()"""
    


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def spam(update, context):
    for i in range(3):
        update.message.reply_text("spamming....")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("865160940:AAGVqhtANhA7Y3X3Gixne8Vf1BNPy1f36UI", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("who", who))
    dp.add_handler(CommandHandler("spam", spam))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    print(Filters.text)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
