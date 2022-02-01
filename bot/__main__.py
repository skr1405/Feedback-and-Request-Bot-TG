# Importing Required Modules
import logging

from pyrogram import Client, idle, filters
from configs import Config as vars



if __name__ == "__main__":
    # Logging Stuff
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)s %(name)s %(message)s",
        )
    logging.getLogger("pyrogram").setLevel(logging.WARNING)


    BOT_TOKEN = vars.BOT_TOKEN
    API_ID = vars.API_ID
    API_HASH = vars.API_HASH

    app = Client(
        "Feedback and Request Bot",
        API_ID,
        API_HASH,
        bot_token = BOT_TOKEN,
        plugins = dict(root="bot/handlers")
    )

    app.start()
    logging.info("Pyrogram Client Started...✅")
    idle()
    app.stop()