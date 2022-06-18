import logging
import string
from decimal import Decimal

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
@dp.message_handler(content_types=['text'],
                    text=emoji.emojize(':arrows_clockwise:    Изменить кол-во товара', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите нужную категорию', language='alias'), reply_markup=kb_a.edit_information)
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

########################################################################################################################
# Добавить информацию
########################################################################################################################
@dp.message_handler(content_types=['text'],
                    text=emoji.emojize(':heavy_plus_sign:    Добавить информацию', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите нужную категорию', language='alias'), reply_markup=kb_a.add_information)
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
                        '<b>Пример:</b> "Добавить новый бренд HQD"', language='alias'), parse_mode="HTML")
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
                        '<b>Пример:</b> "Добавить новые бренды HQD,Smoke,Vaporlax"', language='alias'),
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
                    'Структура товара такая: (Категория),(Брэнд),(Наименование),(Цена)\n\n'
                    '<b>Пример №1:</b>  "Добавить новый товар: Одноразовые сигареты,HQD,Cuvie,900"\n'
                    '<b>Пример №2:</b>  "Добавить новые товары: \nОдноразовые сигареты,HQD,Cuvie,900\nPod системы,Smok,Novo 4,2500',
                    language='alias'),
                                       parse_mode="HTML")
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Вы можете посмотреть существующие категории и бренды', language='alias'),
                                       reply_markup=kb_a.keyboard_categories_and_brands)

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
                        'Структура товара такая: (Категория),(Брэнд),(Наименование),(Цена)\n'
                        'Если "Цена" не целое число, записывайте его через "."'
                        '<b>Пример:</b>  "Добавить новый товар: Одноразовые сигареты,HQD,Cuvie,900"\n', language='alias'),
                                           parse_mode="HTML")
                else:
                    product_full = product.strip().split(',')
                    category = product_full[0].strip()
                    brand = product_full[1].strip()
                    name = product_full[2].strip()
                    price = float(product_full[3].strip())

                    category_in_db = get_requests.is_category_in_db(category)
                    brand_in_db = get_requests.is_brand_in_db(brand)

                    if category_in_db and brand_in_db:
                        is_product_in_db = get_requests.check_similar_product(category, brand, name)
                        if is_product_in_db:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукт {product_full} уже существует в Базе Данных', language='alias'))
                        elif is_product_in_db == False:
                            post_requests.add_product(category, brand, name,price)
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
                            f'Вам следует сначал добавить бренд, а потом создавать продукт', language='alias'))
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
                        price = float(product_full[3].strip())

                        category_in_db = get_requests.is_category_in_db(category)
                        brand_in_db = get_requests.is_brand_in_db(brand)

                        if category_in_db and brand_in_db:
                            is_product_in_db = get_requests.check_similar_product(category, brand, name)
                            if is_product_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Продукт {product_full} уже существует в Базе Данных', language='alias'))
                            elif is_product_in_db == False:
                                post_requests.add_product(category, brand, name,price)
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
                                f'Вам следует сначал добавить бренд, а потом создавать продукт', language='alias'))
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
                        'Структура товара такая: (Категория),(Брэнд),(Наименование),(Цена)\n'
                        'Если "Цена" не целое число, записывайте его через "."'
                        '<b>Пример:</b>  "Добавить новые товары: \nОдноразовые сигареты,HQD,Cuvie,357.8\nPod системы,Smok,Novo 4,2500',
                        language='alias'),
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

                markup_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_id = categories[0]
                    categories_name = categories[1]
                    markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                     callback_data=f"add_products_in_shop_{categories_id}"))
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':arrow_down: Выберите категорию, которую хотите заполнить', language='alias'),
                                       reply_markup=markup_categories)

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

                category_id = int(callback_query.data.split('add_products_in_shop_')[1])
                category_name = get_requests.check_category_name(category_id)
                # Клавиатура товаров
                if category_id == 1:
                    keyboard_add_products_in_shop = types.InlineKeyboardMarkup(resize_keyboard=True)
                    kb_add_products = types.InlineKeyboardButton(
                        text=emoji.emojize(f'Добавить "{category_name}"', language='alias'),
                        callback_data=f'products_add_in_shop_{category_id}')
                    kb_products = types.InlineKeyboardButton(text=emoji.emojize('Все товары', language='alias'),
                                                             callback_data=f'products_in_shop_cat_{category_id}')
                    kb_shops = types.InlineKeyboardButton(text=emoji.emojize('Все магазины', language='alias'),
                                                          callback_data='products_in_shop_shops')
                    kb_сharging_types = types.InlineKeyboardButton(text=emoji.emojize('Типы зарядки', language='alias'),
                                                             callback_data=f'products_in_shop_kb_сharging_types')
                    keyboard_add_products_in_shop.add(kb_add_products)
                    keyboard_add_products_in_shop.add(kb_products)
                    keyboard_add_products_in_shop.add(kb_shops)
                    keyboard_add_products_in_shop.add(kb_сharging_types)


                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':arrow_down: Выберите нужное вам действие:', language='alias'),
                                           reply_markup=keyboard_add_products_in_shop)
                elif category_id == 5:
                    keyboard_add_products_in_shop = types.InlineKeyboardMarkup(resize_keyboard=True)
                    kb_add_products = types.InlineKeyboardButton(
                        text=emoji.emojize(f'Добавить "{category_name}"', language='alias'),
                        callback_data=f'products_add_in_shop_{category_id}')
                    kb_products = types.InlineKeyboardButton(text=emoji.emojize('Все товары', language='alias'),
                                                             callback_data=f'products_in_shop_cat_{category_id}')
                    kb_shops = types.InlineKeyboardButton(text=emoji.emojize('Все магазины', language='alias'),
                                                          callback_data='products_in_shop_shops')
                    kb_size_charcoal = types.InlineKeyboardButton(text=emoji.emojize('Типы размеров', language='alias'),
                                                             callback_data=f'products_in_shop_kb_size_types')
                    keyboard_add_products_in_shop.add(kb_add_products)
                    keyboard_add_products_in_shop.add(kb_products)
                    keyboard_add_products_in_shop.add(kb_shops)
                    keyboard_add_products_in_shop.add(kb_size_charcoal)


                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':arrow_down: Выберите нужное вам действие:', language='alias'),
                                           reply_markup=keyboard_add_products_in_shop)
                else:
                    keyboard_add_products_in_shop = types.InlineKeyboardMarkup(resize_keyboard=True)
                    kb_add_products = types.InlineKeyboardButton(
                        text=emoji.emojize(f'Добавить "{category_name}"', language='alias'),
                        callback_data=f'products_add_in_shop_{category_id}')
                    kb_products = types.InlineKeyboardButton(text=emoji.emojize('Все товары', language='alias'),
                                                             callback_data=f'products_in_shop_cat_{category_id}')
                    kb_shops = types.InlineKeyboardButton(text=emoji.emojize('Все магазины', language='alias'),
                                                          callback_data='products_in_shop_shops')

                    keyboard_add_products_in_shop.add(kb_add_products)
                    keyboard_add_products_in_shop.add(kb_products)
                    keyboard_add_products_in_shop.add(kb_shops)

                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':arrow_down: Выберите нужное вам действие:', language='alias'),
                                           reply_markup=keyboard_add_products_in_shop)
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

