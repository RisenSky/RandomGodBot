import json
import telebot
import models
from app import tool_base




file = open("RU.json", encoding="utf-8")
ru_bot_text = json.load(file)

file = open("ENG.json", encoding="utf-8")
eng_bot_text = json.load(file)


# ----Подгружаем файл с текстами ответов бота----
def language_check(user_id):
    language = tool_base.get_one(models.User, user_id=str(user_id))
    if language == None:
        return (False, ru_bot_text)
    else:
        if language.language == "RU":
            return (True, ru_bot_text)
        else:
            return (True, eng_bot_text)


def create_inlineKeyboard(key, row=0):
    keyboard = telebot.types.InlineKeyboardMarkup()
    key_list = []
    count = 0
    for i in key:
        key_list.append(telebot.types.InlineKeyboardButton(
            text=i, callback_data=key.get(i)))
        count += 1

        if count >= row:
            keyboard.add(*[i for i in key_list])
            key_list = []
            count = 0
        if list(key.keys())[-1] == i:
            keyboard.add(*[i for i in key_list])
    return keyboard

