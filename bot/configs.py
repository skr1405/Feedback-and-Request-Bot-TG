# -*- coding: utf-8 -*-
from os import environ

class Config:

    BOT_TOKEN = environ.get("BOT_TOKEN")
    BASE_URL_OF_BOT = environ.get("BASE_URL_OF_BOT")
    PORT = int(environ.get("PORT", "8443"))
    OWNER_ID = int(environ.get("OWNER_ID"))
    GROUP_LINK = environ.get("GROUP_LINK")
    CHANNEL_LINK = environ.get("CHANNEL_LINK")