# Типы размеров углей
@dp.callback_query_handler(lambda callback_query: 'products_in_shop_kb_size_types' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                all_size_charcoal = get_requests.all_size_charcoal()
                finish_text = create_text.create_view_size_charcoal(all_size_charcoal)
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Список типов зарядок\n\n'
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



# Типы зарядок
@dp.callback_query_handler(lambda callback_query: 'products_in_shop_kb_сharging_types' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                all_сharging_types = get_requests.all_сharging_types()
                finish_text = create_text.create_view_сharging_types(all_сharging_types)
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Список типов зарядок\n\n'
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


@dp.callback_query_handler(lambda callback_query: 'products_in_shop_cat_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                category_id = int(callback_query.data.split('products_in_shop_cat_')[1])
                products = get_requests.check_products_with_category(category_id)
                if products:
                    finish_text = create_text.create_view_products_with_category(products)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Список товаров:\n\n'
                        f'{finish_text}', language='alias'),parse_mode="HTML")
                elif not products:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: В данной категории еще нет товара', language='alias'))

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


@dp.callback_query_handler(lambda callback_query: 'products_add_in_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                category_id = int(callback_query.data.split('products_add_in_shop_')[1])
                categoty_name = get_requests.check_category_name(category_id)
                if category_id == 1:
                    if categoty_name is not None:
                        if categoty_name == 'Одноразовые сигареты':
                            short_cat = 'Одноразовую сигарету'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Кол-во тяг),(Тип зарядки),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 1,1,Спелая вишня,1500,1,20"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 1,1,Спелая вишня,1500,2,20\n'
                                f'1,22,Кислый виноград,1500,3,20"', language='alias'),
                                                   parse_mode="HTML")
                elif category_id == 2:
                    if categoty_name is not None:
                        if categoty_name == 'Жидкости':
                            short_cat = 'Жидкость'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Крепость),(Объем),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 1,35,Кислые мишки,50,30,15"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 1,35,Кислые мишки,50,30,15\n'
                                f'1,35,Лимонный чай,40,30,20"', language='alias'),
                                                   parse_mode="HTML")
                elif category_id == 3:
                    if categoty_name is not None:
                        if categoty_name == 'POD системы':
                            short_cat = 'POD систему'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 2,35,20"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 2,35,10\n'
                                f'1,35,7"', language='alias'),
                                                   parse_mode="HTML")
                elif category_id == 4:
                    if categoty_name is not None:
                        if categoty_name == 'Комплектующие POD cистемы':
                            short_cat = 'Комплектующую POD cистемы'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 2,15,20"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 2,15,10\n'
                                f'1,17,7"', language='alias'),
                                                   parse_mode="HTML")
                elif category_id == 5:
                    if categoty_name is not None:
                        if categoty_name == 'Кальянный уголь':
                            categoty_name = 'Кальянные угли'
                            short_cat = 'Кальянный уголь'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какой {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во в коробке),(ID Размера),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 2,18,60,1,20"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 2,18,60,1,20\n'
                                f'2,18,90,1,20"', language='alias'),
                                                   parse_mode="HTML")

                elif category_id == 6:
                    if categoty_name is not None:
                        if categoty_name == 'Кальянный табак':
                            categoty_name = 'Кальянные табаки'
                            short_cat = 'Кальянный табак'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Объем),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 1,23,Шишки,20,15"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 1,23,Шишки,30,15\n'
                                f'1,37,Тархун,30,20"', language='alias'),
                                                   parse_mode="HTML")
                elif category_id == 7:
                    if categoty_name is not None:
                        if categoty_name == 'Электронные устройства':
                            short_cat = 'Электронное устройство'
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Напишите мне какие {categoty_name.lower()} и в какие магазины вы хотите добавить\n\n'
                                'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример №1:</b>  "Добавить {short_cat.lower()}: 2,53,5"\n'
                                f'<b>Пример №2:</b>  "Добавить {categoty_name.lower()}: 2,53,5\n'
                                f'1,17,3"', language='alias'),
                                                   parse_mode="HTML")
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


