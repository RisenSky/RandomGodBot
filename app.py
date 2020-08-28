import telebot
import config
from base import DataBase
from fsm import FSM


bot = telebot.TeleBot(config.TOKEN)
fsm_base = DataBase()
middleware_base = DataBase()
main_base = DataBase()
tool_base = DataBase()
post_base = DataBase()
end_base = DataBase()
fsm = FSM(fsm_base)