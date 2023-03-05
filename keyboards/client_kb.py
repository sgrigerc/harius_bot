from re import T
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b0 = KeyboardButton('/start')
b1 = KeyboardButton('/editor')
# b2 = KeyboardButton('/blur')
# b3 = KeyboardButton('/color')
# b4 = KeyboardButton('/upload')
button_send = KeyboardButton('/Отправить')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client.add(b0).insert(b1).add(button_send)   #.add(b2).insert(b3).insert(b4)

# button_send_redactor = ReplyKeyboardMarkup(resize_keyboard=True).add(button_send)