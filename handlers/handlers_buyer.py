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



#Просмотр товара через вкладку Товары
#Показывает 7 категорий
@dp.message_handler(content_types=['text'], text=emoji.emojize(':mag_right:    Товары', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                markup_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_id = categories[0]
                    categories_name = categories[1]
                    markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                     callback_data=f"check_products_category_{categories_id}"))
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите категорию, которая вас интересует:', language='alias'),
                                       reply_markup=markup_categories, )

            elif user_is_buyer == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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

# Пользователь выбрал главную категорию
@dp.callback_query_handler(lambda callback_query: 'check_products_category_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                category_id = int(callback_query.data.split('check_products_category_')[1])

                if category_id == 1:
                    all_brands = get_requests.check_all_brands_disposable_cigarettes_in_shops()
                    if all_brands:
                        markup_brands_disposable_cigarettes = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_disposable_cigarettes.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"check_brand_disposable_cigarette_{brand_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_disposable_cigarettes)
                    elif all_brands == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет одноразовых сигарет', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 2:
                    markup_liquid = types.InlineKeyboardMarkup()
                    markup_liquid.add(types.InlineKeyboardButton(text='По названию',callback_data=f"check_name_liquid"))
                    markup_liquid.add(types.InlineKeyboardButton(text='По крепости',callback_data=f"check_fortress_liquid"))
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите как отсортировать жидкости для вас:', language='alias'),
                                           reply_markup=markup_liquid)

                elif category_id == 3:
                    all_brands = get_requests.check_all_brands_pod_systems_in_shops()
                    if all_brands:
                        markup_brands_pod_systems = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_pod_systems.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"check_brand_pod_systems_{brand_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_pod_systems)
                    elif all_brands == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет POD cистем', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 4:
                    all_brands = get_requests.check_all_brands_pod_systems_accessories_in_shops()
                    if all_brands:
                        markup_brands_pod_systems = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_pod_systems.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"check_brand_pod_accessories_{brand_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_pod_systems)
                    elif all_brands == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет комплектующих POD cистем', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 5:
                    all_size = get_requests.check_all_size_hookah_charcoal_in_shops()
                    if all_size:
                        markup_size_hookah_charcoal = types.InlineKeyboardMarkup()
                        for size in all_size:
                            size_id = size[0]
                            size_name = size[1]
                            markup_size_hookah_charcoal.add(types.InlineKeyboardButton(text=size_name,
                                                                                     callback_data=f"check_size_hookah_charcoal_{size_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите размер угля, который вас интересует:', language='alias'),
                                               reply_markup=markup_size_hookah_charcoal)
                    elif all_size == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет кальянного угля', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 6:
                    all_brands = get_requests.check_all_brands_hookah_tobacco_in_shops()
                    if all_brands:
                        markup_brands_hookah_tobacco = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_hookah_tobacco.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"check_brand_hookah_tobacco_{brand_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_hookah_tobacco)
                    elif all_brands == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет кальянного табака', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                elif category_id == 7:
                    all_products = get_requests.check_all_electronic_devices_in_shops()
                    if all_products:
                        markup_all_electronic_devices = types.InlineKeyboardMarkup()
                        for item in all_products:
                            item_id = item[0]
                            item_brand = item[1]
                            item_name = item[2]
                            item_price = item[3]
                            markup_all_electronic_devices.add(types.InlineKeyboardButton(text=f'{item_brand} {item_name}, Цена: {item_price}',
                                                                             callback_data=f"c_edevice_{item_id}"))
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите электронное устройство, которое вас интересует:', language='alias'),
                                               reply_markup=markup_all_electronic_devices)
                    elif all_products == False:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: На данный момент в наших магазинах нет электронных устройств', language='alias'))
                    else:
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал сортировку по крепости
@dp.callback_query_handler(lambda callback_query: 'check_fortress_liquid' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                all_fortress = get_requests.check_liquid_fortress_in_all_shops()
                if all_fortress:
                    markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                    for fortress in all_fortress:
                        fortress_number = fortress[0]
                        markup_all_liquid_fortress.add(types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                       callback_data=f"fortress_liqiud_{fortress_number}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите крепость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid_fortress)
                elif all_fortress == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Нет информации по крепости жидкостей', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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



# Жидкости, Пользователь предлогается выбор вкусов в соответствии модель жидкости и крепостью выбранной до этого
@dp.callback_query_handler(lambda callback_query: 'name_fortress_liqiud_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                result = callback_query.data.split('name_fortress_liqiud_')[1]
                finish_item_fortress = int(result.split('_')[0])
                item_id = int(result.split('_')[1])

                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_liquid_by_id_and_fortress(item_id,finish_item_fortress)
                if all_taste:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for taste in all_taste:
                        item_id = taste[0]
                        taste = taste[1]
                        markup_products_name_and_price.add(
                            types.InlineKeyboardButton(text=f'{taste}',
                                                       callback_data=f"c_liq_{item_id}_{taste}_{finish_item_fortress}"))
                                                # callback_data = check_availability_liqiud'''
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                                     message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                           reply_markup=markup_products_name_and_price)

                elif not all_taste:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной жидкости нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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



# Жидкости, Пользователь выбрал крепость жидкости
@dp.callback_query_handler(lambda callback_query: 'fortress_liqiud_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_fortress = int(callback_query.data.split('fortress_liqiud_')[1])
                all_liquid = get_requests.check_all_liquid_by_fortress(item_fortress)
                if all_liquid:
                    markup_all_liquid = types.InlineKeyboardMarkup()
                    for liquid in all_liquid:
                        item_id = liquid[0]
                        brand_name = liquid[1]
                        item_name = liquid[2]
                        item_price = liquid[3]
                        markup_all_liquid.add(types.InlineKeyboardButton(text=f'{brand_name} {item_name}, Цена: {item_price}',
                                                       callback_data=f"model_liquid_fortress_{item_id}_{item_fortress}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите жидкость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid)
                elif all_liquid == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'В магазинах нет жидкости', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал модель жидкости в соответствии с крепостью выбранной до этого
@dp.callback_query_handler(lambda callback_query: 'model_liquid_fortress_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('model_liquid_fortress_')[1]
                item_id = int(full_info.split('_')[0])
                finish_item_fortress = int(full_info.split('_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_liquid_with_fortress(item_id,finish_item_fortress)
                if all_taste:
                    characteristic_product = get_requests.check_characteristic_liquid(item_id)
                    if characteristic_product:
                        if len(characteristic_product) == 1:
                            item_fortress = characteristic_product[2]
                            item_size = characteristic_product[3]
                            price = characteristic_product[4]
                            markup_products_name_and_price = types.InlineKeyboardMarkup()
                            for taste in all_taste:
                                item_id = taste[0]
                                taste = taste[1]
                                markup_products_name_and_price.add(
                                    types.InlineKeyboardButton(text=f'{taste}',
                                                               callback_data=f"c_liq_fort{item_id}_{taste}_{finish_item_fortress}"))
                                                        # callback_data = check_availability_liqiud
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг.:', language='alias'),
                                                   reply_markup=markup_products_name_and_price)
                        else:
                            list_fortress = ''
                            for characteristic in characteristic_product:
                                item_fortress = characteristic[2]
                                item_size = characteristic[3]
                                price = characteristic[4]
                                list_fortress += f' {item_fortress}мг. '

                            markup_products_name_and_price = types.InlineKeyboardMarkup()
                            for taste in all_taste:
                                item_id = taste[0]
                                taste = taste[1]
                                markup_products_name_and_price.add(
                                    types.InlineKeyboardButton(text=f'{taste}',
                                                               callback_data=f"c_liq_fort{item_id}_{taste}_{finish_item_fortress}"))
                                # callback_data = check_availability_liqiud
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                                   reply_markup=markup_products_name_and_price)

                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_liq_fort{item_id}_{taste}_{finish_item_fortress}"))
                            # callback_data = check_availability_liqiud
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'                    
                            f'Информация отсутствует', language='alias'), parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной жидкости нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал сортировку по названию и выбирает жидкость по бренду и вкусу
@dp.callback_query_handler(lambda callback_query: 'check_name_liquid' == callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                all_liquid = get_requests.check_liquid_info_in_all_shops()
                if all_liquid:
                    markup_all_liquid = types.InlineKeyboardMarkup()
                    for liquid in all_liquid:
                        item_id = liquid[0]
                        brand_name = liquid[1]
                        item_name = liquid[2]
                        item_price = liquid[3]
                        markup_all_liquid.add(types.InlineKeyboardButton(text=f'{brand_name} {item_name}, Цена: {item_price}',
                                                       callback_data=f"check_model_liqiud_{item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите жидкость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid)
                elif all_liquid == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'В магазинах нет жидкости', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователю выводится характеристика жидкости и выбор вкусов
@dp.callback_query_handler(lambda callback_query: 'check_model_liqiud_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_liqiud_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                characteristic_product = get_requests.check_characteristic_liquid(item_id)

                if characteristic_product:
                    if len(characteristic_product) == 1:
                        item_fortress = characteristic_product[0][2]
                        item_size = characteristic_product[0][3]
                        price = characteristic_product[0][4]

                        all_fortress = get_requests.check_liquid_fortress_in_all_shops_by_id(item_id)
                        if all_fortress:
                            markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                            for fortress in all_fortress:
                                fortress_number = fortress[0]
                                markup_all_liquid_fortress.add(
                                    types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                               callback_data=f"name_fortress_liqiud_{fortress_number}_{item_id}"))

                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Выберите крепость, которая вас интересует:', language='alias'),
                                                   reply_markup=markup_all_liquid_fortress)
                        elif all_fortress == False:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Нет информации о крепости жидкости <b>{product_brand} {product_name}</b>', language='alias'), parse_mode='HTML')
                        else:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    else:
                        list_fortress = ''
                        for characteristic in characteristic_product:
                            item_fortress = characteristic[2]
                            item_size = characteristic[3]
                            price = characteristic[4]
                            list_fortress += f' {item_fortress}мг. '
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        all_fortress = get_requests.check_liquid_fortress_in_all_shops_by_id(item_id)
                        if all_fortress:
                            markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                            for fortress in all_fortress:
                                fortress_number = fortress[0]
                                markup_all_liquid_fortress.add(
                                    types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                               callback_data=f"name_fortress_liqiud_{fortress_number}_{item_id}"))

                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Выберите крепость, которая вас интересует:', language='alias'),
                                                   reply_markup=markup_all_liquid_fortress)
                        elif all_fortress == False:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Нет информации о крепости жидкости <b>{product_brand} {product_name}</b>',
                                language='alias'), parse_mode='HTML')
                        else:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif characteristic_product == False:
                    all_fortress = get_requests.check_liquid_fortress_in_all_shops_by_id(item_id)
                    if all_fortress:
                        markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                        for fortress in all_fortress:
                            fortress_number = fortress[0]
                            markup_all_liquid_fortress.add(
                                types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                           callback_data=f"name_fortress_liqiud_{fortress_number}_{item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                        f'Информация отсутствует', language='alias'))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите крепость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid_fortress)
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал вкус в соответствии модель жидкости и крепостью выбранной до этого
# Жидкости, Пользователю покажутся магазины в которых выбранный вкус
@dp.callback_query_handler(lambda callback_query: 'c_liq_fort' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('c_liq_fort')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                fortress = int(model_full.split('_')[2])

                shops = get_requests.check_shop_id_by_liquid_fortress(item_id,taste,fortress)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]
                if shops:
                    finish_string = f'Магазины в которых есть жидкость <b>{product_brand} {product_name}</b> со вкусом <b>{taste}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif not shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Жидкости {product_brand}{product_name} со вкусом {taste} нет в магазинах', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


@dp.callback_query_handler(lambda callback_query: 'c_liq_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('c_liq_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                finish_item_fortress = int(model_full.split('_')[2])
                shops = get_requests.check_shop_id_by_liquid(item_id,taste,finish_item_fortress)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]
                if shops:
                    finish_string = f'Магазины в которых есть жидкость <b>{product_brand} {product_name}</b> со вкусом <b>{taste}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])

                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif not shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Жидкости {product_brand}{product_name} со вкусом {taste} нет в магазинах', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Одноразовые сигареты, Пользователь выбрал сортировку по брендам
@dp.callback_query_handler(lambda callback_query: 'check_brand_disposable_cigarette_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                brand_id = int(callback_query.data.split('check_brand_disposable_cigarette_')[1])

                products_name_and_price = get_requests.check_disposable_cigarette_name_and_price_by_brand_id(brand_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"check_model_disposable_cigarette_{product_item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Одноразовые сигареты, Пользователь выбрал модель в соответствии с брендом выбранным до этого
# Одноразовые сигареты, Просмотр характеристики
@dp.callback_query_handler(lambda callback_query: 'check_model_disposable_cigarette_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_disposable_cigarette_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_disposable_cigarette(item_id)
                if all_taste:

                    characteristic_product = get_requests.check_characteristic_disposable_cigarette(item_id)
                    if characteristic_product:
                        item_count_traction = characteristic_product[2]
                        item_charging_type = characteristic_product[3]
                        price = characteristic_product[4]
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_disp_{item_id}_{taste}"))
                                                            # callback_data = check_availability_disposable_cigarette
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Кол-во затяжек: {item_count_traction}\n'
                            f'Тип зарядки: {item_charging_type}\n'
                            f'Цена: {price}', language='alias'),parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_disp_{item_id}_{taste}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует', language='alias'))
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной модели нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Одноразовые сигареты, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'c_disp_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('c_disp_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]

                shops = get_requests.check_shop_id_by_disposable_cigarettes(item_id,taste)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]
                if shops:
                    finish_string = f'Магазины в которых есть одноразовая сигарета <b>{product_brand} {product_name}</b> со вкусом <b>{taste}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Одноразовой сигареты {product_brand}{product_name} со вкусом {taste} нет в магазинах', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы, Пользователь выбрал сортировку по брендам
@dp.callback_query_handler(lambda callback_query: 'check_brand_pod_systems_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                brand_id = int(callback_query.data.split('check_brand_pod_systems_')[1])

                products_name_and_price = get_requests.check_pod_systems_name_and_price_by_brand_id(brand_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"check_model_pod_systems_{product_item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы, Наличие модели в магазинах
@dp.callback_query_handler(lambda callback_query: 'check_model_pod_systems_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_pod_systems_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops = get_requests.check_shop_id_by_pod_systems(item_id)

                if shops:
                    finish_string = f'Магазины в которых есть POD Система <b>{product_brand} {product_name}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Pod системы <b>{product_brand} {product_name}</b> нет в магазинах',
                        language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы аксессуары, Пользователь выбрал сортировку по брендам
@dp.callback_query_handler(lambda callback_query: 'check_brand_pod_accessories_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                brand_id = int(callback_query.data.split('check_brand_pod_accessories_')[1])

                products_name_and_price = get_requests.check_pod_accessories_name_and_price_by_brand_id(brand_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"check_model_pod_accessories_{product_item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы аксессуары, Наличие модели в магазинах
@dp.callback_query_handler(lambda callback_query: 'check_model_pod_accessories_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_pod_accessories_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops = get_requests.check_shop_id_by_pod_accessories(item_id)

                if shops:
                    finish_string = f'Магазины в которых есть Комплектующая POD системы <b>{product_brand} {product_name}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Комплектующей Pod системы <b>{product_brand} {product_name}</b> нет в магазинах',
                        language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный уголь, Пользователь выбрал сортировку по размерам
@dp.callback_query_handler(lambda callback_query: 'check_size_hookah_charcoal_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                size_id = int(callback_query.data.split('check_size_hookah_charcoal_')[1])

                products_name_and_price = get_requests.check_hookah_charcoal_name_and_price_by_size_id(size_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"check_model_hookah_charcoal_{product_item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный уголь, Характеристика и магазины
@dp.callback_query_handler(lambda callback_query: 'check_model_hookah_charcoal_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_hookah_charcoal_')[1])


                shops = get_requests.check_shop_id_by_hookah_charcoal(item_id)
                characteristic_product = get_requests.check_characteristic_hookah_charcoal(item_id)
                if characteristic_product:
                    item_brand = characteristic_product[0]
                    item_name = characteristic_product[1]
                    item_size = characteristic_product[2]
                    item_count_in_box = characteristic_product[3]
                    item_price = characteristic_product[4]
                    if shops:
                        finish_string = f'Магазины в которых есть Кальянный уголь <b>{item_brand} {item_name}</b>:\n'
                        for shop_id in shops:
                            shops_info = get_requests.get_shop_by_id(shop_id[0])
                            shop_city = shops_info[1]
                            shop_street = shops_info[2]
                            shop_house = shops_info[3]
                            finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                        # callback_data = check_availability_disposable_cigarette
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'{finish_string}', language='alias'), parse_mode='HTML')

                    elif shops == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'Кальянного угля <b>{item_brand} {item_name}</b> нет в магазинах',
                            language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'Кальянный уголь <b>{item_brand} {item_name}</b> в магазинах:\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            language='alias'), parse_mode='HTML')

                elif characteristic_product == False:
                    product = get_requests.get_product_brand_and_name(item_id)
                    item_brand = product[0]
                    item_name = product[1]
                    if shops:
                        finish_string = f'Магазины в которых есть Кальянный уголь <b>{item_brand} {item_name}</b>:\n'
                        for shop_id in shops:
                            shops_info = get_requests.get_shop_by_id(shop_id[0])
                            shop_city = shops_info[1]
                            shop_street = shops_info[2]
                            shop_house = shops_info[3]
                            finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                        # callback_data = check_availability_disposable_cigarette

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'{finish_string}', language='alias'), parse_mode='HTML')
                    elif shops == False:

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'Кальянного угля <b>{item_brand} {item_name}</b> нет в магазинах',
                            language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'Кальянный уголь <b>{item_brand} {item_name}</b> в магазинах:\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            language='alias'), parse_mode='HTML')

                else:
                    product = get_requests.get_product_brand_and_name(item_id)
                    item_brand = product[0]
                    item_name = product[1]
                    if shops:
                        finish_string = f'Магазины в которых есть Кальянный уголь <b>{item_brand} {item_name}</b>:\n'
                        for shop_id in shops:
                            shops_info = get_requests.get_shop_by_id(shop_id[0])
                            shop_city = shops_info[1]
                            shop_street = shops_info[2]
                            shop_house = shops_info[3]
                            finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                        # callback_data = check_availability_disposable_cigarette

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            f'{finish_string}', language='alias'), parse_mode='HTML')
                    elif shops == False:

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            f'Кальянного угля <b>{item_brand} {item_name}</b> нет в магазинах',
                            language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            f'Кальянный уголь <b>{item_brand} {item_name}</b> в магазинах:\n'
                            f':pensive: Ошибка при работе с Базой Данных',
                            language='alias'), parse_mode='HTML')

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный табак, Пользователь выбрал бренд
@dp.callback_query_handler(lambda callback_query: 'check_brand_hookah_tobacco_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                brand_id = int(callback_query.data.split('check_brand_hookah_tobacco_')[1])

                products_name_and_price = get_requests.check_hookah_tobacco_name_and_price_by_brand_id(brand_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"check_model_hookah_tobacco_{product_item_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный табак, Пользователь выбрал модель в соответствии с брендом выбранным до этого
# Кальянный табак, Просмотр характеристики
@dp.callback_query_handler(lambda callback_query: 'check_model_hookah_tobacco_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                item_id = int(callback_query.data.split('check_model_hookah_tobacco_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_hookah_tobacco(item_id)
                if all_taste:
                    characteristic_product = get_requests.check_characteristic_hookah_tobacco(item_id)
                    if characteristic_product:
                        item_size = characteristic_product[2]
                        price = characteristic_product[3]
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_htob_{item_id}_{taste}"))
                                                            # callback_data = check_availability_hookah_tobacco
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Объем : {item_size} г.\n'
                            f'Цена: {price}', language='alias'),parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_htob_{item_id}_{taste}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует', language='alias'))
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной модели нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный табак, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'c_htob_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('c_htob_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]

                shops = get_requests.check_shop_id_by_hookah_tobacco(item_id,taste)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]
                if shops:
                    finish_string = f'Магазины в которых есть Кальянный табак <b>{product_brand} {product_name}</b> со вкусом <b>{taste}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Кальянного табака  {product_brand}{product_name} со вкусом {taste} нет в магазинах', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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



# Электронные устройства, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'c_edevice_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('c_edevice_')[1]
                item_id = int(model_full)

                shops = get_requests.check_shop_id_by_electronic_devices(item_id)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]
                if shops:
                    finish_string = f'Магазины в которых есть Электронное устройство <b>{product_brand} {product_name}</b>:\n'
                    for shop_id in shops:
                        shops_info = get_requests.get_shop_by_id(shop_id[0])
                        shop_city = shops_info[1]
                        shop_street = shops_info[2]
                        shop_house = shops_info[3]
                        finish_string += f"Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        finish_string, language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Электронного устройства {product_brand}{product_name} нет в магазинах', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

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
                all_shops = get_requests.all_shops()
                markup_shops = types.InlineKeyboardMarkup()
                for shop in all_shops:
                    shop_id = shop[0]
                    shop_city = shop[1]
                    shop_street = shop[2]
                    shop_house = shop[3]
                    markup_shops.add(types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                                     callback_data=f"products_shop_{shop_id}"))
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите адрес магазина, для просмотра товара именно в нем:', language='alias'),
                                       reply_markup=markup_shops)

            elif user_is_buyer == False:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


