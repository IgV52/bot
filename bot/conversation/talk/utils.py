from telegram import ReplyKeyboardMarkup

def active_keyboard(list_info):
    keyboard = [[]]
    keyboard.append(list_info)
    return ReplyKeyboardMarkup(keyboard, 
            one_time_keyboard=True, resize_keyboard=True)
            