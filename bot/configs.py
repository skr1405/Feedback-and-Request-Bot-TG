from os import environ

BOT_TOKEN = environ.get("BOT_TOKEN")
BASE_URL_OF_BOT = environ.get("BASE_URL_OF_BOT")
PORT = int(environ.get("PORT", "8443"))
OWNER_ID = int(environ.get("OWNER_ID"))
GROUP_LINK = environ.get("GROUP_LINK")
CHANNEL_LINK = environ.get("CHANNEL_LINK")
REQUEST_GROUP_ID = int(environ.get("REQUEST_GROUP_ID"))
REQUEST_CHANNEL_ID = int(environ.get("REQUEST_CHANNEL_ID"))
REQUEST_CHANNEL_LINK = int(environ.get("REQUEST_CHANNEL_LINK"))