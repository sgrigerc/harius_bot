from aiogram import types, Dispatcher
from create_bot import dp, bot 
from keyboards import kb_client


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello', reply_markup=kb_client)
    await message.delete()

# @dp.message_handler(commands=['Editor'])
# async def photo_open_command(message: types.Message):
#     await bot.send_message(message.from_user.id, "Нажмите на команду /upload")
    
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    # dp.register_message_handler(photo_open_command, commands=['editor'])