# Добавить одноразовую сигарету
@dp.message_handler(lambda message: 'Добавить одноразовую сигарету:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Добавить одноразовую сигарету:')
                disposable_cigarettes = result[1]
                if '\n' in disposable_cigarettes:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить одноразовую сигарету", но указываете несколько сигарет\n'
                        'Чтобы добавить одну одноразовую сигарету, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Кол-во тяг),(Тип зарядки),(Кол-во штук)\n\n'
                        '<b>Пример:</b>  "Добавить одноразовую сигарету: 1,1,Спелая вишня,1500,1,20', language='alias'),
                                           parse_mode="HTML")
                else:
                    disposable_cigarettes = disposable_cigarettes.strip()
                    disposable_cigarettes = disposable_cigarettes.split(',')
                    shop_id = int(disposable_cigarettes[0].strip())
                    item_id = int(disposable_cigarettes[1].strip())
                    item_taste = disposable_cigarettes[2].strip()
                    item_count_traction = int(disposable_cigarettes[3].strip())
                    item_charging_type = int(disposable_cigarettes[4].strip())
                    item_count = int(disposable_cigarettes[5].strip())

                    category_id = 1
                    category_name = "Одноразовые сигареты"
                    short_category_name = "Одноразовой сигаретой"
                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            disposable_cigarettes_in_db = get_requests.check_similar_disposable_cigarettes(item_id, shop_id,item_taste,
                                                                                                           item_count_traction,item_charging_type)
                            if disposable_cigarettes_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} {item_taste} на {item_count_traction} затяжек c типом зарядки {item_charging_type} уже существует в магазине №{shop_id}', language='alias'))
                            elif disposable_cigarettes_in_db == False:
                                successfully_recorded = post_requests.add_disposable_cigarettes_in_shop(item_id, shop_id, item_taste, item_count_traction, item_charging_type , item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste} на {item_count_traction} затяжек c типом зарядки {item_charging_type} в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "{short_category_name}"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить одноразовые сигареты
@dp.message_handler(lambda message: 'Добавить одноразовые сигареты:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 1
                category_name = "Одноразовые сигареты"
                short_category_name = "Одноразовой сигаретой"

                result = message.text.split('Добавить одноразовые сигареты:')
                disposable_cigarettes = result[1]
                if '\n' in disposable_cigarettes:
                    disposable_cigarettes = disposable_cigarettes.split('\n')
                    for cigarettes in disposable_cigarettes:
                        cigarettes = cigarettes.strip()
                        if cigarettes == "":
                            continue
                        cigarettes_full = cigarettes.split(",")
                        shop_id = int(cigarettes_full[0].strip())
                        item_id = int(cigarettes_full[1].strip())
                        item_taste = cigarettes_full[2].strip()
                        item_count_traction = int(cigarettes_full[3].strip())
                        item_charging_type = int(cigarettes_full[4].strip())
                        item_count = int(cigarettes_full[5].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                disposable_cigarettes_in_db = get_requests.check_similar_disposable_cigarettes(item_id,
                                                                                                               shop_id,
                                                                                                               item_taste,
                                                                                                               item_count_traction,
                                                                                                               item_charging_type)
                                if disposable_cigarettes_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} {item_taste} на {item_count_traction} затяжек c типом зарядки {item_charging_type} уже существует в магазине №{shop_id}', language='alias'))
                                elif disposable_cigarettes_in_db == False:
                                    successfully_recorded = post_requests.add_disposable_cigarettes_in_shop(item_id, shop_id, item_taste,
                                                                            item_count_traction,item_charging_type, item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste} на {item_count_traction}  затяжек c типом зарядки {item_charging_type} в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "{short_category_name}"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить одноразовые сигареты", но указываете одну сигарету\n'
                        'Чтобы добавить несколько одноразовых сигарет, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Кол-во тяг),(Тип зарядки),(Кол-во штук)\n\n'
                        f'<b>Пример:</b>  "Добавить {category_name.lower()}: 1,1,Спелая вишня,1500,1,20\n'
                                f'1,22,Кислый виноград,1500,3,20"', language='alias'),
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


# Добавить жидкость
@dp.message_handler(lambda message: 'Добавить жидкость:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 2
                category_name = "Жидкости"
                short_cat = "Жидкость"

                result = message.text.split('Добавить жидкость:')
                vaping_liquids = result[1]
                if '\n' in vaping_liquids:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить жидкость", но указываете несколько жидкостей\n'
                        'Чтобы добавить одну жидкость, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Крепость),(Объем),(Кол-во штук)\n\n'
                                f'<b>Пример:</b>  "Добавить {short_cat.lower()}: 1,35,Кислые мишки,50,30,15"', language='alias'),
                                                   parse_mode="HTML")
                else:
                    vaping_liquids = vaping_liquids.strip()
                    vaping_liquids = vaping_liquids.split(',')
                    shop_id = int(vaping_liquids[0].strip())
                    item_id = int(vaping_liquids[1].strip())
                    item_taste = vaping_liquids[2].strip()
                    item_fortress = int(vaping_liquids[3].strip())
                    item_size = int(vaping_liquids[4].strip())
                    item_count = int(vaping_liquids[5].strip())

                    short_category_name = short_cat
                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            vaping_liquids_in_db = get_requests.check_similar_vaping_liquids(item_id, shop_id,item_taste,
                                                                                item_fortress,item_size)
                            if vaping_liquids_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} {item_taste} крепостью {item_fortress} мг. и объемом {item_size} мл. уже существует в магазине №{shop_id}', language='alias'))
                            elif vaping_liquids_in_db == False:
                                successfully_recorded = post_requests.add_vaping_liquids_in_shop(item_id, shop_id, item_taste,item_fortress,item_size,item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste} крепостью {item_fortress} мг. и объемом {item_size} мл. в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "Жидкостью"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить жидкости
