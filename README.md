# Feedback-and-Request-Bot-TG
Telegram Bot to Request Content and Give Feedback

## Deployment
### Heroku
#### Use This Button to Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Variables
### *Compulsory Variables*
* `BOT_TOKEN `
  * Value : Bot Token Obtained From [@BotFather](https://t.me/BotFather)
  * Use : To Connect to Telegram as Bot

* `OWNER_ID `
  * Value : Your Telegram ID
  * Use : To Receive Feedback

* `BASE_URL_OF_BOT `
  * Value : Heroku App Link
  * Use : To Start Webhook

* `GROUP_LINK `
  * Value : Telegram Group Link
  * Use : To Send with Welcome Message when `/start` is used

* `CHANNEL_LINK `
  * Value : Telegram Channel Link
  * Use : To Send with Welcome Message when `/start` is used

* `REQUEST_GROUP_ID `
  * Value : Telegram Group ID
  * Use : To Get Request Message, which starts with `#request`

* `REQUEST_CHANNEL_ID `
  * Value : Telegram Channel ID
  * Use : To Send Request So that Users Can See Status

* `REQUEST_CHANNEL_LINK `
  * Value : Telegram Channel ID
  * Use : To Send to User so that they can join Channel and See their Request Status

### *Optional Variables*
* `REQUEST_COMPLETE_TEXT `
  * Value : Any String
  * Use : Any Text to send with Request Complete Message
