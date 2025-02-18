from aiogram import types, executor
import logging

from config import Admins, bot, dp
from handlers import register_all_handlers


async def on_startup(_):
  for admin in Admins:
    await bot.send_message(chat_id=admin, text='Бот включен')

async def on_shutdown(_):
  for admin in Admins:
    await bot.send_message(chat_id=admin, text='Бот выключен')

register_all_handlers(dp)

if __name__ == '__main__':
  logging.basicConfig(level=logging.INFO)
  executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
