from aiogram import types, Dispatcher
from config import bot


async def start_handler(message: types.Message):
  await message.answer('Hello world!')

async def image_handler(message: types.Message):
  photo = open('media/image.jpeg', 'rb')
  await bot.send_photo(chat_id=message.from_id.id,
                       photo=photo)

def register_handlers(dp: Dispatcher):
  dp.register_message_handler(start_handler, commands=['start'])
  dp.register_message_handler(image_handler, commands=['image'])
