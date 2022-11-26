import os
import telebot
from base import DataBase
from fsm import FSM


bot = telebot.TeleBot(os.getenv('TG_TOKEN'))
fsm_base = DataBase()
middleware_base = DataBase()
main_base = DataBase()
tool_base = DataBase()
post_base = DataBase()
end_base = DataBase()
fsm = FSM(fsm_base)
