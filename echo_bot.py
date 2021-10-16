

import logging,pickle,pytube
import os
import shutil
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from pytube import YouTube
import instaloader
"""bot files """
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer
"""ends"""
#chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
#trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
#trainer.train("chatterbot.corpus.english")
# Get a response to an input statement

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
    update.message.reply_text('I only give replay if you mention me with my tag "@lostlover_bot" 😋')

def who(update, context):
    update.message.reply_text('iam a super duper bot to bring to hell')


def echo(update, context):
    """Echo the user message."""
    print(update.message.chat.first_name,":",update.message.text)
    """user input"""
    user_input=update.message.text
    """BOT REPLY """
    #bot_reply=user_input.replace("@lostlover_bot",'')
    #fullstring = update.message.text
    #substring = "@lostlover_bot"
    #if substring in fullstring:
    #    print("Found!")
     #   update.message.reply_text(bot_reply)
    #else:
     #   print(" @lostlover_bot Not found!")
    """update.message.reply_text(update.message.text)"""
    """update.message.replay_text()"""
    


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def spam(update, context):
    for i in range(3):
        update.message.reply_text("spamming....")

def morning(update, context):
    fullstring = update.message.text
    substring = "morning" or "Morning" or "mrng" or "Mrng"
    if substring in fullstring:
        print("said good morning")
        update.message.reply_text("good morning")
    else:
        print(" nothing to deal with..")

def chatai(update, context):
    answer = chatbot.get_response(update.message.text)
    print(answer)
    response_data = str(answer)
    update.message.reply_text(response_data)

######################## The downloader ########################################

def ytdl(update , context):
    link = update.message.text.split()
    ####################VARIABLES#######################
    try:yturl = link[1]
    except:
        update.message.reply_text("missed link? or wrong link?")
        update.message.reply_text("Format :  /ytdl <youtube  link> ")
    save_path = "ytdl/"
    ####################################################
    


    update.message.reply_text("Currently under construction.... ")
    update.message.reply_text("Sorry for the in conviniance occured.")


#################################################################################


################################ Instagram DP downloader #################################################
#Source : instaloader

def instadp(update , context):
    tmp= update.message.text.split()
    username = tmp[1]
    update.message.reply_text("Downloading instagram profile picture of username: "+username)
    ig = instaloader.Instaloader(dirname_pattern="dpfolder/",filename_pattern=None,title_pattern=username)
    dp = username
    ig.download_profile(dp , profile_pic_only=True)
    chatid=update.message.chat.id
    directory_path = os.getcwd()
    filepath = directory_path+"/dpfolder/"+username+".jpg"
    update.message.reply_document(open(filepath, 'rb'))
    pathtoremove = "dpfolder"
    shutil.rmtree(pathtoremove, ignore_errors=False, onerror=None)
    fromuser = update.message.chat.username
    print("Profile pic requested by "+fromuser+" is successfully uploaded..")
    update.message.reply_text("Done.")
    



#################################################################################
def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("who", who))
    dp.add_handler(CommandHandler("spam", spam))
    dp.add_handler(CommandHandler("ytdl", ytdl))
    dp.add_handler(CommandHandler("instadp", instadp))

    # on noncommand i.e message - echo the message on Telegram
    """dp.add_handler(MessageHandler(Filters.text, echo))"""
    dp.add_handler(MessageHandler(Filters.text, morning))
    #dp.add_handler(MessageHandler(Filters.text, chatai))

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