@dp.message_handler(lambda message: 'Добавить жидкости:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 2
                category_name = "Жидкости"
                short_cat = "Жидкость"

                result = message.text.split('Добавить жидкости:')
                vaping_liquids = result[1]
                if '\n' in vaping_liquids:
                    vaping_liquids = vaping_liquids.split('\n')
                    for vaping_liquid in vaping_liquids:
                        vaping_liquid = vaping_liquid.strip()
                        if vaping_liquid == "":
                            continue
                        vaping_liquid_full = vaping_liquid.split(",")
                        shop_id = int(vaping_liquid_full[0].strip())
                        item_id = int(vaping_liquid_full[1].strip())
                        item_taste = vaping_liquid_full[2].strip()
                        item_fortress = int(vaping_liquid_full[3].strip())
                        item_size = int(vaping_liquid_full[4].strip())
                        item_count = int(vaping_liquid_full[5].strip())

                        short_category_name = short_cat
                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                vaping_liquids_in_db = get_requests.check_similar_vaping_liquids(item_id, shop_id,
                                                                                                 item_taste,
                                                                                                 item_fortress,
                                                                                                 item_size)
                                if vaping_liquids_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} {item_taste} крепостью {item_fortress} мг. и объемом {item_size} мл. уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif vaping_liquids_in_db == False:
                                    successfully_recorded = post_requests.add_vaping_liquids_in_shop(item_id, shop_id,
                                                                                                     item_taste,
                                                                                                     item_fortress,
                                                                                                     item_size,
                                                                                                     item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste} крепостью {item_fortress} мг. и объемом {item_size} мл. в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "Жидкостью"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить одноразовые сигареты", но указываете одну сигарету\n'
                        'Чтобы добавить несколько одноразовых сигарет, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Кол-во тяг),(Кол-во штук)\n\n'
                        f'<b>Пример:</b>  "Добавить {category_name.lower()}: 1,1,Спелая вишня,1500,20\n'
                                f'1,22,Кислый виноград,1500,20"', language='alias'),
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


