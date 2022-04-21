from bot import constants
from bot import settings

def check_role(user_id):
    if user_id in settings.ADMIN:
        return constants.ADMIN
    return constants.USER