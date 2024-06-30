from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def show_keyboard_work_button():
    markup = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Sherik kerak', callback_data='btn_1')
    btn2 = InlineKeyboardButton(text='Ish joyi kerak', callback_data='btn_2')
    btn3 = InlineKeyboardButton(text='Hodim kerak', callback_data='btn_3')
    btn4 = InlineKeyboardButton(text='Ustoz kerak', callback_data='btn_4')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)

    return markup


def yes_or_no_button():
    markup = InlineKeyboardMarkup(row_width=2)
    btn_1 = InlineKeyboardButton(text='Ha', callback_data='yes')
    btn_2 = InlineKeyboardButton(text="Yo'q", callback_data='no')
    markup.row(btn_1, btn_2)
    return markup