# Добавить pod систему
@dp.message_handler(lambda message: 'Добавить pod систему:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 3
                category_name = "POD системы"
                short_cat = "POD система"

                result = message.text.split('Добавить pod систему:')
                pod = result[1]
                if '\n' in pod:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить pod систему:", но указываете несколько pod систем\n'
                        'Чтобы добавить pod систему, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример:</b>  "Добавить pod систему: 2,35,20"\n', language='alias'),
                                                   parse_mode="HTML")
                else:
                    pod = pod.strip()
                    pod = pod.split(',')
                    shop_id = int(pod[0].strip())
                    item_id = int(pod[1].strip())
                    item_count = int(pod[2].strip())

                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            vaping_pod_in_db = get_requests.check_similar_pod(item_id,shop_id)
                            if vaping_pod_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}', language='alias'))
                            elif vaping_pod_in_db == False:
                                successfully_recorded = post_requests.add_vaping_pod(item_id, shop_id, item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "POD системой"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить pod системы
@dp.message_handler(lambda message: 'Добавить pod системы:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 3
                category_name = "POD системы"
                short_cat = "POD система"

                result = message.text.split('Добавить pod системы:')
                pods = result[1]
                if '\n' in pods:
                    pods = pods.split('\n')
                    for pod in pods:
                        pod = pod.strip()
                        if pod == "":
                            continue
                        pod_full = pod.split(",")
                        shop_id = int(pod_full[0].strip())
                        item_id = int(pod_full[1].strip())
                        item_count = int(pod_full[2].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                vaping_pod_in_db = get_requests.check_similar_pod(item_id, shop_id)
                                if vaping_pod_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif vaping_pod_in_db == False:
                                    successfully_recorded = post_requests.add_vaping_pod(item_id, shop_id, item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "POD системой"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить одноразовые сигареты", но указываете одну сигарету\n'
                        'Чтобы добавить несколько одноразовых сигарет, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Кол-во тяг),(Кол-во штук)\n\n'
                        f'<b>Пример:</b>  "Добавить {category_name.lower()}: 1,1,Спелая вишня,1500,20\n'
                                f'1,22,Кислый виноград,1500,20"', language='alias'),
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


#Добавить комплектующую pod системы
@dp.message_handler(lambda message: 'Добавить комплектующую pod cистемы:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 4


                result = message.text.split('Добавить комплектующую pod cистемы:')
                pod_systems_accessories = result[1]
                if '\n' in pod_systems_accessories:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить комплектующую pod cистемы:", но указываете несколько комплектующих pod систем\n'
                        'Чтобы добавить комплектующую pod cистемы, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример</b>  "Добавить комплектующую pod cистемы: 2,15,20"\n', language='alias'),
                                                   parse_mode="HTML")
                else:
                    pod_systems_accessories = pod_systems_accessories.strip()
                    pod_systems_accessories = pod_systems_accessories.split(',')
                    shop_id = int(pod_systems_accessories[0].strip())
                    item_id = int(pod_systems_accessories[1].strip())
                    item_count = int(pod_systems_accessories[2].strip())

                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            pod_accessories_in_db = get_requests.check_similar_pod_accessories(item_id,shop_id)
                            if pod_accessories_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}', language='alias'))
                            elif pod_accessories_in_db == False:
                                successfully_recorded = post_requests.add_pod_accessories(item_id, shop_id, item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "Комплектующей pod cистемы"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить комплектующие pod системы
@dp.message_handler(lambda message: 'Добавить комплектующие pod cистемы:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 4
                category_name = "POD системы"
                short_cat = "POD система"

                result = message.text.split('Добавить комплектующие pod cистемы:')
                pod_systems_accessories = result[1]
                if '\n' in pod_systems_accessories:
                    pod_systems_accessories = pod_systems_accessories.split('\n')
                    for pod_systems_accessory in pod_systems_accessories:
                        pod_systems_accessory = pod_systems_accessory.strip()
                        if pod_systems_accessory == "":
                            continue
                        pod_pod_systems_accessory_full = pod_systems_accessory.split(",")
                        shop_id = int(pod_pod_systems_accessory_full[0].strip())
                        item_id = int(pod_pod_systems_accessory_full[1].strip())
                        item_count = int(pod_pod_systems_accessory_full[2].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                pod_accessories_in_db = get_requests.check_similar_pod_accessories(item_id, shop_id)
                                if pod_accessories_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif pod_accessories_in_db == False:
                                    successfully_recorded = post_requests.add_pod_accessories(item_id, shop_id, item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "Комплектующей pod cистемы"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить комплектующие pod cистемы:", но указываете одну комплектующую pod систем\n'
                        'Чтобы добавить несколько комплектующих pod cистемы, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример</b>  "Добавить комплектующие pod cистемы: 2,15,10\n'
                                f'1,17,7"\n', language='alias'),
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


# Добавить кальянный уголь
@dp.message_handler(lambda message: 'Добавить кальянный уголь:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 5

                result = message.text.split('Добавить кальянный уголь:')
                hookah_charcoal = result[1]
                if '\n' in hookah_charcoal:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить кальянный уголь", но указываете несколько кальянных углей\n'
                        'Чтобы добавить один кальянный уголь, напишите как в примере: \n\n'
                         'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во в коробке),(ID Размера),(Кол-во штук)\n\n'
                                f'<b>Пример:</b>  "Добавить кальянный уголь: 2,18,60,1,20"\n', language='alias'),
                                                   parse_mode="HTML")
                else:
                    hookah_charcoal = hookah_charcoal.strip()
                    hookah_charcoal = hookah_charcoal.split(',')
                    shop_id = int(hookah_charcoal[0].strip())
                    item_id = int(hookah_charcoal[1].strip())
                    item_count_in_box = int(hookah_charcoal[2].strip())
                    item_size = int(hookah_charcoal[3].strip())
                    item_count = int(hookah_charcoal[4].strip())

                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            hookah_charcoal_in_db = get_requests.check_similar_hookah_charcoal(item_id, shop_id,item_count_in_box,
                                                                                item_size)
                            if hookah_charcoal_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} с количесвом {item_count_in_box} в коробке и размером {item_size} уже существует в магазине №{shop_id}', language='alias'))
                            elif hookah_charcoal_in_db == False:
                                successfully_recorded = post_requests.add_vaping_hookah_charcoal(item_id, shop_id, item_count_in_box,item_size,item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id}  с количесвом {item_count_in_box} в коробке и размером {item_size} в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "Кальянный углем"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить кальянные угли
@dp.message_handler(lambda message: 'Добавить кальянные угли:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 5

                result = message.text.split('Добавить кальянные угли:')
                hookah_charcoals = result[1]
                if '\n' in hookah_charcoals:
                    hookah_charcoals = hookah_charcoals.split('\n')
                    for hookah_charcoal in hookah_charcoals:
                        hookah_charcoal = hookah_charcoal.strip()
                        if hookah_charcoal == "":
                            continue
                        hookah_charcoal_full = hookah_charcoal.split(",")

                        shop_id = int(hookah_charcoal_full[0].strip())
                        item_id = int(hookah_charcoal_full[1].strip())
                        item_count_in_box = int(hookah_charcoal_full[2].strip())
                        item_size = int(hookah_charcoal_full[3].strip())
                        item_count = int(hookah_charcoal_full[4].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                hookah_charcoal_in_db = get_requests.check_similar_hookah_charcoal(item_id, shop_id,
                                                                                                   item_count_in_box,
                                                                                                   item_size)
                                if hookah_charcoal_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} с количесвом {item_count_in_box} в коробке и размером {item_size} уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif hookah_charcoal_in_db == False:
                                    successfully_recorded = post_requests.add_vaping_hookah_charcoal(item_id, shop_id,
                                                                                                     item_count_in_box,
                                                                                                     item_size,
                                                                                                     item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id}  с количесвом {item_count_in_box} в коробке и размером {item_size} в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "Кальянный углем"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить кальянные угли:", но указываете один кальянный уголь\n'
                        'Чтобы добавить несколько кальянных углей, напишите как в примере: \n\n'
                         'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во в коробке),(ID Размера),(Кол-во штук)\n\n'
                                f'<b>Пример №2:</b>  "Добавить кальянные угли: 2,18,60,1,20\n'
                                f'2,18,90,2,20"', language='alias'),
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


# Добавить кальянный табак
@dp.message_handler(lambda message: 'Добавить кальянный табак:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 6

                result = message.text.split('Добавить кальянный табак:')
                hookah_tobacco = result[1]
                if '\n' in hookah_tobacco:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить кальянный табак:", но указываете несколько табаков\n'
                        'Чтобы добавить один кальянный табак, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Объем),(Кол-во штук)\n\n'
                        f'<b>Пример:</b>  "Добавить кальянный табак: 1,35,Кислые мишки,30,15"', language='alias'),
                                                   parse_mode="HTML")
                else:
                    hookah_tobacco = hookah_tobacco.strip()
                    hookah_tobacco = hookah_tobacco.split(',')
                    shop_id = int(hookah_tobacco[0].strip())
                    item_id = int(hookah_tobacco[1].strip())
                    item_taste = hookah_tobacco[2].strip()
                    item_size = int(hookah_tobacco[3].strip())
                    item_count = int(hookah_tobacco[4].strip())

                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            hookah_tobacco_in_db = get_requests.check_similar_hookah_tobacco(item_id, shop_id,item_taste,
                                                                                item_size)
                            if hookah_tobacco_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} {item_taste}, объемом {item_size} мг. уже существует в магазине №{shop_id}', language='alias'))
                            elif hookah_tobacco_in_db == False:
                                successfully_recorded = post_requests.add_hookah_tobacco_in_shop(item_id, shop_id, item_taste,item_size,item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste}, объемом {item_size} мг. в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "Кальянным табаком"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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

