import logging
from pyrogram import Client, filters

logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
        )
logging.getLogger(__name__)

@Client.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await client.send_message(message.chat.id, "Hello")
    