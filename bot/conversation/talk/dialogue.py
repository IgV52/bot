from bot.database.db import db, info_buttons, info_discussion
from bot.conversation.talk.utils import active_keyboard

def talk(update, context):
    context.user_data['button'] = info_buttons(db)
    keyboard = active_keyboard(context.user_data['button'])
    update.message.reply_text(
        f"Выберите направление.",
        reply_markup=keyboard)
    return 'theme'

def theme(update, context):
    context.user_data['all_quest'] = info_discussion(db, update.message.text)
    keyboard = active_keyboard(context.user_data['button'][update.message.text])
    update.message.reply_text(f"Выберите опрос.",
    reply_markup=keyboard)
    return 'quest'

def quest(update, context):
    msg = update.message.text
    question = context.user_data['all_quest']['blank_form']
    if not 'answer' in context.user_data:
        num = context.user_data['button'][context.user_data['all_quest']['theme']][msg]
        context.user_data['num'] = [str(i) for i in range(1,num+1)]
        update.message.reply_text(question[msg][context.user_data['num'][0]])
        context.user_data['theme'] = msg
        context.user_data['answer'] = []
    else:
        context.user_data['answer'].append({context.user_data['num'][0]: msg})
        del context.user_data['num'][0]
        if not context.user_data['num']:
            update.message.reply_text("Спасибо за ответы",reply_markup=active_keyboard(['ВЫХОД']))
            return 'end'
        update.message.reply_text(question[context.user_data['theme']][context.user_data['num'][0]])
    return 'quest'

def dialogue_dontknow(update, context):
    update.message.reply_text("Я вас не понимаю")
