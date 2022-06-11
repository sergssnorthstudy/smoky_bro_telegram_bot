import logging
import string

from aiogram import Bot, Dispatcher, executor, types
import emoji

import create_text
from main import dp
from main import bot
import requests_database.get_requests as get_requests
import requests_database.post_requests as post_requests
from keyboards import keyboards_admin as kb_a
from keyboards import keyboards_buyer as kb_b
from keyboards import keyboards_seller as kb_s
from keyboards import keyboards_common as kb_c

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


# Добавить информацию
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
                    'Выберите нужную категорию', language='alias'),reply_markup=kb_a.add_information)
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


# Добавить брэнд
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
                    '<b>Пример №1:</b>  "Добавить новый бренд: HQD"\n'
                    '<b>Пример №2:</b>  "Добавить новые бренды: HQD,Smoke,Vaporlax"', language='alias'),
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


# Добавить 1 брэнд
@dp.message_handler(lambda message: 'Добавить новый бренд:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новый бренд:')
                brand = result[1]
                if ',' in brand:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить новый бренд", но указываете несколько брендов\n'
                        'Чтобы добавить один брэнд, напишите как в примере \n\n'
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


# Добавить несколько брэндов
@dp.message_handler(lambda message: 'Добавить новые бренды:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новые бренды:')
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
                        'Чтобы добавить сразу несколько брэндов, напишите как в примере \n\n'
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


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'add_products')
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
                    'Напишите мне новый товар или товары\n'
                    'Структура товара такая (Категория),(Брэнд),(Наименование)\n\n'
                    '<b>Пример №1:</b>  "Добавить новый товар: Одноразовые сигареты,HQD,Cuvie"\n'
                    '<b>Пример №2:</b>  "Добавить новые товары: \nОдноразовые сигареты,HQD,Cuvie\nPod системы,Smok,Novo 4', language='alias'),
                                       parse_mode="HTML")
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Вы можете посмотреть существующие категории и бренды', language='alias'), reply_markup=kb_a.keyboard_categories_and_brands)

                '''markup_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_name = categories[1]
                    markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                          callback_data=f"categories_name_categories_name"))'''

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


@dp.callback_query_handler(lambda callback_query: 'all_categories_for_admin' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            all_categories = get_requests.get_all_categories()
            if all_categories:
                finish_string = create_text.create_view_categories(all_categories)
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    f'Ниже показаны все категории:\n'
                    f'{finish_string}', language='alias'))
            elif all_categories == False:
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: В базе данных нет информации по категориям', language='alias'))
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


'''@dp.callback_query_handler(lambda callback_query: 'admin_categories_name' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                'Это пустые кнопки, они созданы для того чтобы вы не напрягали свои глазки и не читали текст', language='alias'))
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
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))'''



@dp.callback_query_handler(lambda callback_query: 'all_brands_for_admin' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            eng_let = string.ascii_uppercase
            markup = types.InlineKeyboardMarkup(row_width=5)
            len_letter = len(eng_let)
            row = len_letter / 5
            row_remains = len_letter % 5
            row = int(row)

            counter = 0
            cou_let = 0
            while counter <= row:
                try:
                    markup.add(types.InlineKeyboardButton(text=eng_let[cou_let + 0],
                                                          callback_data=f"admin_brand_letter_{eng_let[cou_let + 0]}"),
                               types.InlineKeyboardButton(text=eng_let[cou_let + 1],
                                                          callback_data=f"admin_brand_letter_{eng_let[cou_let + 1]}"),
                               types.InlineKeyboardButton(text=eng_let[cou_let + 2],
                                                          callback_data=f"admin_brand_letter_{eng_let[cou_let + 2]}"),
                               types.InlineKeyboardButton(text=eng_let[cou_let + 3],
                                                          callback_data=f"admin_brand_letter_{eng_let[cou_let + 3]}"),
                               types.InlineKeyboardButton(text=eng_let[cou_let + 4],
                                                          callback_data=f"admin_brand_letter_{eng_let[cou_let + 4]}"),
                               )
                    counter += 1
                    cou_let += 5
                except Exception as ex:
                    except_counter = 0

                    while except_counter < row_remains:
                        markup.add(types.InlineKeyboardButton(text=eng_let[cou_let + 0],
                                                              callback_data=f"admin_brand_letter_{eng_let[cou_let + 0]}"))
                        except_counter += 1
                    break
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(callback_query.from_user.id,
                                   text='С какой буквы начинается брэнд?',
                                   reply_markup=markup)
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


@dp.callback_query_handler(lambda callback_query: 'admin_brand_letter_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            result = callback_query.data.split('admin_brand_letter_')
            letter = result[1]
            get_brands = get_requests.get_brands_starting_with_letter(letter)
            if get_brands:
                finish_string = create_text.create_view_brands(get_brands)
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    f'Ниже показаны все бренды начинающиеся с буквы "{letter}":\n'
                    f'{finish_string}', language='alias'))
            elif get_brands == False:
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    f':x: В Базе Данных нет брэндов начинающихся на {letter}', language='alias'))
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


