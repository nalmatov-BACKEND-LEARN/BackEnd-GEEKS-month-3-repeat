import asyncio
from aiogram import types, Dispatcher
from config import bot


# games : ['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']
game_keyword = 'game'

async def echo_handler(message: types.Message):
  # Squaring
  try:
    num = float(message.text)
    await message.answer(int(num**2))
    return
  except ValueError:
    pass
  
  # Game
  if (message.text == game_keyword):
    result = await message.answer_dice('🎲')

    await asyncio.sleep(4)

    await message.answer(f"Тебе выпало число {result.dice.value} с кости")
    return
  

  # Echo
  await message.answer(message.text)

def register_handlers(dp: Dispatcher):
  dp.register_message_handler(echo_handler)