# Остановился тут
# Добавить кальянные табаки
@dp.message_handler(lambda message: 'Добавить кальянные табаки' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 6

                result = message.text.split('Добавить кальянные табаки:')
                hookah_tobacco = result[1]
                if '\n' in hookah_tobacco:
                    hookah_tobaccos = hookah_tobacco.split('\n')
                    for hookah_tobacco in hookah_tobaccos:
                        hookah_tobacco = hookah_tobacco.strip()
                        if hookah_tobacco == "":
                            continue
                        hookah_tobacco_full = hookah_tobacco.split(",")
                        shop_id = int(hookah_tobacco_full[0].strip())
                        item_id = int(hookah_tobacco_full[1].strip())
                        item_taste = hookah_tobacco_full[2].strip()
                        item_size = int(hookah_tobacco_full[3].strip())
                        item_count = int(hookah_tobacco_full[4].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                hookah_tobacco_in_db = get_requests.check_similar_hookah_tobacco(item_id, shop_id,
                                                                                                 item_taste,
                                                                                                 item_size)
                                if hookah_tobacco_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} {item_taste}, объемом {item_size} мг. уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif hookah_tobacco_in_db == False:
                                    successfully_recorded = post_requests.add_hookah_tobacco_in_shop(item_id, shop_id,
                                                                                                     item_taste,
                                                                                                     item_size,
                                                                                                     item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} {item_taste}, объемом {item_size} мг. в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "Кальянным табаком"', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить кальянные табаки:", но указываете один кальянный табак\n'
                        'Чтобы добавить несколько кальянных табаков, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Вкус),(Объем),(Кол-во штук)\n\n'
                        f'<b>Пример:</b>  "Добавить кальянные табаки: 1,23,Шишки,30,15\n'
                        f'1,37,Тархун,30,20"', language='alias'),
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


# Добавить электронное устройство
@dp.message_handler(lambda message: 'Добавить электронное устройство:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 7

                result = message.text.split('Добавить электронное устройство:')
                electronic_devices = result[1]
                if '\n' in electronic_devices:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить электронное устройство:", но указываете несколько устройств\n'
                        'Чтобы добавить электронное устройство, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример:</b>  "Добавить электронное устройство: 2,53,5"\n', language='alias'),
                                                   parse_mode="HTML")
                else:
                    electronic_devices = electronic_devices.strip()
                    electronic_devices = electronic_devices.split(',')
                    shop_id = int(electronic_devices[0].strip())
                    item_id = int(electronic_devices[1].strip())
                    item_count = int(electronic_devices[2].strip())

                    is_product_in_db = get_requests.is_product_in_db(item_id)
                    if is_product_in_db:
                        is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id, category_id)
                        if is_product_corresponds_category:
                            electronic_devices_in_db = get_requests.check_similar_electronic_devices(item_id,shop_id)
                            if electronic_devices_in_db:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                     f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}', language='alias'))
                            elif electronic_devices_in_db == False:
                                successfully_recorded = post_requests.add_electronic_devices(item_id, shop_id, item_count)
                                if successfully_recorded:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                        language='alias'))
                                elif successfully_recorded == False:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_corresponds_category == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Предмет с ID {item_id} не является "Электронным устройством"', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_product_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
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


# Добавить электронные устройства
@dp.message_handler(lambda message: 'Добавить электронные устройства:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = 7

                result = message.text.split('Добавить электронные устройства:')
                electronic_devices = result[1]
                if '\n' in electronic_devices:
                    electronic_devices = electronic_devices.split('\n')
                    for electronic_device in electronic_devices:
                        electronic_device = electronic_device.strip()
                        if electronic_device == "":
                            continue
                        electronic_device_full = electronic_device.split(",")
                        shop_id = int(electronic_device_full[0].strip())
                        item_id = int(electronic_device_full[1].strip())
                        item_count = int(electronic_device_full[2].strip())

                        is_product_in_db = get_requests.is_product_in_db(item_id)
                        if is_product_in_db:
                            is_product_corresponds_category = get_requests.is_product_corresponds_category(item_id,
                                                                                                           category_id)
                            if is_product_corresponds_category:
                                electronic_devices_in_db = get_requests.check_similar_electronic_devices(item_id,
                                                                                                         shop_id)
                                if electronic_devices_in_db:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        f':x: Продукт ID {item_id} уже существует в магазине №{shop_id}',
                                        language='alias'))
                                elif electronic_devices_in_db == False:
                                    successfully_recorded = post_requests.add_electronic_devices(item_id, shop_id,
                                                                                                 item_count)
                                    if successfully_recorded:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            f':white_check_mark: Я успешно записал {item_count} шт. продукта ID {item_id} в магазин №{shop_id}',
                                            language='alias'))
                                    elif successfully_recorded == False:
                                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                                else:
                                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                            elif is_product_corresponds_category == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Предмет с ID {item_id} не является "Электронным устройством"',
                                    language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                        elif is_product_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукта с ID {item_id} нет в базе данных', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы написали: "Добавить электронные устройства:", но указываете одно электронное устройство\n'
                        'Чтобы добавить несколько электронных устройств, напишите как в примере: \n\n'
                        'Структура товара в магазине такая:\n(№ Магазина),(ID Товара),(Кол-во штук)\n\n'
                                f'<b>Пример:</b>  "Добавить электронные устройства: 2,53,5\n'
                        f'1,53,5"\n', language='alias'),
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


########################################################################################################################
# Изменить информацию
########################################################################################################################
# Изменить брэнд
@dp.callback_query_handler(lambda callback_query: 'edit_brand' == callback_query.data)
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
                    'Напишите мне какой бренд или бренды вы хотите изменить\n\n'
                    'Структура бренда такая:\n(ID Бренда),(Наименование бренда)\n\n'
                    f'<b>Пример:</b>  "Изменить бренд: 1,Hqd"\n', language='alias'),
                                       parse_mode="HTML")
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Вы можете посмотреть все бренды', language='alias'), reply_markup=kb_a.keyboard_brands)
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


