from aiogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Программа на сегодня')],
    [KeyboardButton(text='👤Профиль'), KeyboardButton(text='📚База знаний'), KeyboardButton(text='⚙️Настройки')]
    ],  
    resize_keyboard=True,
    input_field_placeholder='Ввыберите пункт меню'
)



def tell_more_button():
    builder = InlineKeyboardBuilder()
    builder.button(text='Расскажи подробнее🏋🏽🔥🎧', callback_data="tell_me_more")
    return builder.as_markup()

def start_training_button(): 
    builder = InlineKeyboardBuilder()
    builder.button(text='💪🏼Начать тренироваться💪🏼', callback_data='start_training')
    return builder.as_markup()


database_button =  InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Питание', callback_data='nutrition')],
        [InlineKeyboardButton(text='База упражнений', callback_data='exercises')],
    ],
)

set_target_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Сброс веса')],
        [KeyboardButton(text='Укрепление')],
        [KeyboardButton(text='Быть в форме')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите желаемую программу'  
)

set_training_programm_time_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Заниматься 1 месяц')],
        [KeyboardButton(text='Заниматься 2 месяца')],
        [KeyboardButton(text='Заниматься 3 месяца')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите желаемое время'  
)

set_lvl_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Новичок')],
        [KeyboardButton(text='Средняя')],
        [KeyboardButton(text='Продвинутый')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите желаемое время'  
)

def change_programme_button():
    builder = InlineKeyboardBuilder()
    builder.button(text='Изменить свою программу', callback_data="start_training")
    return builder.as_markup()
