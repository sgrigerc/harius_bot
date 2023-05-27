import io
import os
import numpy as np
import cv2
from typing import Text
from aiogram.dispatcher import FSMContext, filters
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
# from data_base import sqlite_db
from create_bot import dp, bot, storage
import numpy as np

from aiogram.types import Message, ContentTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from PIL import Image, ImageEnhance


# Определяем состояния
class PhotoStates(StatesGroup):
   WAITING_FOR_PHOTO = State()
   PROCESSING_PHOTO = State()


async def cm_start(message: types.Message):
   global ID
   ID = message.from_user.id
   chat_id = message.chat.id
   await PhotoStates.WAITING_FOR_PHOTO.set()
   await message.reply("Загрузите фото для обработки!")                         
   print('принятие фото')


async def cancel_handler(message: types.Message, state: FSMContext):
   if message.from_user.id == ID:
      current_state = await state.get_state()
      if current_state is None:
         return
      await state.finish()
      await message.reply('Ok')


# Обработчик для получения фото
async def load_photo(message: Message, state: FSMContext):
   if message.from_user.id == ID:
      async with state.proxy() as data:
         data['photo'] = message.photo[-1]     
         print('Начало загрузки фото')
         # Передаем объект PhotoStates в качестве аргумента state
      await PhotoStates.PROCESSING_PHOTO.set()
      await message.reply("Хорошая фотография! Теперь введите R G B и blur через пробел")
      
      # Переходим в следующее состояние
      print('фото принято')
      print(message.photo[-1].file_id)
      print(message.from_user.id)


# Обработчик для обработки параметров фильтра
async def apply_photo_filter(message: Message, state: FSMContext):
   if message.from_user.id == ID:
      # Извлекаем сохраненное фото из состояния
      async with state.proxy() as data:
         # Получаем значения RGB из сообщения пользователя
         r = 182 # значение R по умолчанию
         g = 12 # значение G по умолчанию
         b = 235 # значение B по умолчанию
         blur = 5 # значение blur по умолчанию
         try:
            r, g, b, blur = map(int, message.text.split())
         except ValueError:
            pass
         
         # Получаем информацию о файле по его file_id
         photo = data['photo']
         file_id = photo.file_id
         file_info = await bot.get_file(file_id)
         
         # Получаем ссылку на файл
         file_path = file_info.file_path

         # Скачиваем фото
         photo_buffer = io.BytesIO()
         await bot.download_file_by_id(file_id, photo_buffer)

         
         # Декодируем фото с помощью OpenCV
         img = cv2.imdecode(np.frombuffer(photo_buffer.getvalue(), dtype=np.uint8), cv2.IMREAD_COLOR)
         new_img = np.zeros(img.shape, dtype='uint8')
   
   
         # Уменьшение размера фото
         img = cv2.imdecode(np.frombuffer(photo_buffer.getvalue(), dtype=np.uint8), cv2.IMREAD_COLOR)
         # Преобразование в чб
         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         # Blur размытие
         img = cv2.GaussianBlur(img, (blur, blur), 0)  
         img = cv2.Canny(img, 50, 50)
         con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
         
         # Прорисовка контуров
         cv2.drawContours(new_img, con, -1, (b, g, r), 1)
      
         # Кодирование фото в байты
         success, img_encoded = cv2.imencode('.jpg', new_img)
         img_bytes = img_encoded.tobytes()
         # Отправляем измененное фото пользователю
         await bot.send_photo(chat_id=message.chat.id, photo=img_bytes)

      await state.finish()
         


# Регистрируем хендлеры
def register_handlers_redactor(dp: Dispatcher):
   dp.register_message_handler(cancel_handler, state="*", commands="отмена")
   dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")
   dp.register_message_handler(cm_start, commands=['editor'], state=None)
   dp.register_message_handler(load_photo, content_types=ContentTypes.PHOTO, state='*')
   dp.register_message_handler(apply_photo_filter,lambda message: not message.text.isdigit(), content_types=types.ContentType.TEXT, state=PhotoStates.PROCESSING_PHOTO)     

