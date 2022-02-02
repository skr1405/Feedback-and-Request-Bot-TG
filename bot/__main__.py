# Importing Required Modules
import logging

from telegram.ext import Updater, CommandHandler
# from telegram.

from bot.handlers.feedback import add_feedback_handlers
from bot.configs import Config as vars

# Logging Stuff
logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
logging.getLogger().setLevel(logging.DEBUG)

def start(update, context):
    update.message.reply_text('Hi! \nWelcome to the *IMDb Bot*. \nSend me the name of any movie or TV show to get its details. \nHappy viewing! \n \nCreated by [SKR](https://t.me/SKR1405)',parse_mode='markdown', disable_web_page_preview=True)



def main():
    # GETTING VARIABLES
    BOT_TOKEN = vars.BOT_TOKEN
    BASE_URL_OF_BOT = vars.BASE_URL_OF_BOT
    PORT = vars.PORT

    updater = Updater(BOT_TOKEN, workers=100)

    dp = updater.dispatcher


    updater.start_webhook(
        listen="0.0.0.0",
        port = PORT,
        url_path = BOT_TOKEN,
        webhook_url = BASE_URL_OF_BOT + BOT_TOKEN
    )

    dp.add_handler(CommandHandler("start", start))

    logging.info("Bot Started...✅")
    updater.idle()




if __name__ == "__main__":

    main()