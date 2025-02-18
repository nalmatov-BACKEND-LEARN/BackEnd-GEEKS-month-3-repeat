from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot


quizperiod = 60 # in seconds

async def quiz(message: types.Message):
  keyboard = InlineKeyboardMarkup()
  button = InlineKeyboardButton('Далее', callback_data='button_1')
  
  keyboard.add(button)
  
  question = '1 + 1 = ?'
  answers = ['2', '1', '5']
  
  await bot.send_poll(
    chat_id=message.from_user.id,
    question=question,
    options=answers,
    is_anonymous=True,
    type='quiz',
    correct_option_id=0,
    explanation='Ответ 2',
    open_period=quizperiod,
    reply_markup=keyboard
  )

async def quiz_2(call: types.CallbackQuery):
  keyboard = InlineKeyboardMarkup()
  button = InlineKeyboardButton('Далее', callback_data='button_2')

  keyboard.add(button)

  question = '2 + 2 = ?'
  answers = ['1', '5', '4']
  
  await bot.send_poll(
    chat_id=call.from_user.id,
    question=question,
    options=answers,
    is_anonymous=True,
    type='quiz',
    explanation='Ответ 4',
    correct_option_id=2,
    open_period=quizperiod,
    reply_markup=keyboard,
  )

async def quiz_3(call: types.CallbackQuery):
  question = '1 + 3 = ?'
  answers = ['3', '7', '4']
  
  await bot.send_poll(
    chat_id=call.from_user.id,
    question=question,
    options=answers,
    is_anonymous=True,
    type='quiz',
    explanation='Ответ 4',
    correct_option_id=2,
    open_period=quizperiod,
  )
  pass
  
def register_handlers(dp: Dispatcher):
  dp.register_message_handler(quiz, commands=['quiz'])
  dp.register_callback_query_handler(quiz_2, text='button_1')
  dp.register_callback_query_handler(quiz_3, text='button_2')
