from aiogram import types, Dispatcher
from create_bot import dp, bot 
from keyboards import kb_client



async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, напиши мне "инструкция" или нажми на кнопку /editor чтобы сразу перейти к редактированию', reply_markup=kb_client)
    await message.delete()


async def register_handlers_base(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
