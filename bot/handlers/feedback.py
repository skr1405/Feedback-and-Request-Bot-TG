import logging

from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from bot.configs import Config as vars

logging.getLogger(__name__).setLevel(logging.INFO)


# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID

LOG_TEXT = "ID: <code>{}</code>\nName: <a href='tg://user?id={}'>{}{}</a>\nStarted the bot..."
START_TEXT = "You Can Give Feedback and Contact Admins by Sending Messages to Me..."
IF_TEXT = "<b>Message from:</b> {}\n<b>Name:</b> {}\n\n{}"



def add_feedback_handlers(bot):
    bot.add_handler(
        CommandHandler(command="start", callback=start, filters=Filters.chat_type.private, run_async=True)
    )

    bot.add_handler(
        MessageHandler(filters=Filters.chat_type.private & Filters.text, callback=pm_text, run_async=True)
    )

















#***************HANDLERS BELOW******************

def start(update, context):
    context.bot.send_message(
        chat_id = OWNER_ID,
        text = LOG_TEXT.format(update.message.chat.id,update.message.chat.id,update.message.chat.first_name,"" if update.message.chat.last_name == None else " "+update.message.chat.last_name),
        parse_mode = "html"
    )
    inline_keyboard = [[InlineKeyboardButton("💬GROUP💬", url = f"{vars.GROUP_LINK}"), InlineKeyboardButton("📢CHANNEL📢", url = f"{vars.CHANNEL_LINK}")]]
    update.message.reply_text(
        "*Hi {}!*\n".format(update.message.chat.first_name)+START_TEXT,
        reply_markup = InlineKeyboardMarkup(inline_keyboard),
        parse_mode = "markdown"
    )

def pm_text(update, context):
    info = update.message.from_user
    reference_id = info.id
    update.message.copy(
        chat_id = OWNER_ID,
        caption = IF_TEXT.format(reference_id, info.first_name, update.message.text),
        parse_mode = "html"
    )

