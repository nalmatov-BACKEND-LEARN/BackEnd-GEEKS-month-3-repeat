from aiogram import Dispatcher, Bot, executor, types
from decouple import config

import logging


token = config('TELEGRAM_BOT_TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
  await message.answer('Hello world!')

@dp.message_handler(commands=['image'])
async def image_handler(message: types.Message):
  photo = open('media/image.jpeg', 'rb')
  await bot.send_photo(chat_id=message.from_id.id,
                       photo=photo)

@dp.message_handler()
async def echo_handler(message: types.Message):
  try:
    num = float(message.text)
    await message.answer(int(num**2))
    return
  except: pass

  await message.answer(message.text)

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  executor.start_polling(dp, skip_updates=True)
