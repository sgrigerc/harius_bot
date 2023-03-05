from PIL import Image, ImageEnhance
from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вышел в онлайн') 
    sqlite_db.sql_start()
       
from handlers import client, redactor, other

client.register_handlers_client(dp)
redactor.register_handlers_redactor(dp)
other.register_handlers_other(dp)   
    
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)