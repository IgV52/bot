from telegram.ext import ConversationHandler
from bot.conversation.utils import keyboard
from bot.database.db import db, user_info, get_or_create_user

def reg(update, context):
    user_name = update.message.text
    if len(user_name.split()) < 2:
        update.message.reply_text("Пожалуйста введите имя и фамилию")
        return 'reg'
    else:
        get_or_create_user(db,update,user_name)
        update.message.reply_text(
            "Теперь мы можем начать",
            reply_markup=keyboard(['Тест','Опрос']))
        return 'select'

def start(update, context):
    info = user_info(db,update.effective_user.id)
    if info[0]:
        reply_text = f"Привет\n{info[1]}"
        update.message.reply_text(reply_text, reply_markup=keyboard(['Тест', 'Опрос']))
        return 'select'
    reply_text = "Привет я БОТ для проведения интервью и cначала нам надо познакомиться"
    update.message.reply_text(reply_text, reply_markup=keyboard(['Регистрация']))
    return 'reg'

def end_talk(update, context):
    update.message.reply_text('Вы завершили беседу')
    return ConversationHandler.END

def dialogue_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")
