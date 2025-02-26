from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from datetime import date
from dateutil.relativedelta import relativedelta

from app import texts
from app import keyboards as kb
import app.database.reqests as rq


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await rq.set_user(message.from_user.id)
    await message.answer(text=texts.welcome_message, reply_markup=kb.tell_more_button())

@router.callback_query(lambda callback: callback.data == "tell_me_more")
async def tell_me_more(callback: CallbackQuery):
    await callback.message.answer(texts.tell_me_more_message, reply_markup=kb.start_training_button())
    await callback.answer()

@router.callback_query(lambda callback: callback.data == "start_training")
async def set_target(callback: CallbackQuery):
    await callback.message.answer(text='Выберите желаемую программу', reply_markup=kb.set_target_buttons)
    await callback.answer()


@router.message(F.text == "Сброс веса")
@router.message(F.text == "Укрепление")
@router.message(F.text == "Быть в форме")
async def set_programm_target(message: Message):
    await rq.set_target(message.from_user.id, message.text)
    await message.answer(text=texts.first_motivation, reply_markup=kb.set_training_programm_time_buttons)

@router.message(F.text == "Заниматься 1 месяц")
@router.message(F.text == "Заниматься 2 месяца")
@router.message(F.text == "Заниматься 3 месяца")
async def set_training_programm_time(message: Message):
    interval = message.text.split()[1]
    await rq.set_start_time(message.from_user.id, date.today())
    await rq.set_end_time(message.from_user.id, date.today()+relativedelta(months=int(interval)))
    await rq.set_training_time(message.from_user.id, interval)
    await message.answer(text='На каком уровне ваша физическая форма?', reply_markup=kb.set_lvl_buttons)

@router.message(F.text == 'Новичок')
@router.message(F.text == 'Средняя')
@router.message(F.text == 'Продвинутый')
async def set_programm_lvl(message: Message):
    await rq.set_lvl(message.from_user.id, message.text)
    await message.answer(text='Отлично, ваш план занятий готов', reply_markup=kb.main_buttons)

@router.message(F.text == '👤Профиль')
async def profile(message: Message):
    info = await rq.get_info(message.from_user.id)
    await message.answer(text = f'<b>Цель:</b> {info.target}\n<b>Уровень:</b> {info.lvl}\n<b>Начало занятий:</b> {info.start_time}\n<b>Конец занятий:</b> {info.end_time}',parse_mode="HTML")
    
@router.message(F.text == '⚙️Настройки')
async def settings(message: Message):
    await message.answer(text='Выберите пункт настроек', reply_markup=kb.change_programme_button())

@router.message(F.text == '📚База знаний')
async def knowledge_base(message: Message):
    await message.answer(text='Выберите, что хотите узнать', reply_markup=kb.database_button)

# @router.message(F.text == 'Программа на сегодня')
# async def today_programm(message: Message):
#     await message.answer_animation(animation='app/squats-exercise.gif')