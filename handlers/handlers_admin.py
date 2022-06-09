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
'''@dp.message_handler(content_types=['text'], text=emoji.emojize(':heavy_plus_sign:    Добавить новый товар', language='alias'))
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
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
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
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))'''


'''@dp.callback_query_handler(lambda callback_query: 'shop_add_data_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    callback_data = callback_query.data.split('shop_add_data_')
    shop_id = callback_data[1]'''


@dp.message_handler(content_types=['text'], text=emoji.emojize(':heavy_plus_sign:    Добавить информацию', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите нужную категорию', language='alias'),reply_markup=kb.add_information)
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


@dp.callback_query_handler(lambda callback_query: 'add_brand' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Напишите мне новый бренд или бренды\n\n'
                    '<b>Пример №1:</b>  "Добавить новый бренд HQD"\n'
                    '<b>Пример №2:</b>  "Добавить новые бренды HQD,Smoke,Vaporlax"', language='alias'),
                                       parse_mode="HTML")
            elif user_is_admin == False:
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь Администратором', language='alias'))
            else:
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
        elif is_complete_user == False:
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
        else:
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    elif is_incomplete_user == False:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
            ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
    else:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))


@dp.message_handler(lambda message: 'Добавить новый бренд ' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новый бренд')
                brand = result[1]
                if ',' in brand:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить новый бренд", но указываете несколько брендов\n'
                        'Чтобы добавить один брэнд напишите как в примере \n\n'
                        '<b>Пример:</b> "Добавить новый бренд HQD"', language='alias'),parse_mode="HTML")
                else:
                    brand = brand.strip()
                    is_brand_in_db = get_requests.check_similar_brand(brand)
                    if is_brand_in_db:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Брэнд {brand} уже существует в Базе Данных', language='alias'))
                    elif is_brand_in_db == False:
                        post_requests.add_brand(brand)
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                             f':white_check_mark: Я успешно записал брэнд {brand} в базу данных', language='alias'))
                    else:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

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


@dp.message_handler(lambda message: 'Добавить новые бренды' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новые бренды')
                brand = result[1]
                if ',' in brand:
                    brand = brand.strip()
                    list_brands = brand.split(',')
                    for brand in list_brands:
                        brand = brand.strip()
                        is_brand_in_db = get_requests.check_similar_brand(brand)
                        if is_brand_in_db:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Брэнд {brand} уже существует в Базе Данных', language='alias'))
                        elif is_brand_in_db == False:
                            post_requests.add_brand(brand)
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':white_check_mark: Я успешно записал брэнд {brand} в базу данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить новые бренды", но указали один брэнд или не напечатали ","\n'
                        'Чтобы добавить сразу несколько брэндов напишите как в примере \n\n'
                        '<b>Пример:</b> "Добавить новые бренды HQD,Smoke,Vaporlax"', language='alias'),parse_mode="HTML")

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





@dp.callback_query_handler(lambda callback_query: 'add_products' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                pass
            elif user_is_admin == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь Администратором', language='alias'))
            else:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
        elif is_complete_user == False:
            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
        else:
            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    elif is_incomplete_user == False:
        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
            ':pensive: Ваш аккаунт не настроен, напишите: "/start" чтобы исправить это', language='alias'))
    else:
        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))