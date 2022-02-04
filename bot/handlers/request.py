from cProfile import run
import logging

from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import bot.configs as vars

logging.getLogger(__name__).setLevel(logging.INFO)



# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID
GROUP_ID = vars.REQUEST_GROUP_ID
CHANNEL_ID = vars.REQUEST_CHANNEL_ID

TO_USER = "sdfjjsdfj"



# ADDING HANDLERS
def add_request_handlers(bot):
    bot.add_handler(
        MessageHandler(filters=Filters.chat(GROUP_ID) & Filters.regex("#request "), callback=user_request, run_async=True)
    )





#***************HANDLERS BELOW******************

def user_request(update, context):
    update.message.reply_text(
        text = To_USER
    )