# Importing Required Modules
import logging

from pyrogram import Client
from os import environ

# Logging Stuff
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(threadName)s %(name)s %(message)s",
    )
logging.getLogger("pyrogram").setLevel(logging.ERROR)

BOT_TOKEN = environ.get("BOT_TOKEN")
API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")

app = Client("Feedback and Request Bot", bot_token=BOT_TOKEN)
app.start()


app.send_message(environ.get("OWNER_ID"), "heLLO")