# Изменить бренд
@dp.message_handler(lambda message: 'Изменить бренд:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                result = message.text.split('Изменить бренд:')
                brand = result[1].strip()
                if ',' in brand:
                    brand = brand.split(',')
                    brand_id = brand[0].strip()
                    brand_name = brand[1].strip()
                    is_brand_in_db = get_requests.check_brand_in_id(brand_id)
                    if is_brand_in_db:
                        successful_update = post_requests.update_brand_in_id(brand_id,brand_name)
                        if successful_update:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':white_check_mark: Я успешно обновил данные, теперь бренд с ID {brand_id}: {brand_name}'
                                f'', language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    elif is_brand_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Бренда с ID {brand_id} не существует в базе данных', language='alias'))
                    else:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':x: Вы не указали ID или название, а возможно забыли поставить запятую', language='alias'))

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


# Изменить товар
@dp.callback_query_handler(lambda callback_query: 'edit_products' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                markup_edit_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_id = categories[0]
                    categories_name = categories[1]
                    markup_edit_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                     callback_data=f"edit_products_{categories_id}"))
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':arrow_down: Выберите категорию, которую хотите изменить', language='alias'),
                                       reply_markup=markup_edit_categories)

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


# Изменить товар в магазине
@dp.callback_query_handler(lambda callback_query: 'edit_products_in_shop' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:

                markup_all_shops = types.InlineKeyboardMarkup(row_width=2)
                all_shops = get_requests.all_shops()
                for shop in all_shops:
                    shop_id = shop[0]
                    shop_city = shop[1]
                    shop_street = shop[2]
                    shop_house = shop[3]
                    markup_all_shops.add(types.InlineKeyboardButton(text=f'№{shop_id} г.{shop_city}, ул.{shop_street}, д.{shop_house}',
                                                                     callback_data=f"edit_products_in_shop_{shop_id}"))
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':arrow_down: Выберите магазин, в который хотите внести изменения', language='alias'),
                                       reply_markup=markup_all_shops)

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


#Изменить товар в магазине
@dp.callback_query_handler(lambda callback_query: 'edit_products_in_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                shop_id = int(callback_query.data.split('edit_products_in_shop_')[1])
                shop = get_requests.get_shop_by_id(shop_id)
                shop_id = shop[0]
                shop_city = shop[1]
                shop_street = shop[2]
                shop_house = shop[3]
                markup_shop = types.InlineKeyboardMarkup()
                markup_shop.add(types.InlineKeyboardButton(text=f'Все товары',
                                                                 callback_data=f"info_product_in_shop_{shop_id}"))

                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Напишите мне у какого товара вы хотите изменить кол-во\n'
                    '',
                    language='alias'),
                                       parse_mode="HTML")
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    f'Вы можете посмотреть все товары в магазине: №{shop_id} г.{shop_city}, ул.{shop_street}, д.{shop_house}', language='alias'),
                                       reply_markup=markup_shop)


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



@dp.callback_query_handler(lambda callback_query: 'info_product_in_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                shop_id = int(callback_query.data.split('info_product_in_shop_')[1])

                disposable_cigarettes = get_requests.get_disposable_cigarettes_by_shopid(shop_id)
                if disposable_cigarettes:
                    disposable_cigarettes_text = create_text.create_view_disposable_cigarettes(disposable_cigarettes)
                elif disposable_cigarettes == False:
                    disposable_cigarettes_text  = "<b>Одноразовые сигареты</b>\n" \
                                                                 "Список пуст"
                else:
                    disposable_cigarettes_text = "<b>Одноразовые сигареты</b>\n" \
                                                                 "Возникли ошибки при работе с базой данных"


                vaping_liquids = get_requests.get_vaping_liquids_by_shopid(shop_id)
                if vaping_liquids:
                    vaping_liquids_text = create_text.create_view_vaping_liquids(vaping_liquids)
                elif vaping_liquids == False:
                    vaping_liquids_text = "<b>Жидкости</b>\n" \
                                                                 "Список пуст"
                else:
                    vaping_liquids_text = "<b>Жидкости</b>\n" \
                                    "Возникли ошибки при работе с базой данных"


                pod_systems = get_requests.get_pod_systems_by_shopid(shop_id)
                if pod_systems:
                    pod_systems_text = create_text.create_view_pod_systems(pod_systems)
                elif pod_systems == False:
                    pod_systems_text = "<b>POD системы</b>\n" \
                                          "Список пуст"
                else:
                    pod_systems_text = "<b>POD системы</b>\n" \
                                          "Возникли ошибки при работе с базой данных"

                pod_systems_accessories = get_requests.get_pod_systems_accessories_by_shopid(shop_id)
                if pod_systems_accessories:
                    pod_systems_accessories_text = create_text.create_view_pod_systems_accessories(pod_systems_accessories)
                elif pod_systems_accessories == False:
                    pod_systems_accessories_text = "<b>Аксессуары POD систем</b>\n" \
                                       "Список пуст"
                else:
                    pod_systems_accessories_text = "<b>Аксессуары POD систем</b>\n" \
                                       "Возникли ошибки при работе с базой данных"

                hookah_charcoal = get_requests.get_hookah_charcoal_by_shopid(shop_id)
                if hookah_charcoal:
                    hookah_charcoal_text = create_text.create_view_hookah_charcoal(
                        hookah_charcoal)
                elif hookah_charcoal == False:
                    hookah_charcoal_text = "<b>Кальянный уголь</b>\n" \
                                                   "Список пуст"
                else:
                    hookah_charcoal_text = "<b>Кальянный уголь</b>\n" \
                                                   "Возникли ошибки при работе с базой данных"

                hookah_tobacco = get_requests.get_hookah_tobacco_by_shopid(shop_id)
                if hookah_tobacco:
                    hookah_tobacco_text = create_text.create_view_hookah_tobacco(
                        hookah_tobacco)
                elif hookah_tobacco == False:
                    hookah_tobacco_text = "<b>Кальянный уголь</b>\n" \
                                           "Список пуст"
                else:
                    hookah_tobacco_text = "<b>Кальянный уголь</b>\n" \
                                           "Возникли ошибки при работе с базой данных"

                electronic_devices = get_requests.get_electronic_devices_by_shopid(shop_id)
                if electronic_devices:
                    electronic_devices_text = create_text.create_view_electronic_devices(
                        electronic_devices)
                elif electronic_devices == False:
                    electronic_devices_text = "<b>Электронные устройства</b>\n" \
                                          "Список пуст"
                else:
                    electronic_devices_text = "<b>Электронные устройства</b>\n" \
                                          "Возникли ошибки при работе с базой данных"

                await bot.answer_callback_query(callback_query.id)

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    disposable_cigarettes_text,language='alias'),parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    vaping_liquids_text,language='alias'), parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    pod_systems_text,language='alias'),parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    pod_systems_accessories_text, language='alias'), parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    hookah_charcoal_text, language='alias'), parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    hookah_tobacco_text, language='alias'), parse_mode="HTML")

                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    electronic_devices_text, language='alias'), parse_mode="HTML")



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


