from aiogram import Dispatcher
from . import commands, echo, quiz


def register_all_handlers(dp: Dispatcher):
  handlers = (commands, quiz, echo, )

  for handler in handlers:
    handler.register_handlers(dp)
