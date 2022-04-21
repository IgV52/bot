import logging.config
from bot import settings

from bot.logging_config import LOGGING_CONFIG
from telegram.ext import Updater
from bot.conversation.convers_main import conv_handler

def main():
   
    mybot = Updater(settings.BOT_API, use_context=True)
    
    dp = mybot.dispatcher

    dp.add_handler(conv_handler)

    logging.config.dictConfig(LOGGING_CONFIG)

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
