# -*- coding: utf-8 -*-
from os import environ

class Config:

    API_ID = environ.get("API_ID")
    API_HASH = environ.get("API_HASH")
    BOT_TOKEN = environ.get("BOT_TOKEN")
    OWNER_ID = environ.get("OWNER_ID")