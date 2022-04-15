from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot

class FCMAdmin(StatesGroup):
    photo = State()
    dish = State()
    des = State()
    price = State

async def hi(message: types.Message):
    await FCMAdmin.photo.set()
    await message.reply('Отправь Фото Блюда!')

async def photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await FCMAdmin.next()
    await message.reply('Название блюда!')

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dish_name'] = message.text
    await FCMAdmin.next()
    await message.reply('описание еды')

async def load_Des(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['Description'] = message.text
    await FCMAdmin.next()
    await message.reply('Укажите Цену')

async def load_price(message: types.Message,state : FSMContext):
    async with state.proxy() as data:
        data['price'] = float(message.text)
        await state.finish()
        await bot.send_message(message.chat.id, 'Заказ принят!.Ожидайте...')

async def cancel_reg(message:types.Message,state:FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.reply('OK!')

def register_hendler_fsmAdminGetUser(dp: Dispatcher):
    dp.register_message_handler(hi, commands=["Run"])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state="*")
    dp.register_message_handler(photo, state=FCMAdmin.photo, content_types=["photo"])
    dp.register_message_handler(load_name, state=FCMAdmin.dish)
    dp.register_message_handler(load_Des, state=FCMAdmin.des)
    dp.register_message_handler(load_price, state=FCMAdmin.price)
    dp.register_message_handler(cancel_reg, state="*", commands="cancel")
