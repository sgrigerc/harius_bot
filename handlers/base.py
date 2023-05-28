from datetime import datetime
from aiogram import types, Dispatcher
import asyncio
from create_bot import dp, bot 
from keyboards import kb_client


async def command_start(message: types.Message):
    # Текущщее время
    now = datetime.now()
    hour = now.hour
    
    # Определяем время
    if 6 <= hour < 12:
        greeting = "Доброе утро!"
    elif 12 <= hour < 18:
        greeting = "Добрый день!"
    elif 18 <= hour < 24:
        greeting = "Добрый вечер!"
    else:
        greeting = "Доброй ночи!"
    
    responses = [f"{greeting}, как дела?",
                "Нажмите на команду /tool, или /editor чтобы сразу перейти к редактированию"]
    
    # Отправка сообщений с задержкой
    for response in responses:
        await asyncio.sleep(0.5)  # Задержка между сообщениями
        await bot.send_message(message.from_user.id, response, reply_markup=kb_client)   


def register_handlers_base(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
