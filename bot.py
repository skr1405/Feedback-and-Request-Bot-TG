# Importing Required Modules
import logging
from pyrogram import Client, filters
from os import environ

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    )
logging.getLogger("pyrogram").setLevel(logging.ERROR)

BOT_TOKEN = environ.get("BOT_TOKEN")

app = Client("Feedback and Request Bot", bot_token=BOT_TOKEN)


app.send_message(environ.get("OWNER_ID"), "heLLO")







