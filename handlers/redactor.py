import io
import os
from typing import Text
from aiogram.types import ContentType, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import client_kb
import kivy
from create_bot import dp, bot


class FSMAdmin(StatesGroup):
    photo = State()
    blur = State()
    color = State()
 
# async def make_changes_command(message: types.Message):
#     await bot.send_message(message.from_user.id, "Что надо человек", reply_markup=client_kb.button_send)
#     await message.delete()
        
#Начало диалога загрузки нового фото
# @dp.message_handler(commands="Загрузить", state=None)
async def cm_start(message : types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузите фото')

#Выход из состояний
# @dp.message_handler(state="*", commands="отмена")
# @dp.message_handler(Text(equals="отмена", ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("ОК")
    

#Ловим первый ответ и пишем словарь
# @dp.message_handler(content_types=['photo', 'document'])
# async def photo_or_doc_handler(message: types.Message):
#     file_in_io = io.BytesIO()
#     if message.content_type == 'photo':
#         await message.photo[-1].download(destination_file=file_in_io)
#         await FSMAdmin.next()
#         await message.reply("Фото загружено успешно, теперь введите зернистость")
#     elif message.content_type == 'document':
#         await message.document.download(destination_file=file_in_io)
#     # file_in_io - do smth with this file-like object

def download_file(file: types.File):
     file_path = file.file_path
     destination = r'C:\\Users\\admin\\Desktop\\moonlog inspector\\download'
     destination_file = bot.download_file(file_path, destination)
     
#Ловим первый ответ и пишем словарь
@dp.message_handler(content_types = ContentType.PHOTO)
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id
        print(data)
        
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        src = '.images/' + file_info.file_path.replace('images/', '')
        with open(src, 'wb') as new_file:
            new_file.write(download_file)
            new_file.close()
        await FSMAdmin.next()
        await message.reply("Фото загружено успешно, теперь введите зернистость")
        
    # await FSMAdmin.next()
    # await message.reply("Фото загружено успешно, теперь введите зернистость")
    # await message.reply(message.photo[-1].file_id)
    
    #сохраняем фото в бд


#Ловим второй ответ
# @dp.message_handler(state=FSMAdmin.blur)
async def blur_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['blur'] = message.text
    await FSMAdmin.next()
    await message.reply("Введите цвет в rgb")
    
#Ловим третий ответ
# @dp.message_handler(state=FSMAdmin.color)
async def color_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['color'] = message.text
    await FSMAdmin.next()
    await message.reply("Нажмите кнопку Отправить")
    
    await sqlite_db.sql_add_command(state)
    await state.finish()

@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    
    photo_file_id = 'AgACAgIAAxkBAAICSWPpDP13J7J3CEnOFLOAS97md4gWAAIXxTEbcANJS_5QLa_vczr5AQADAgADeQADLgQ'
    photo_url = 'dcd'
    photo_bytes = 'ef'
    
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id)

#Регистрируем хендлеры
def register_handlers_redactor(dp : Dispatcher):
    dp.register_message_handler(cancel_handler, state="*", commands="отмена")
    dp.register_message_handler(cancel_handler, Text(equals="отмена", ignore_case=True), state="*")  # type: ignore
    dp.register_message_handler(cm_start, commands=['editor'], state=None)
    # dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(blur_photo, state=FSMAdmin.blur)
    dp.register_message_handler(color_photo, state=FSMAdmin.color)