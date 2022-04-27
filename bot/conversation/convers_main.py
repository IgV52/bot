from telegram.ext import CommandHandler, MessageHandler, Filters, ConversationHandler
from bot.conversation.talk.conv_talk import conv_talk
from bot.conversation.poll.conv_poll import conv_poll
from bot.conversation.conv_handler import start, dialogue_dontknow, reg
from bot.conversation.select import selection_handlers

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)], 
        states={
            'reg': [MessageHandler(Filters.text, reg)],
            'main': [MessageHandler(Filters.regex('^(Начало)$'), start)],
            'select': selection_handlers
        },
        fallbacks=[MessageHandler(Filters.video | Filters.photo | Filters.document
          | Filters.location, dialogue_dontknow)])