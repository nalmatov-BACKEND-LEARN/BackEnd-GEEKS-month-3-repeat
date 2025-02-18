from aiogram import Bot, Dispatcher
from decouple import config

token = config('TELEGRAM_BOT_TOKEN')

Admins = (1038789342, )

bot = Bot(token=token)
dp = Dispatcher(bot)
