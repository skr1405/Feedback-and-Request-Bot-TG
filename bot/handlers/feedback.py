import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from os import environ

logging.getLogger(__name__)

# IMPORTANT VARIABLES
owner_id = environ.get("OWNER_ID")

LOG_TEXT = "ID: <code>{}</code>\nFirst Name: <a href='tg://user?id={}'>{}{}</a>\nDC ID: <code>{}</code>"


# MAIN STUFF
@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await bot.send_message(
        chat_id=owner_id,
        text=LOG_TEXT.format(message.chat.id,message.chat.id,message.chat.first_name,message.chat.last_name,message.chat.dc_id),
        parse_mode="html"
    )
    await message.reply_text(
        text="**Hi {}!**\n".format(message.chat.first_name)+C.START,
        reply_markup=InlineKeyboardMarkup([
            [ InlineKeyboardButton(text="🛠SUPPORT🛠", url=f"{C.SUPPORT_GROUP}"), InlineKeyboardButton(text="📮UPDATES📮", url=f"{C.UPDATE_CHANNEL}")]
        ])
    )

