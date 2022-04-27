from bot import settings
from pymongo import MongoClient

client = MongoClient(settings.MONGO_LINK)
db = client[settings.MONGO_DB]

def get_or_create_user(db, update, user_name):
    user = db.users.find_one({"user_id" : update.effective_user.id})
    if not user:
        user = {
            "user_id" : update.effective_user.id,
            "first_name" : update.effective_user.first_name,
            "last_name" : update.effective_user.last_name,
            "username" : update.effective_user.username,
            "chat_id" : update.message.chat_id,
            "date" : update.message.date,
            "user_name": user_name
        }
        db.users.insert_one(user)
    return user

def user_info(db, user_id):
    user = db.users.find_one({'user_id': user_id})
    if user:
        return [True, user['user_name']]
    return [False]

def info_buttons(db, id):
    button = db.buttons.find_one({'id': id})
    return button['button']

def info_discussion(db, section):
    discussion = db.talk.find_one({'section' : section})
    return discussion

def info_poll(db, section):
    poll = db.poll.find_one({'section' : section})
    return poll

def save_data(db, section, theme, answer, user_id):
    user = db.users.find_one({"user_id" : user_id})
    if not section in user:
        db.users.update_one({'_id': user['_id']}, {'$set': {section: [{'theme':theme, 'answer': answer}]}})
    else:
        db.users.update_one({'_id': user['_id']}, {'$push': {section: {'theme':theme, 'answer': answer}}})

def user_profile(db, user_id, section, theme):
    key = section+'.'+'theme'
    if db.users.find_one({'user_id': user_id, key: theme}):
        return True
    return False