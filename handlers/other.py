from aiogram import types, Dispatcher
from create_bot import dp, bot
import asyncio


async def echo_send(message: types.Message):
   await message.reply('Цвета можно подбирать в диапазоне от 0 до 255, blur нечетные цифры(1, 3, 5, 7, 9) чем меньше, тем больше точность')

async def examples_of_color(message: types.Message):
   responses = ["12 235 230 5",
                "Мятный,зернистость средняя",
               "167 16 218 5",
               "фиолетовый, зернистость средняя",
               "217 214 15 5",
               "Желтый, зернистость средняя",
               "В любом случае вы можете изменять любые параметры. blur(1, 3, 5, 7, 9)."]
   
   # Отправка сообщений с задержкой
   for response in responses:
      await asyncio.sleep(0.5)  # Задержка между сообщениями
      await message.answer(response)


def register_handlers_other(dp : Dispatcher):
   dp.register_message_handler(echo_send, commands=['Инструкция'])
   dp.register_message_handler(examples_of_color, commands=['Примеры'])
   