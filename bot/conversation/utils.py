from telegram import ReplyKeyboardMarkup

def keyboard(list_info):
    keyboard = [['Выход']]
    keyboard.insert(0,list_info)
    return ReplyKeyboardMarkup(keyboard, 
            one_time_keyboard=True, resize_keyboard=True)
