import logging
from aiogram import Bot, Dispatcher, executor, types
import emoji

from main import dp
from main import bot
import requests_database.get_requests as get_requests
import requests_database.post_requests as post_requests



#Buyer Products
@dp.message_handler(content_types=['text'], text=emoji.emojize(':mag_right:    Товары', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Можете посмотреть товары', language='alias'))
            elif user_is_buyer == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь продавцом, обратитесь к администратору', language='alias'))
            else:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
        elif is_complete_user == False:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
        else:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    elif is_incomplete_user == False:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
    else:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))


#Buyer Shops
@dp.message_handler(content_types=['text'], text=emoji.emojize(':house:    Магазины', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Можете посмотреть информацию по магазинам', language='alias'))
            elif user_is_buyer == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь продавцом, обратитесь к администратору', language='alias'))
            else:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
        elif is_complete_user == False:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
        else:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    elif is_incomplete_user == False:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
    else:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))