#Показывает 7 категорий
@dp.callback_query_handler(lambda callback_query: 'products_shop_' in callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:
                shop_id = int(callback_query.data.split('products_shop_')[1])

                markup_categories = types.InlineKeyboardMarkup(row_width=2)
                all_categories = get_requests.get_all_categories()
                for categories in all_categories:
                    categories_id = categories[0]
                    categories_name = categories[1]
                    markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                     callback_data=f"products_category_{categories_id}_{shop_id}"))
                await bot.answer_callback_query(callback_query.id)
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    'Выберите категорию, которая вас интересует:', language='alias'),
                                       reply_markup=markup_categories, )

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Пользователь выбрал главную категорию
@dp.callback_query_handler(lambda callback_query: 'products_category_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('products_category_')[1]
                category_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if category_id == 1:
                    all_brands = get_requests.check_all_brands_disposable_cigarettes_in_shop(shop_id)
                    if all_brands:
                        markup_brands_disposable_cigarettes = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_disposable_cigarettes.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"shop_brand_disposable_cigarette_{brand_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_disposable_cigarettes)
                    elif all_brands == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет одноразовых сигарет', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 2:
                    markup_liquid = types.InlineKeyboardMarkup()
                    markup_liquid.add(types.InlineKeyboardButton(text='По названию',callback_data=f"shop_name_liquid_{shop_id}"))
                    markup_liquid.add(types.InlineKeyboardButton(text='По крепости',callback_data=f"shop_fortress_liquid_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите как отсортировать жидкости для вас:', language='alias'),
                                           reply_markup=markup_liquid)

                elif category_id == 3:
                    all_brands = get_requests.check_all_brands_pod_systems_in_shop(shop_id)
                    if all_brands:
                        markup_brands_pod_systems = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_pod_systems.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"shop_brand_pod_systems_{brand_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_pod_systems)
                    elif all_brands == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет POD cистем', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 4:
                    all_brands = get_requests.check_all_brands_pod_systems_accessories_in_shop(shop_id)
                    if all_brands:
                        markup_brands_pod_systems = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_pod_systems.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"shop_brand_pod_accessories_{brand_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_pod_systems)
                    elif all_brands == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет комплектующих POD cистем', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 5:
                    all_size = get_requests.check_all_size_hookah_charcoal_in_shop(shop_id)
                    if all_size:
                        markup_size_hookah_charcoal = types.InlineKeyboardMarkup()
                        for size in all_size:
                            size_id = size[0]
                            size_name = size[1]
                            markup_size_hookah_charcoal.add(types.InlineKeyboardButton(text=size_name,
                                                                                     callback_data=f"shop_size_hookah_charcoal_{size_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите размер угля, который вас интересует:', language='alias'),
                                               reply_markup=markup_size_hookah_charcoal)
                    elif all_size == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет кальянного угля', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif category_id == 6:
                    all_brands = get_requests.check_all_brands_hookah_tobacco_in_shop(shop_id)
                    if all_brands:
                        markup_brands_hookah_tobacco = types.InlineKeyboardMarkup()
                        for brand in all_brands:
                            brand_id = brand[0]
                            brand_name = brand[1]
                            markup_brands_hookah_tobacco.add(types.InlineKeyboardButton(text=brand_name,
                                                                             callback_data=f"shop_brand_hookah_tobacco_{brand_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите бренд, который вас интересует:', language='alias'),
                                               reply_markup=markup_brands_hookah_tobacco)
                    elif all_brands == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет кальянного табака', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                elif category_id == 7:
                    all_products = get_requests.check_all_electronic_devices_in_shop(shop_id)
                    if all_products:
                        markup_all_electronic_devices = types.InlineKeyboardMarkup()
                        for item in all_products:
                            item_id = item[0]
                            item_brand = item[1]
                            item_name = item[2]
                            item_price = item[3]
                            markup_all_electronic_devices.add(types.InlineKeyboardButton(text=f'{item_brand} {item_name}, Цена: {item_price}',
                                                                             callback_data=f"shop_edevice_c_{item_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите электронное устройство, которое вас интересует:', language='alias'),
                                               reply_markup=markup_all_electronic_devices)
                    elif all_products == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f':pensive: На данный момент в магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city} нет электронных устройств', language='alias'))
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


@dp.callback_query_handler(lambda callback_query: 'shop_brand_disposable_cigarette_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_brand_disposable_cigarette_')[1]
                brand_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                products_name_and_price = get_requests.shop_disposable_cigarette_name_and_price_by_brand_id(brand_id,shop_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"shop_model_disposable_cigarette_{product_item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара в магазине', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Одноразовые сигареты, Пользователь выбрал модель в соответствии с брендом выбранным до этого
# Одноразовые сигареты, Просмотр характеристики
@dp.callback_query_handler(lambda callback_query: 'shop_model_disposable_cigarette_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_disposable_cigarette_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.shop_taste_disposable_cigarette(item_id,shop_id)
                if all_taste:
                    characteristic_product = get_requests.check_characteristic_disposable_cigarette(item_id)
                    if characteristic_product:
                        item_count_traction = characteristic_product[2]
                        item_charging_type = characteristic_product[3]
                        price = characteristic_product[4]
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"shop_disp_{item_id}_{taste}_{shop_id}"))
                                                            # callback_data = check_availability_disposable_cigarette
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Кол-во затяжек: {item_count_traction}\n'
                            f'Тип зарядки: {item_charging_type}\n'
                            f'Цена: {price}', language='alias'),parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"c_disp_{item_id}_{taste}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует', language='alias'))
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной модели нет вкусов в магазине', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Одноразовые сигареты, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'shop_disp_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('shop_disp_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                shop_id = model_full.split('_')[2]

                shops = get_requests.is_disposable_cigarettes_in_shop(item_id,taste,shop_id)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Одноразовая сигарета <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')

                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Одноразовой сигареты <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал сортировку по крепости
@dp.callback_query_handler(lambda callback_query: 'shop_fortress_liquid_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                shop_id = int(callback_query.data.split('shop_fortress_liquid_')[1])

                all_fortress = get_requests.check_liquid_fortress_in_shop(shop_id)
                if all_fortress:
                    markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                    for fortress in all_fortress:
                        fortress_number = fortress[0]
                        markup_all_liquid_fortress.add(types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                       callback_data=f"shop_liqiud_fortress_{fortress_number}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите крепость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid_fortress)
                elif all_fortress == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Нет информации по крепости жидкостей', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал крепость жидкости
@dp.callback_query_handler(lambda callback_query: 'shop_liqiud_fortress_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_liqiud_fortress_')[1]
                item_fortress = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                all_liquid = get_requests.check_all_liquid_by_fortress_in_shop(item_fortress,shop_id)
                if all_liquid:
                    markup_all_liquid = types.InlineKeyboardMarkup()
                    for liquid in all_liquid:
                        item_id = liquid[0]
                        brand_name = liquid[1]
                        item_name = liquid[2]
                        item_price = liquid[3]
                        markup_all_liquid.add(types.InlineKeyboardButton(text=f'{brand_name} {item_name}, Цена: {item_price}',
                                                       callback_data=f"shop_model_liq_fort_{item_id}_{item_fortress}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите жидкость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid)
                elif all_liquid == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'В магазине нет жидкости', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал модель жидкости в соответствии с крепостью выбранной до этого
@dp.callback_query_handler(lambda callback_query: 'shop_model_liq_fort_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_liq_fort_')[1]
                item_id = int(full_info.split('_')[0])
                finish_item_fortress = int(full_info.split('_')[1])
                shop_id = int(full_info.split('_')[2])

                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_liquid_with_fortress_in_shop(item_id,finish_item_fortress,shop_id)
                if all_taste:
                    characteristic_product = get_requests.check_characteristic_liquid(item_id)
                    if characteristic_product:
                        if len(characteristic_product) == 1:
                            item_fortress = characteristic_product[2]
                            item_size = characteristic_product[3]
                            price = characteristic_product[4]
                            markup_products_name_and_price = types.InlineKeyboardMarkup()
                            for taste in all_taste:
                                item_id = taste[0]
                                taste = taste[1]
                                markup_products_name_and_price.add(
                                    types.InlineKeyboardButton(text=f'{taste}',
                                                               callback_data=f"liq_fort_shop_{item_id}_{taste}_{finish_item_fortress}_{shop_id}"))
                                                        # callback_data = check_availability_liqiud
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг.:', language='alias'),
                                                   reply_markup=markup_products_name_and_price)
                        else:
                            list_fortress = ''
                            for characteristic in characteristic_product:
                                item_fortress = characteristic[2]
                                item_size = characteristic[3]
                                price = characteristic[4]
                                list_fortress += f' {item_fortress}мг. '

                            markup_products_name_and_price = types.InlineKeyboardMarkup()
                            for taste in all_taste:
                                item_id = taste[0]
                                taste = taste[1]
                                markup_products_name_and_price.add(
                                    types.InlineKeyboardButton(text=f'{taste}',
                                                               callback_data=f"liq_fort_shop_{item_id}_{taste}_{finish_item_fortress}_{shop_id}"))
                                # callback_data = check_availability_liqiud
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                                   reply_markup=markup_products_name_and_price)

                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"liq_fort_shop_{item_id}_{taste}_{finish_item_fortress}_{shop_id}"))
                            # callback_data = check_availability_liqiud
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'                    
                            f'Информация отсутствует', language='alias'), parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной жидкости нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал вкус в соответствии модель жидкости и крепостью выбранной до этого
# Жидкости, Пользователю покажутся магазины в которых выбранный вкус
@dp.callback_query_handler(lambda callback_query: 'liq_fort_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('liq_fort_shop_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                fortress = int(model_full.split('_')[2])
                shop_id =int(model_full.split('_')[3])

                shops = get_requests.is_liquid_fortress_in_shop(item_id,taste,fortress,shop_id)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Жидкость <b>{product_brand} {product_name}</b> cо вкусом {taste}\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')

                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Жидкости <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь выбрал сортировку по названию и выбирает жидкость по бренду и вкусу
@dp.callback_query_handler(lambda callback_query: 'shop_name_liquid_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                shop_id = int(callback_query.data.split('shop_name_liquid_')[1])

                all_liquid = get_requests.check_liquid_info_in_shop(shop_id)
                if all_liquid:
                    markup_all_liquid = types.InlineKeyboardMarkup()
                    for liquid in all_liquid:
                        item_id = liquid[0]
                        brand_name = liquid[1]
                        item_name = liquid[2]
                        item_price = liquid[3]
                        markup_all_liquid.add(types.InlineKeyboardButton(text=f'{brand_name} {item_name}, Цена: {item_price}',
                                                       callback_data=f"shop_model_liq_{item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите жидкость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid)
                elif all_liquid == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'В магазинах нет жидкости', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователю выводится характеристика жидкости и выбор вкусов
@dp.callback_query_handler(lambda callback_query: 'shop_model_liq_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_liq_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                characteristic_product = get_requests.check_characteristic_liquid(item_id)

                if characteristic_product:
                    if len(characteristic_product) == 1:
                        item_fortress = characteristic_product[0][2]
                        item_size = characteristic_product[0][3]
                        price = characteristic_product[0][4]

                        all_fortress = get_requests.check_liquid_fortress_in_shop_by_item(item_id,shop_id)
                        if all_fortress:
                            markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                            for fortress in all_fortress:
                                fortress_number = fortress[0]
                                markup_all_liquid_fortress.add(
                                    types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                               callback_data=f"avail_liquid_{fortress_number}_{item_id}_{shop_id}"))

                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Выберите крепость, которая вас интересует:', language='alias'),
                                                   reply_markup=markup_all_liquid_fortress)
                        elif all_fortress == False:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {item_fortress} мг.\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Нет информации о крепости жидкости <b>{product_brand} {product_name}</b>', language='alias'), parse_mode='HTML')
                        else:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                    else:
                        list_fortress = ''
                        for characteristic in characteristic_product:
                            item_fortress = characteristic[2]
                            item_size = characteristic[3]
                            price = characteristic[4]
                            list_fortress += f' {item_fortress}мг. '
                        all_fortress = get_requests.check_liquid_fortress_in_shop_by_item(item_id,shop_id)
                        if all_fortress:
                            markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                            for fortress in all_fortress:
                                fortress_number = fortress[0]
                                markup_all_liquid_fortress.add(
                                    types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                               callback_data=f"avail_liquid_{fortress_number}_{item_id}_{shop_id}"))

                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Выберите крепость, которая вас интересует:', language='alias'),
                                                   reply_markup=markup_all_liquid_fortress)
                        elif all_fortress == False:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                                f'Крепость: {list_fortress}\n'
                                f'Размер: {item_size} мл.\n'
                                f'Цена: {price}', language='alias'), parse_mode='HTML')
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Нет информации о крепости жидкости <b>{product_brand} {product_name}</b>',
                                language='alias'), parse_mode='HTML')
                        else:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif characteristic_product == False:
                    all_fortress = get_requests.check_liquid_fortress_in_shop_by_item(item_id,shop_id)
                    if all_fortress:
                        markup_all_liquid_fortress = types.InlineKeyboardMarkup()
                        for fortress in all_fortress:
                            fortress_number = fortress[0]
                            markup_all_liquid_fortress.add(
                                types.InlineKeyboardButton(text=f'{fortress_number} мг.',
                                                           callback_data=f"avail_liquid_{fortress_number}_{item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                        f'Информация отсутствует', language='alias'))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите крепость, которая вас интересует:', language='alias'),
                                           reply_markup=markup_all_liquid_fortress)
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Жидкости, Пользователь предлогается выбор вкусов в соответствии модель жидкости и крепостью выбранной до этого
@dp.callback_query_handler(lambda callback_query: 'avail_liquid_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                result = callback_query.data.split('avail_liquid_')[1]
                finish_item_fortress = int(result.split('_')[0])
                item_id = int(result.split('_')[1])
                shop_id = int(result.split('_')[2])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.shop_taste_liquid_by_id_and_fortress(item_id,finish_item_fortress,shop_id)
                if all_taste:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for taste in all_taste:
                        item_id = taste[0]
                        taste = taste[1]
                        markup_products_name_and_price.add(
                            types.InlineKeyboardButton(text=f'{taste}',
                                                       callback_data=f"liq_c_shop_{item_id}_{taste}_{finish_item_fortress}_{shop_id}"))
                                                # callback_data = check_availability_liqiud'''
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                                     message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Выберите вкус, у жидкости {product_brand} {product_name}, {finish_item_fortress} мг. :', language='alias'),
                                           reply_markup=markup_products_name_and_price)

                elif not all_taste:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной жидкости нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


@dp.callback_query_handler(lambda callback_query: 'liq_c_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('liq_c_shop_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                finish_item_fortress = int(model_full.split('_')[2])
                shop_id = int(model_full.split('_')[3])

                shops = get_requests.is_liquid_fortress_in_shop(item_id, taste, finish_item_fortress, shop_id)
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]


                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Жидкость <b>{product_brand} {product_name}</b> cо вкусом {taste}\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')

                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Жидкости <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))



            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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






