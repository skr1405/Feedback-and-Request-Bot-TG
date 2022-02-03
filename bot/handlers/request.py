import logging

from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from bot.configs import Config as vars

logging.getLogger(__name__).setLevel(logging.INFO)



# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID



# ADDING HANDLERS
def add_feedback_handlers(bot):
    pass