@dp.message_handler(lambda message: 'Добавить новый товар:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новый товар:')
                product = result[1]
                if '\n' in product:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы сделали перенос строки, но выбрали: "Добавить новый товар"\n'
                        'Перенос строки следует использовать, при добавлении нескольких товаров\n'
                        'Чтобы добавить один товар, напишите как в примере \n\n'
                        'Структура товара такая (Категория),(Брэнд),(Наименование)\n'
                        '<b>Пример:</b>  "Добавить новый товар: Одноразовые сигареты,HQD,Cuvie"\n', language='alias'),parse_mode="HTML")
                else:
                    product_full = product.strip().split(',')
                    category = product_full[0].strip()
                    brand = product_full[1].strip()
                    name = product_full[2].strip()

                    category_in_db = get_requests.is_category_in_db(category)
                    brand_in_db = get_requests.is_brand_in_db(brand)

                    if category_in_db and brand_in_db:
                        is_product_in_db = get_requests.check_similar_product(category, brand, name)
                        if is_product_in_db:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукт {product_full} уже существует в Базе Данных', language='alias'))
                        elif is_product_in_db == False:
                            post_requests.add_product(category,brand,name)
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':white_check_mark: Я успешно записал продукт {product_full} в базу данных',
                                language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif category_in_db == False and brand_in_db:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Категории "{category}" не существует в Базе Данных\n'
                            f'Вам следует сначал добавить категорию, а потом создавать продукт', language='alias'))
                    elif category_in_db and brand_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Бренда "{brand}" не существует в Базе Данных\n'
                            f'Вам следует сначал добавить категорию, а потом создавать продукт', language='alias'))
                    elif category_in_db == False and brand_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Категории "{category}" не существует в Базе Данных\n'
                            f':x: Бренда "{brand}" не существует в Базе \n'
                            f'Вам следует сначал добавить категорию и бренд, а потом создавать продукт',
                            language='alias'))
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


