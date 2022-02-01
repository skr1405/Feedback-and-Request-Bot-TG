import logging
from pyrogram import Client, filters
import pyrogram

logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
        )
logging.getLogger(pyrogram)

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await client.send_message(message.chat.id, "Hello")
    