# Изменить товар
@dp.callback_query_handler(lambda callback_query: 'edit_products_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                category_id = callback_query.data.split('edit_products_')[1]
                category_name = get_requests.check_category_name(category_id)

                markup_categories = types.InlineKeyboardMarkup()
                markup_categories.add(types.InlineKeyboardButton(text=f'Все товары из категории "{category_name}"',
                                                                 callback_data=f"products_in_shop_cat_{category_id}"))

                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Напишите мне ID товара, который вы хотите изменить, а также обновленную информацию\n'
                    'Структура товара такая: (ID Товара),(Брэнд),(Наименование),(Цена)\n'
                    'Если "Цена" не целое число, записывайте его через "."\n\n'
                    '<b>Пример №1:</b>  "Изменить товар: 15,HQD,Cuvie,1200"\n'
                    '<b>Пример №2:</b>  "Изменить товары: 15,HQD,Cuvie,1500\n13,Smok,Gun +,900.5',
                    language='alias'),
                                       parse_mode="HTML")
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    f'Вы можете посмотреть существующие товары в категории: "{category_name}"\n', language='alias'),
                                       reply_markup=markup_categories)


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



@dp.message_handler(lambda message: 'Изменить товар:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Изменить товар:')
                product = result[1]
                if '\n' in product:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы сделали перенос строки, но выбрали: "Изменить товар"\n'
                        'Перенос строки следует использовать, при изменении нескольких товаров\n'
                        'Чтобы изменить один товар, напишите как в примере \n\n'
                        'Структура изменения товара такая:  (ID Товара),(Брэнд),(Наименование),(Цена)\n'
                        'Если "Цена" не целое число, записывайте его через "."'
                        '<b>Пример:</b>  "Изменить товар: 15,HQD,Cuvie,550.5"\n', language='alias'),
                                           parse_mode="HTML")
                else:
                    product_full = product.strip().split(',')
                    product_id = product_full[0].strip()
                    brand = product_full[1].strip()
                    name = product_full[2].strip()
                    price = float(product_full[3].strip())

                    category_id =get_requests.check_category_by_product(product_id)
                    category_name = get_requests.check_category_name(category_id)
                    brand_in_db = get_requests.is_brand_in_db(brand)

                    if brand_in_db:
                        is_product_in_db = get_requests.check_similar_product(category_name, brand, name)
                        if is_product_in_db:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Продукт {product_full} уже существует в Базе Данных', language='alias'))
                        elif is_product_in_db == False:
                            post_requests.update_product(brand, name,price,product_id)
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':white_check_mark: Я успешно обновил продукт {product_full} в базе данных',
                                language='alias'))
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                    elif brand_in_db == False:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            f':x: Бренда "{brand}" не существует в Базе Данных\n'
                            f'Вам следует сначал добавить бренд, а потом создавать продукт', language='alias'))

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


@dp.message_handler(lambda message: 'Изменить товары:' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_admin = get_requests.check_user_is_admin(user_id)
            if user_is_admin:
                result = message.text.split('Изменить товары:')
                products = result[1]
                if '\n' in products:
                    products = products.split('\n')
                    for product in products:
                        product = product.strip()
                        if product == "":
                            continue
                        product_full = product.strip().split(',')
                        product_id = product_full[0].strip()
                        brand = product_full[1].strip()
                        name = product_full[2].strip()
                        price = float(product_full[3].strip())

                        category_id = get_requests.check_category_by_product(product_id)
                        category_name = get_requests.check_category_name(category_id)
                        brand_in_db = get_requests.is_brand_in_db(brand)

                        if brand_in_db:
                            is_product_in_db = get_requests.check_similar_product(category_name, brand, name)
                            if is_product_in_db:
                                post_requests.update_product(brand, name, price, product_id)
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':white_check_mark: Я успешно обновил продукт {product_full} в базе данных',
                                    language='alias'))

                            elif is_product_in_db == False:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    f':x: Продукта {product_full} не существует в Базе Данных', language='alias'))
                            else:
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                        elif brand_in_db == False:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                f':x: Бренда "{brand}" не существует в Базе Данных\n'
                                f'Вам следует сначал добавить бренд, а потом создавать продукт', language='alias'))

                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))


                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Вы указали один товар или не сделали перенос строки, но выбрали: "Изменить товары:"\n'
                        'Чтобы добавить несколько товаров, напишите как в примере \n\n'
                        'Структура изменения товара такая:  (ID Товара),(Брэнд),(Наименование),(Цена)\n'
                        'Если "Цена" не целое число, записывайте его через "."'
                        '<b>Пример:</b>  "Изменить товары: 15,HQD,Cuvie,550.5"\n'
                        '17,HQD,Max,750', language='alias'),
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

