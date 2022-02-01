import logging
from pyrogram import Client, filters


logging.getLogger(__name__)

@Client.on_message(filters.command("ye") & filters.private)
async def start(client, message):
    await client.send_message(message.chat.id, "Hello")