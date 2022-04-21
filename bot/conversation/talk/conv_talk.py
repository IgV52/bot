from telegram.ext import ConversationHandler, Filters, MessageHandler
from bot.conversation.talk.dialogue import talk,theme,quest
from bot.conversation.talk.dialogue import dialogue_dontknow

conv_talk = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Опрос)$'), talk)], 
        states={
            'theme': [MessageHandler(Filters.text, theme)],
            'quest': [MessageHandler(Filters.text, quest)]
        },
        fallbacks=[MessageHandler(Filters.video | Filters.photo | Filters.document
          | Filters.location, dialogue_dontknow)],
        map_to_parent={'end': 'end'})