@dp.message_handler(lambda message: 'Добавить новые товары:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить новые товары:')
                products = result[1]
                if '\n' in products:
                    products = products.split('\n')
                    for product in products:
                        product = product.strip()
                        if product == "":
                            continue
                        product_full = product.strip().split(',')
                        category = product_full[0].strip()
                        brand = product_full[1].strip()
                        name = product_full[2].strip()

                        category_in_db = get_requests.is_category_in_db(category)
                        brand_in_db = get_requests.is_brand_in_db(brand)

                        if category_in_db and brand_in_db:
                            is_product_in_db = get_requests.check_similar_product(category, brand, name)
                            if is_product_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Продукт {product_full} уже существует в Базе Данных', language='alias'))
                            elif is_product_in_db == False:
                                post_requests.add_product(category, brand, name)
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':white_check_mark: Я успешно записал продукт {product_full} в базу данных',
                                    language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif category_in_db == False and brand_in_db:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Категории "{category}" не существует в Базе Данных\n'
                                f'Вам следует сначал добавить категорию, а потом создавать продукт', language='alias'))
                        elif category_in_db and brand_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Бренда "{brand}" не существует в Базе Данных\n'
                                f'Вам следует сначал добавить категорию, а потом создавать продукт', language='alias'))
                        elif category_in_db == False and brand_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Категории "{category}" не существует в Базе Данных\n'
                                f':x: Бренда "{brand}" не существует в Базе \n'
                                f'Вам следует сначал добавить категорию и бренд, а потом создавать продукт',
                                language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))


                else:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':x: Вы указали один товар или не сделали перенос строки, но выбрали: "Добавить новые товары:"\n'
                            'Чтобы добавить несколько товаров, напишите как в примере \n\n'
                            'Структура товара такая (Категория),(Брэнд),(Наименование)\n'
                            '<b>Пример:</b>  "Добавить новые товары: \nОдноразовые сигареты,HQD,Cuvie\nPod системы,Smok,Novo 4', language='alias'),
                                       parse_mode="HTML")

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


@dp.callback_query_handler(lambda callback_query: callback_query.data == 'add_products_in_shop')
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.answer_callback_query(callback_query.id)

                markup_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_id = categories[0]
                    categories_name = categories[1]
                    markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                          callback_data=f"add_products_in_shop_{categories_id}"))

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':arrow_down: Выберите категорию, которую хотите заполнить', language='alias'),reply_markup=markup_categories)

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


@dp.callback_query_handler(lambda callback_query: 'add_products_in_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.answer_callback_query(callback_query.id)

                category_id = int(callback_query.data.split('add_products_in_shop_')[1])

                # Клавиатура товаров
                keyboard_add_products_in_shop = types.InlineKeyboardMarkup(resize_keyboard=True)
                kb_products = types.InlineKeyboardButton(text=emoji.emojize('Все товары', language='alias'),
                                                   callback_data=f'products_in_shop_cat_{category_id}')
                kb_shops = types.InlineKeyboardButton(text=emoji.emojize('Все магазины', language='alias'),
                                                callback_data='products_in_shop_shops')
                keyboard_add_products_in_shop.add(kb_products)
                keyboard_add_products_in_shop.add(kb_shops)


                if category_id == 1:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':arrow_down: Вы можете посмотреть существующие товары и магазины ', language='alias'),reply_markup=keyboard_add_products_in_shop)
                elif category_id == 2:
                    pass
                elif category_id == 3:
                    pass
                elif category_id == 4:
                    pass
                elif category_id == 5:
                    pass
                elif category_id == 6:
                    pass
                elif category_id == 7:
                    pass
                else:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: По всей видимости вы добавили новую категорию, но для нее не расписан алгоритм добавления товара\n'
                        'Вам стоит обратится к разработчику данного бота', language='alias'))
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


@dp.callback_query_handler(lambda callback_query: 'products_in_shop_shops' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.answer_callback_query(callback_query.id)

                all_shops = get_requests.all_shops()
                finish_text = create_text.create_view_shops(all_shops)
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Список магазинов\n\n'
                    f'{finish_text}', language='alias'))
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


@dp.callback_query_handler(lambda callback_query: 'products_in_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.answer_callback_query(callback_query.id)

                category_id = int(callback_query.data.split('add_products_in_shop_')[1])
                if category_id == 1:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':arrow_down: Вы можете посмотреть существующие товары и магазины ', language='alias'),reply_markup=kb_a.keyboard_add_products_in_shop)
                elif category_id == 2:
                    pass
                elif category_id == 3:
                    pass
                elif category_id == 4:
                    pass
                elif category_id == 5:
                    pass
                elif category_id == 6:
                    pass
                elif category_id == 7:
                    pass
                else:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: По всей видимости вы добавили новую категорию, но для нее не расписан алгоритм добавления товара\n'
                        'Вам стоит обратится к разработчику данного бота', language='alias'))
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