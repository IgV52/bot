from telegram.ext import MessageHandler, Filters
from bot.conversation.talk.conv_talk import conv_talk
from bot.conversation.poll.conv_poll import conv_poll
from bot.conversation.conv_handler import start, end_talk

selection_handlers = [
    conv_talk,
    MessageHandler(Filters.regex('^(Начало)$'), start),
    MessageHandler(Filters.regex('^(Выход)$'), end_talk),
    conv_poll,
    MessageHandler(Filters.regex('^(Начало)$'), start),
    MessageHandler(Filters.regex('^(Выход)$'), end_talk)]