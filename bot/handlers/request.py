from cProfile import run
import logging

from telegram.ext import MessageHandler, CallbackQueryHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
import bot.configs as vars

logging.getLogger(__name__).setLevel(logging.INFO)



# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID
GROUP_ID = vars.REQUEST_GROUP_ID
CHANNEL_ID = vars.REQUEST_CHANNEL_ID
CHANNEL_LINK = vars.REQUEST_CHANNEL_LINK

ON_REQUEST = "*👋Hello *[{}](tg://user?id={})*\n\n🔹Your Request for {} has been submitted to Admins.\n\n🔹Your Request Will Be Uploaded Soon.\n\n🔹Admins Might Be Busy. So, This Can Take Some Time⏳.\n\n👇Check Your Request Status Here👇*"
REQUEST = "*Request By *[{}](tg://user?id={})*\n\nRequest: {}*"
IF_REQUEST_EMPTY = "<b>👋Hello <a href='tg://user?id={}'>{}</a>\nYour Request is Empty.\nTo Request Use:👇</b>\n<code>#request &lt;Your Request&gt;</code>"



# ADDING HANDLERS
def add_request_handlers(bot):
    bot.add_handler(
        MessageHandler(filters=Filters.chat(GROUP_ID) & Filters.entity("hashtag"), callback=user_request, run_async=True)
    )

    bot.add_handler(
        CallbackQueryHandler(pattern="done", callback=done, run_async=True)
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
        inline_keyboard1 = [[InlineKeyboardButton("Request Message💬", url=update.message.link)],[InlineKeyboardButton("🚫Reject", callback_data="hell"), InlineKeyboardButton("Done✅", callback_data="done")]]
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
    original_text = update.callback_query.message.text_markdown_v2
    update.callback_query.message.edit_text(
        text = f"*COMPLETED✅\n\n*~{original_text}~",
        parse_mode = "markdownv2"
    )