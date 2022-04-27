from telegram import ReplyKeyboardMarkup

def active_keyboard(list_info):
    keyboard = [['Назад']]
    keyboard.insert(0,list_info)
    return ReplyKeyboardMarkup(keyboard, 
            one_time_keyboard=True, resize_keyboard=True)

def static_keyboard(list_info):
    keyboard = [[]]
    keyboard.append(list_info)
    return ReplyKeyboardMarkup(keyboard, 
            one_time_keyboard=True, resize_keyboard=True)

def format_text(question,num,answer):
    form_answer = answer[num].replace(',','\n')
    user_text = f"""<b>Вопрос № {num}:</b>\n {question[num]}\n<b>Варианты ответа:</b>\n {form_answer}"""
    return user_text

def key_quest(dict_quest):
    key = [key for key in dict_quest.keys()]
    return key
