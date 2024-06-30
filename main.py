from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboard import *

TOKEN = '7172093258:AAEiqhPmV1HOpLSLGC0wW-ituO83UfyCuBw'

bot = Bot(TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class Form(StatesGroup):
    waiting_for_age = State()
    waiting_for_confirmation = State()


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer(f'Assalom alaykum {message.from_user.full_name}.\n')
    await show_keyboard_work(message)


async def show_keyboard_work(message: Message):
    await message.answer(text=f'Ustoz Shogird kanalining rasmiy botiga xush kelibsiz',
                         reply_markup=show_keyboard_work_button())


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn_'))
async def first_question(call: CallbackQuery):
    btn_text_map = {
        'btn_1': 'Sherik kerak',
        'btn_2': 'Ish joyi kerak',
        'btn_3': 'Hodim kerak',
        'btn_4': 'Ustoz kerak',
    }
    btn_name = btn_text_map.get(call.data)
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, text=f'{btn_name} topish uchun ariza berildi.\n'
                                                   f'Hozir sizga bir nechta savollar beriladi.\n'
                                                   f'Har biriga javob bering.\n'
                                                   f"Oxirida agar xammasi to'g'ri bo'lsa 'Ha' tugmasini bosing va \n"
                                                   f"arizangiz amalga oshirildi")
    await second_question(call.message)


async def second_question(message: Message):
    await bot.send_message(message.chat.id, f'Yoshingiz nechida?\n'
                                            f'Masalan: 19')

    await Form.waiting_for_age.set()


@dp.message_handler(state=Form.waiting_for_age)
async def process_age(message: Message, state: FSMContext):
    user_input = message.text
    await state.update_data(age=user_input)
    await yes_or_no(message)


async def yes_or_no(message: Message):
    await show_yes_or_no(message)

    await Form.waiting_for_confirmation.set()


async def show_yes_or_no(message: Message):
    await message.answer(f"Berilgan ma'lumotlar to'g'rimi?",
                         reply_markup=yes_or_no_button())


@dp.callback_query_handler(lambda call: 'yes' in call.data)
async def answer_to_yes(call: CallbackQuery):
    await call.message.answer(text=f"📪 So`rovingiz tekshirish uchun adminga jo`natildi! \n"
                                   f"E'lon 24-48 soat ichida kanalda chiqariladi. ")


@dp.callback_query_handler(lambda call: 'no' in call.data)
async def answer_to_no(call: CallbackQuery):
    await call.message.answer(text="So'rovnoma qaytadan olib boriladi",
                              reply_markup=show_keyboard_work_button())


executor.start_polling(dp)

