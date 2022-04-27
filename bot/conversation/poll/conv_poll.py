from telegram.ext import ConversationHandler, Filters, MessageHandler
from bot.conversation.poll.dialogue import poll,section,quest,theme,back
from bot.conversation.talk.dialogue import dialogue_dontknow

conv_poll = ConversationHandler(
        entry_points=[MessageHandler(Filters.regex('^(Тест)$'), poll)],
        states={
            'section': [MessageHandler(Filters.regex('^(Назад)$'), back),
                        MessageHandler(Filters.text, section)],
            'theme' : [MessageHandler(Filters.regex('^(Назад)$'), back),
                        MessageHandler(Filters.text, theme)],
            'quest': [MessageHandler(Filters.text, quest)]
        },
        fallbacks=[MessageHandler(Filters.video | Filters.photo | Filters.document
                                | Filters.location, dialogue_dontknow)],
        map_to_parent={'select': 'select'})

