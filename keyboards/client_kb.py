from re import T
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b0 = KeyboardButton('/отмена')
b1 = KeyboardButton('/editor')
b2 = KeyboardButton('/instruction')
b3 = KeyboardButton('/Примеры')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b0).insert(b1).add(b2).add(b3)   

