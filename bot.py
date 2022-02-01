from pyrogram import Client, filters
from os import environ


BOT_TOKEN = environ.get("BOT_TOKEN")

app = Client(bot_token=BOT_TOKEN)


app.send_message(environ.get("OWNER_ID"), "heLLO")







