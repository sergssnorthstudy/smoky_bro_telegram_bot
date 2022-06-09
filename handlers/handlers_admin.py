import logging
from aiogram import Bot, Dispatcher, executor, types
import emoji

from main import dp
from main import bot
import requests_database.get_requests as get_requests
import requests_database.post_requests as post_requests
import keyboards.keyboards_admin as kb

# Получить статистику
@dp.message_handler(content_types=['text'], text=emoji.emojize(':bar_chart:    Получить статистику', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Можете посмотреть статистику!!!!!', language='alias'))
            elif user_is_admin == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь Администратором', language='alias'))
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


# Обновление данных
@dp.message_handler(content_types=['text'], text=emoji.emojize(':arrows_clockwise:    Изменить кол-во товара', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Можете изменить кол-во товара!!!!!', language='alias'))
            elif user_is_admin == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь Администратором', language='alias'))
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


#Добавление данных
@dp.message_handler(content_types=['text'], text=emoji.emojize(':heavy_plus_sign:    Добавить новый товар', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                all_shops = get_requests.all_shops()
                if all_shops:
                    markup = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        shop_fullname = f'г. {shop_city}, ул. {shop_street}, дом {shop_house}'

                        markup.add(types.InlineKeyboardButton(text=shop_fullname,
                                                              callback_data=f"shop_add_data_{shop_id}"))
                    await bot.send_message(message.from_user.id,
                                           text='Укажите в какой магазин вы хотите добавить товар:',
                                           reply_markup=markup)

            elif user_is_admin == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь Администратором', language='alias'))
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
