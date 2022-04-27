from telegram import ParseMode
from bot.database.db import db, info_buttons, info_poll, user_profile, save_data
from bot.conversation.poll.utils import active_keyboard, format_text, key_quest, static_keyboard

def poll(update, context):
    context.user_data['trigger'] = 'poll'
    context.user_data['button'] = info_buttons(db, 2)
    keyboard = active_keyboard(context.user_data['button'])
    update.message.reply_text(
        f"Выберите раздел.",
        reply_markup=keyboard)
    return 'section'

def section(update, context):
    context.user_data['trigger'] = 'section'
    user_data = context.user_data
    msg = update.message.text
    if msg not in user_data['button']:
        update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
        return 'section'
    else:
        user_data['info'] = info_poll(db, msg)
        keyboard = active_keyboard(user_data['button'][msg])
        user_data['section'] = msg
        update.message.reply_text(f"Выберите тест.",
        reply_markup=keyboard)
        return 'theme'

def theme(update, context):
    context.user_data['trigger'] = 'theme'
    msg = update.message.text
    reply_text = update.message.reply_text
    user_data = context.user_data
    if msg not in user_data['button'][user_data['section']]:
        reply_text("Ошибка. Нажмите доступную кнопку!")
        return 'theme'
    else:
        user_data['theme'] = msg
        user_data['answer'] = dict()
        user_data['start'] = ['start']
        if user_profile(db,update.effective_user.id,user_data['section'],msg):
            reply_text("Вы уже проходили этот тест", 
            reply_markup=active_keyboard(user_data['button'][user_data['section']]))
            return 'theme'
        user_data['num'] = key_quest(user_data['info']['form'][msg]['quest'])
        reply_text(f"Информация о правилах теста, если вы готовы отправте боту любое сообщение.")
        return 'quest'

def quest(update, context):
    user_data = context.user_data
    answer = user_data['info']['form'][user_data['theme']]['answer']
    button = user_data['button'][user_data['section']][user_data['theme']]
    question = user_data['info']['form'][user_data['theme']]['quest']
    msg = update.message.text
    reply_text = update.message.reply_text
    if 'start' in user_data:
        del user_data['start']
        reply_text(format_text(question,user_data['num'][0],answer),
        reply_markup=static_keyboard(button), parse_mode=ParseMode.HTML)
        return 'quest'
    else:
        if msg not in button:
            update.message.reply_text("Ошибка. Нажмите доступную кнопку!")
            return 'quest'
        user_data['answer'][user_data['num'][0]] = msg
        del user_data['num'][0]
        if not user_data['num']:
            save_data(db, user_data['section'],user_data['theme'],
                    user_data['answer'], update.effective_user.id)
            reply_text("Спасибо за ответы",reply_markup=static_keyboard(['Выход', 'Начало']))
            return 'select'
        reply_text(format_text(question,user_data['num'][0],answer),
        reply_markup=static_keyboard(button), parse_mode=ParseMode.HTML)
        return 'quest'
    
def dialogue_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")

def back(update,context):
    if context.user_data['trigger'] == 'section':
        update.message.reply_text("Выберите действие",reply_markup=static_keyboard(['Тест','Опрос', 'Выход']))
        return 'select'
    
    if context.user_data['trigger'] == 'theme':
        context.user_data['trigger'] = 'section'
        update.message.reply_text("Выберите раздел",reply_markup=active_keyboard(context.user_data['button']))
        return 'section'
    