from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token = '6123346106:AAE1HL9m_8fQAQtpyG98lxEiidHwalaE5gs')
dp = Dispatcher(bot, storage=storage)
# dp.skip_updates = True