# Pod системы, Пользователь выбрал сортировку по брендам
@dp.callback_query_handler(lambda callback_query: 'shop_brand_pod_systems_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_brand_pod_systems_')[1]
                brand_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                products_name_and_price = get_requests.shop_pod_systems_name_and_price_by_brand_id(brand_id,shop_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"shop_model_pod_systems_{product_item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы, Наличие модели в магазинах
@dp.callback_query_handler(lambda callback_query: 'shop_model_pod_systems_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_pod_systems_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops = get_requests.is_pod_systems_in_shop(item_id,shop_id)
                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Pod система <b>{product_brand} {product_name}</b>\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Pod системы <b>{product_brand} {product_name}</b>\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Pod система <b>{product_brand} {product_name}</b>\n'
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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








# Pod системы аксессуары, Пользователь выбрал сортировку по брендам
@dp.callback_query_handler(lambda callback_query: 'shop_brand_pod_accessories_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_brand_pod_accessories_')[1]
                brand_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                products_name_and_price = get_requests.shop_pod_accessories_name_and_price_by_brand_id(brand_id,shop_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"shop_model_pod_accessories_{product_item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Pod системы аксессуары, Наличие модели в магазинах
@dp.callback_query_handler(lambda callback_query: 'shop_model_pod_accessories_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_pod_accessories_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops = get_requests.is_pod_accessories_in_shop(item_id, shop_id)
                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Комплектующая POD cистемы <b>{product_brand} {product_name}</b>\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Комплектующей POD cистемы <b>{product_brand} {product_name}</b>\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Комплектующая POD cистемы <b>{product_brand} {product_name}</b>\n'
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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









# Кальянный уголь, Пользователь выбрал сортировку по размерам
@dp.callback_query_handler(lambda callback_query: 'shop_size_hookah_charcoal_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_size_hookah_charcoal_')[1]
                size_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                products_name_and_price = get_requests.shop_hookah_charcoal_name_and_price_by_size_id(size_id,shop_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"shop_model_hookah_charcoal_{product_item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный уголь, Характеристика и магазины
@dp.callback_query_handler(lambda callback_query: 'shop_model_hookah_charcoal_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_hookah_charcoal_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])
                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                shops = get_requests.is_hookah_charcoal_in_shop(item_id, shop_id)
                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                characteristic_product = get_requests.check_characteristic_hookah_charcoal(item_id)

                if characteristic_product:
                    item_brand = characteristic_product[0]
                    item_name = characteristic_product[1]
                    item_size = characteristic_product[2]
                    item_count_in_box = characteristic_product[3]
                    item_price = characteristic_product[4]
                    if shops:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                    elif shops == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянного угля <b>{product_brand} {product_name}</b>\n'
                            f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{item_brand} {item_name}</b> :\n\n'
                            f'Размер углей: {item_size}\n'
                            f'Кол-во в пачке: {item_count_in_box}\n'
                            f'Цена: {item_price} \n\n'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif characteristic_product == False:
                    if shops:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                    elif shops == False:

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянного угля <b>{product_brand} {product_name}</b>\n'
                            f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'), parse_mode='HTML')
                else:
                    if shops:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                    elif shops == False:

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянного угля <b>{product_brand} {product_name}</b>\n'
                            f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f':pensive: Ошибка при работе с Базой Данных'
                            f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                            f'Кальянный уголь <b>{product_brand} {product_name}</b>\n'
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'), parse_mode='HTML')

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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















# Кальянный табак, Пользователь выбрал бренд
@dp.callback_query_handler(lambda callback_query: 'shop_brand_hookah_tobacco_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_brand_hookah_tobacco_')[1]
                brand_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])

                products_name_and_price = get_requests.shop_hookah_tobacco_name_and_price_by_brand_id(brand_id,shop_id)
                if products_name_and_price:
                    markup_products_name_and_price = types.InlineKeyboardMarkup()
                    for product_name_and_price in products_name_and_price:
                        product_item_id = product_name_and_price[0]
                        product_brand = product_name_and_price[1]
                        product_name = product_name_and_price[2]
                        product_price = product_name_and_price[3]
                        markup_products_name_and_price.add(types.InlineKeyboardButton(text=f'{product_brand} {product_name}, Цена: {product_price}',
                                                                                           callback_data=f"shop_model_hookah_tobacco_{product_item_id}_{shop_id}"))
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите модель, которая вас интересует:', language='alias'),
                                           reply_markup=markup_products_name_and_price)
                elif not products_name_and_price:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данного бренда нет товара', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный табак, Пользователь выбрал модель в соответствии с брендом выбранным до этого
# Кальянный табак, Просмотр характеристики
@dp.callback_query_handler(lambda callback_query: 'shop_model_hookah_tobacco_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                full_info = callback_query.data.split('shop_model_hookah_tobacco_')[1]
                item_id = int(full_info.split('_')[0])
                shop_id = int(full_info.split('_')[1])


                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                all_taste = get_requests.check_taste_hookah_tobacco_in_shop(item_id,shop_id)
                if all_taste:
                    characteristic_product = get_requests.check_characteristic_hookah_tobacco(item_id)
                    if characteristic_product:
                        item_size = characteristic_product[2]
                        price = characteristic_product[3]
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"htob_c_shop_{item_id}_{taste}_{shop_id}"))
                                                            # callback_data = check_availability_hookah_tobacco
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Объем : {item_size} г.\n'
                            f'Цена: {price}', language='alias'),parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    elif characteristic_product == False:
                        markup_products_name_and_price = types.InlineKeyboardMarkup()
                        for taste in all_taste:
                            item_id = taste[0]
                            taste = taste[1]
                            markup_products_name_and_price.add(
                                types.InlineKeyboardButton(text=f'{taste}',
                                                           callback_data=f"htob_c_shop_{item_id}_{taste}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Характеристика <b>{product_brand} {product_name}</b> :\n\n'
                            f'Информация отсутствует', language='alias'))
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            f'Выберите вкус, у модели {product_brand} {product_name}:', language='alias'),
                                               reply_markup=markup_products_name_and_price)
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif all_taste == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У данной модели нет вкусов', language='alias'))
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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


