import logging
import re

from telegram.ext import MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import bot.configs as vars

logging.getLogger(__name__).setLevel(logging.INFO)



# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID
GROUP_ID = vars.REQUEST_GROUP_ID
CHANNEL_ID = vars.REQUEST_CHANNEL_ID
CHANNEL_LINK = vars.REQUEST_CHANNEL_LINK
REQUEST_COMPLETE_TEXT = vars.REQUEST_COMPLETE_TEXT

ON_REQUEST = "*👋Hello *[{}](tg://user?id={})*\n\n🔹Your Request for {} has been submitted to Admins.\n\n🔹Your Request Will Be Uploaded Soon.\n\n🔹Admins Might Be Busy. So, This Can Take Some Time⏳.\n\n👇Check Your Request Status Here👇*"
REQUEST = "*Request By *[{}](tg://user?id={})*\n\nRequest: {}*"
ON_DONE = "*Dear *[{}](tg://user?id={})*😎\n\nYour Request for{} is Completed🥳{}\n\n👍Thanks for Requesting\!*"
ON_REJECT = "Dear *[{}](tg://user?id={})*😎\n\nYour Request for{} is Rejected😥\n\nReason: {}\n\n👍Thanks for Requesting\!*"
IF_REQUEST_EMPTY = "<b>👋Hello <a href='tg://user?id={}'>{}</a>\nYour Request is Empty.\nTo Request Use:👇</b>\n<code>#request &lt;Your Request&gt;</code>"



# ADDING HANDLERS
def add_request_handlers(bot):
    bot.add_handler(
        MessageHandler(filters=Filters.chat(GROUP_ID) & Filters.entity("hashtag"), callback=user_request, run_async=True)
    )

    bot.add_handler(
        CallbackQueryHandler(pattern="done", callback=done, run_async=True)
    )

    bot.add_handler(
        CallbackQueryHandler(pattern="reject", callback=reject, run_async=True)
    )

    bot.add_handler(
        CallbackQueryHandler(pattern="completed", callback=completed, run_async=True)
    )





#***************HANDLERS BELOW******************

def user_request(update, context):
    if update.message.text.lower() == "#request":
        info = update.message.from_user
        update.message.reply_text(
            text = IF_REQUEST_EMPTY.format(info.id, info.first_name),
            quote = False,
            parse_mode = "html"
        )
        return
    if update.message.text.lower().startswith("#request"):
        info = update.message.from_user
        message = update.message.text[8:].strip()
        inline_keyboard1 = [[InlineKeyboardButton("Request Message💬", url=update.message.link)],[InlineKeyboardButton("🚫Reject", callback_data="reject"), InlineKeyboardButton("Done✅", callback_data="done")]]
        context.bot.send_message(
            chat_id = CHANNEL_ID,
            text = REQUEST.format(info.first_name, info.id, message),
            reply_markup = InlineKeyboardMarkup(inline_keyboard1),
            parse_mode = "markdown"
        )
        inline_keyboard2 = [[InlineKeyboardButton("⏳REQUEST STATUS⏳", url=CHANNEL_LINK)]]
        update.message.reply_text(
            text = ON_REQUEST.format(info.first_name, info.id, message),
            quote = False,
            reply_markup = InlineKeyboardMarkup(inline_keyboard2),
            parse_mode = "markdown"
        )


#**************CALLBACK HANDLERS*****************

def done(update, context):
    user_info = update.callback_query.from_user
    user_status = context.bot.get_chat_member(CHANNEL_ID, user_info.id).status
    if (user_status == "creator") or (user_status == "administrator"):
        original_text = update.callback_query.message.text_markdown_v2
        inline_keyboard = [[InlineKeyboardButton("Request Completed✅", callback_data="completed")]]
        update.callback_query.message.edit_text(
            text = f"*COMPLETED✅\n\n*~{original_text}~",
            reply_markup = InlineKeyboardMarkup(inline_keyboard),
            parse_mode = "markdownv2"
        )
        details = re.match(r".*\[(.*)\].*id=(\d+)", original_text)
        context.bot.send_message(
            chat_id = GROUP_ID,
            text = ON_DONE.format(details.group(1), details.group(2), "\n".join(original_text.split("\n")[2:])[9:-1], ("\n"+REQUEST_COMPLETE_TEXT) if REQUEST_COMPLETE_TEXT != "" else ""),
            parse_mode ="markdownv2"
        )
    else:
        update.callback_query.answer(
            text = "Who the hell are you?\nYou are not Admin😠",
            show_alert = True
        )

def completed(update, context):
    update.callback_query.answer(
        text = f"Request is Completed🥳\n{REQUEST_COMPLETE_TEXT}",
        show_alert = True
    )

def reject(update, context):
    user_info = update.callback_query.from_user
    user_status = context.bot.get_chat_member(CHANNEL_ID, user_info.id).status
    if (user_status == "creator") or (user_status == "administrator"):
        original_text = update.callback_query.message.text_markdown_v2
        reason = "Unavailable"
        inline_keyboard = [[InlineKeyboardButton("Request Rejected🚫", callback_data="rejected")]]
        update.callback_query.message.edit_text(
            text = f"*REJECTED🚫\n\nReason: {reason}\n\n*~{original_text}~",
            reply_markup = InlineKeyboardMarkup(inline_keyboard)
            parse_mode = "markdownv2"
        )
        details = re.match(r".*\[(.*)\].*id=(\d+)", original_text)
        context.bot.send_message(
            chat_id = GROUP_ID,
            text = ON_REJECT.format(details.group(1), details.group(2), "\n".join(original_text.split("\n")[2:])[9:-1], reason),
            parse_mode ="markdownv2"
        )
    else:
        update.callback_query.answer(
            text = "Who the hell are you?\nYou are not Admin😠",
            show_alert = True
        )

def rejected(update, context):
    update.callback_query.answer(
        text = f"Request is Rejected😥",
        show_alert = True
    )