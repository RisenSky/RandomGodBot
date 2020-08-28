import json
import telebot
from tool import language_check, create_inlineKeyboard

def get_menu_keyboard(user_id):
	buttons = language_check(user_id)[1]['menu']['menu_buttons']
	menu_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	menu_keyboard.row(buttons[0], buttons[1])
	menu_keyboard.row(buttons[2])
	menu_keyboard.row(buttons[3], buttons[4])
	return menu_keyboard

	
def get_draw_keyboard(user_id):
	buttons = language_check(user_id)[1]['draw']['draw_buttons']
	draw_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	draw_keyboard.row(buttons[0], buttons[1])
	draw_keyboard.row(buttons[2], buttons[3])
	draw_keyboard.row(buttons[4], buttons[5])
	draw_keyboard.row(buttons[6], buttons[7])
	return draw_keyboard
	

def back_button(user_id):
	buttons = language_check(user_id)[1]['draw']['back']
	back_button = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
	back_button.row(buttons)
	return back_button


