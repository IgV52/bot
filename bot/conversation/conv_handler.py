from telegram.ext import ConversationHandler
from bot.conversation.utils import keyboard

def start(update, context):
    reply_text = "Привет я БОТ для проведения интервью"
    update.message.reply_text(reply_text, reply_markup=keyboard())
    return 'talk'

def end_talk(update, context):
    update.message.reply_text('Вы завершили беседу')
    return ConversationHandler.END

def dialogue_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")