# Кальянный табак, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'htob_c_shop_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('htob_c_shop_')[1]
                item_id = int(model_full.split('_')[0])
                taste = model_full.split('_')[1]
                shop_id = model_full.split('_')[2]

                shops = get_requests.is_hookah_tobacco_in_shop(item_id,taste,shop_id)
                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Кальянный табак <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Кальянный табак <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Кальянный табак <b>{product_brand} {product_name}</b> со вкусом {taste}\n'
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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





# Электронные устройства, Пользователю показываются магазины
@dp.callback_query_handler(lambda callback_query: 'shop_edevice_c_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_buyer = get_requests.check_user_is_buyer(user_id)
            if user_is_buyer:

                model_full = callback_query.data.split('shop_edevice_c_')[1]
                item_id = int(model_full.split('_')[0])
                shop_id = int(model_full.split('_')[1])

                shops = get_requests.is_electronic_devices_in_shop(item_id, shop_id)
                shops_info = get_requests.get_shop_by_id(shop_id)
                shop_city = shops_info[1]
                shop_street = shops_info[2]
                shop_house = shops_info[3]

                product = get_requests.get_product_brand_and_name(item_id)
                product_brand = product[0]
                product_name = product[1]

                if shops:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Электронное устройство <b>{product_brand} {product_name}</b>\n'
                        f'<b>В наличии</b>', language='alias'), parse_mode='HTML')
                elif shops == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Электронного устройства <b>{product_brand} {product_name}</b>\n'
                        f'<b>Нет в наличии</b>', language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'В магазине по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        f'Электронное устройство <b>{product_brand} {product_name}</b>\n'
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_buyer == False:
                await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                    ':pensive: Вы не являетесь покупателем, обратитесь к администратору', language='alias'))
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

