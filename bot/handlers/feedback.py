import logging

from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import bot.configs as vars

logging.getLogger(__name__).setLevel(logging.INFO)


# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID

LOG_TEXT = "ID: <code>{}</code>\nName: <a href='tg://user?id={}'>{}{}</a>\nStarted the bot..."
START_TEXT = "You Can Give Feedback and Contact Admins by Sending Messages to Me..."
MESSAGE = "<b>Message from:</b> <code>{}</code>\n<b>Name:</b> <a href='tg://user?id={}'>{}{}</a>\n\n{}"


# ADDING HANDLERS
def add_feedback_handlers(bot):
    bot.add_handler(
        CommandHandler(command="start", callback=start, filters=Filters.chat_type.private, run_async=True)
    )

    bot.add_handler(
        MessageHandler(filters=Filters.chat(OWNER_ID), callback=reply, run_async=True)
    )

    bot.add_handler(
        MessageHandler(filters=Filters.chat_type.private, callback=user, run_async=True)
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

def reply(update, context):
    if update.message.reply_to_message is not None:
        replied_to = update.message.reply_to_message
        try:
            reference_id = replied_to.text.split()[2]
        except Exception:
            reference_id = replied_to.caption.split()[2]

        if update.message.text != None:
            context.bot.send_message(
                text=update.message.text_html,
                chat_id=int(reference_id),
                parse_mode = "html"
            )
        else:
            update.message.copy(
                caption=update.message.caption_html,
                chat_id=int(reference_id),
                parse_mode = "html"
            )
        update.message.reply_text(
            text = "Message Sent...✅",
            quote = True
        )

def user(update, context):
    info = update.message.from_user
    reference_id = info.id
    if update.message.text != None:
        context.bot.send_message(
            chat_id = OWNER_ID,
            text = MESSAGE.format(reference_id, reference_id, info.first_name, "" if info.last_name == None else " "+info.last_name, update.message.text_html),
            parse_mode = "html"
        )
    else:
        update.message.copy(
            chat_id = OWNER_ID,
            caption = MESSAGE.format(reference_id, reference_id, info.first_name, "" if info.last_name == None else " "+info.last_name, update.message.caption_html if update.message.caption_html is not None else ""),
            parse_mode = "html"
        )