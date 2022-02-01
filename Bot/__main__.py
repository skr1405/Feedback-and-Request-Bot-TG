# Importing Required Modules
import logging
import os

from pyrogram import Client, idle, filters
from os import environ



if __name__ == "__main__":
    # Logging Stuff
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
        )
    logging.getLogger("pyrogram").setLevel(logging.ERROR)


    BOT_TOKEN = environ.get("BOT_TOKEN")
    API_ID = environ.get("API_ID")
    API_HASH = environ.get("API_HASH")

    app = Client(
        "Feedback and Request Bot",
        API_ID,
        API_HASH,
        bot_token = BOT_TOKEN,
        plugins = dict(root="Handlers")
    )

    @app.on_message(filters.command("start") & filters.private)
    async def start(client, message):
        await client.send_message(message.chat.id, "Hello")

    app.start()
    logging.info("Pyrogram Client Started...✅")
    for root, dir, files in os.walk("Handlers"):
        logging.info(root)
        logging.info(dir)
        logging.info(files)
    idle()
    app.stop()