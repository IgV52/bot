from bot import settings

from pymongo import MongoClient
from bot.database.utils import check_role

client = MongoClient(settings.MONGO_LINK)
db = client[settings.MONGO_DB]

def get_or_create_talk(db, file):
    talk_list = db.talk.find_one({'theme' : file['theme']})
    if not talk_list:
        talk_list = {
            'theme' : file['theme'],
            'blank_form' : file['blank_form']
            }
        db.talk.insert_one(talk_list)
    return talk_list

def get_or_create_user(db, update):
    user = db.users.find_one({"user_id" : update.effective_user.id})
    if not user:
        user = {
            "user_id" : update.effective_user.id,
            "first_name" : update.effective_user.first_name,
            "last_name" : update.effective_user.last_name,
            "username" : update.effective_user.username,
            "chat_id" : update.message.chat_id,
            "date" : update.message.date,
            "role" : check_role(update.effective_user.id)
        }
        db.users.insert_one(user)
    return user

def get_buttons(db, file):
    button = db.buttons.find_one('id', file['id'])
    if not button:
        button = {
            "id" : file['id'],
            "button" : {file['theme'] : 
            {file['theme_id']: file['num_quest']}}
        }
        db.buttons.insert_one(button)
    db.buttons.replace_one(button, file)
    return button

def info_buttons(db):
    button = db.buttons.find_one({'id': 1})
    return button['button']

def info_discussion(db, theme):
    discussion = db.talk.find_one({'theme' : theme})
    return discussion
