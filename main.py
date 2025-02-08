from aiogram import Dispatcher, Bot, executor, types
from decouple import config

import logging


token = config('TELEGRAM_BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
  await message.answer('hello world')


if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  executor.start_polling(dp, skip_updates=True)
