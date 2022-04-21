from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from bot.conversation.talk.conv_talk import conv_talk
from bot.conversation.conv_handler import start, dialogue_dontknow, end_talk

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)], 
        states={
            'talk': [conv_talk],
            'end': [MessageHandler(Filters.text, end_talk)]
        },
        fallbacks=[MessageHandler(Filters.video | Filters.photo | Filters.document
          | Filters.location, dialogue_dontknow)])