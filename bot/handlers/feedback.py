import logging

from telegram.ext import CommandHandler, Filters
from bot.configs import Config as vars

logging.getLogger(__name__)


def add_feedback_handlers(bot):
    bot.add_handler(CommandHandler("start", start, filters=Filters.private, run_async=True))

# IMPORTANT VARIABLES
OWNER_ID = vars.OWNER_ID

LOG_TEXT = "ID: <code>{}</code>\nName: <a href='tg://user?id={}'>{}{}</a>\nDC ID: <code>{}</code>"
START_TEXT = "You Can Give Feedback and Contact Admins by Sending Messages to Me..."


def start(update, context):
    context.bot.send_message(update.message.chat.id, "HEllo")


'''
# MAIN STUFF
@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await bot.send_message(
        chat_id=owner_id,
        text=LOG_TEXT.format(message.chat.id,message.chat.id,message.chat.first_name,"" if message.chat.last_name == None else " "+message.chat.last_name,message.chat.dc_id),
        parse_mode="html"
    )
    await message.reply_text(
        text="**Hi {}!**\n".format(message.chat.first_name)+START_TEXT,
        reply_markup=InlineKeyboardMarkup([
            [ InlineKeyboardButton(text="JOIN GROUP", url=f"{vars.GROUP_LINK}"), InlineKeyboardButton(text="JOIN CHANNEL", url=f"{vars.CHANNEL_LINK}")]
        ])
    )

'''