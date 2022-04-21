from telegram import ReplyKeyboardMarkup

def keyboard():
    reply_keyboard = [['Опрос']]
    return ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
