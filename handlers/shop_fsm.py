from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


confirm_text, cancel_text = 'Подтвердить', 'Отмена'

class ShopStates(StatesGroup):
  name = State()
  price = State()
  category = State()
  created_at = State()
  photo = State()
  submit = State()

async def start_shop(message: types.Message):
  await ShopStates.name.set()
  await message.answer('Введите название товара: ')

async def load_name(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['name'] = message.text
  await ShopStates.next()
  await message.answer('Введите цену товара: ')

async def load_price(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['price'] = message.text
  await ShopStates.next()
  await message.answer('Введите категорию товара: ')

async def load_category(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['category'] = message.text
  await ShopStates.next()
  await message.answer('Введите дату создания товара: ')

async def load_created_at(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['created_at'] = message.text
  await ShopStates.next()
  await message.answer('Отправьте фото для товара: ')

async def load_photo(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['photo'] = message.photo[-1].file_id
  
  result_text = (
    f"Данные о товаре:\n"
    f"Название: {data['name']}\n"
    f"Цена: {data['price']}\n"
    f"Категория: {data['category']}\n"
    f"Дата создания: {data['created_at']}"
  )
  
  keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
  buttons = ( KeyboardButton(confirm_text), KeyboardButton(cancel_text) )
  keyboard.add(*buttons)

  await message.answer_photo(photo=data['photo'], caption=result_text, reply_markup=keyboard)
  await message.answer('Сохранить данные?')

  await ShopStates.next()

async def submit(message: types.Message, state: FSMContext):
  if message.text == confirm_text:
    await message.answer('Товар успешно сохранён!', reply_markup=ReplyKeyboardRemove())
    await state.finish()
  elif message.text == cancel_text:
    await message.answer('Товар успешно сохранён!', reply_markup=ReplyKeyboardRemove())
    await state.finish('Товар не сохранён!')
    await state.finish()
  else:
    await message.answer('Закончите с товаром!')

def register_handlers(dp: Dispatcher):
  dp.register_message_handler(start_shop, commands=['shop'], state=None)
  dp.register_message_handler(load_name, state=ShopStates.name)
  dp.register_message_handler(load_price, state=ShopStates.price)
  dp.register_message_handler(load_category, state=ShopStates.category)
  dp.register_message_handler(load_created_at, state=ShopStates.created_at)
  dp.register_message_handler(load_photo, content_types=['photo'], state=ShopStates.photo)
  dp.register_message_handler(submit, state=ShopStates.submit)
