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

ON_REQUEST = "sdfjjsdfj"
IF_REQUEST_EMPTY = "<b>Dear <a href='tg://user?id={}'>{}</a>\nYour Request is Empty.\nTo Request Use</b>\n<code>#request \<Your Request\></code>"



# ADDING HANDLERS
def add_request_handlers(bot):
    bot.add_handler(
        MessageHandler(filters=Filters.chat(GROUP_ID) & Filters.entity("hashtag"), callback=user_request, run_async=True)
    )





#***************HANDLERS BELOW******************

def user_request(update, context):
    if update.message.text.lower() == "#request":
        
        info = update.message.from_user
        update.message.reply_text(
            text = IF_REQUEST_EMPTY.format(info.id, info.first_name),
            parse_mode = "html"
        )
    if update.message.text.lower().startswith("#request"):
        update.message.reply_text(
            text = ON_REQUEST
        )