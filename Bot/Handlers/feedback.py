from http import client
from pyrogram import Client, filters


@Client.on_message(filters.command("start") & filters.private)
def start(client, message):
    client.send_message(message.from_user, "Hello")
    