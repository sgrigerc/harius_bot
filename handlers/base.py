from aiogram import types, Dispatcher
from create_bot import dp, bot 


async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет, как дела?')
    await message.delete()


def register_handlers_base(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
