from aiogram import Dispatcher
from . import commands, echo, quiz, shop_fsm


def register_all_handlers(dp: Dispatcher):
  handlers = (commands, quiz, shop_fsm, echo, )

  for handler in handlers:
    handler.register_handlers(dp)
