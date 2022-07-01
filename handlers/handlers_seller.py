import logging
from aiogram import Bot, Dispatcher, executor, types
import emoji

from datetime import datetime
from main import dp
from main import bot
import requests_database.get_requests as get_requests
import requests_database.post_requests as post_requests
from decimal import Decimal


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Main button, ПРОДАЖА
@dp.message_handler(content_types=['text'], text=emoji.emojize(':heavy_dollar_sign:    Продажа', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = get_requests.check_shop_id_by_user(user_id)
                if shop_id:
                    is_user_have_receipts = get_requests.is_user_have_receipts(user_id)
                    if is_user_have_receipts:
                        is_user_have_open_receipt = get_requests.is_user_have_open_receipt(user_id)
                        if is_user_have_open_receipt:
                            open_receipt_id = get_requests.check_open_receipt_id(user_id)
                            all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)

                            markup_actions = types.InlineKeyboardMarkup()
                            markup_actions.add(types.InlineKeyboardButton(
                                text=emoji.emojize(':heavy_plus_sign:   Продолжить заполнять чек', language='alias'),
                                callback_data=f"continue_a_receipt"))
                            markup_actions.add(types.InlineKeyboardButton(
                                text=emoji.emojize(':heavy_minus_sign:   Удалить позицию', language='alias'),
                                callback_data=f"delete_position_in_receipt"))
                            markup_actions.add(types.InlineKeyboardButton(
                                text=emoji.emojize(':white_check_mark:   Закрыть чек', language='alias'),
                                callback_data=f"close_a_receipt"))


                            if all_items_in_receipt:
                                finish_string = f'Текущий открытый чек:\n\n'
                                counter = 0
                                finish_price = Decimal(0)
                                for item_in_recept in all_items_in_receipt:
                                    counter += 1
                                    item_id = item_in_recept[0]
                                    item_id_in_shop = item_in_recept[1]
                                    brand_name = item_in_recept[2]
                                    item_name = item_in_recept[3]
                                    item_count = item_in_recept[4]
                                    item_price = Decimal(item_in_recept[5]) * item_count
                                    finish_price += item_price
                                    finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                     f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                await bot.send_message(message.from_user.id, text='Выберите действие:',
                                                       parse_mode='HTML', reply_markup=markup_actions)
                                await bot.send_message(message.from_user.id, text=finish_string,
                                                       parse_mode='HTML')

                            elif all_items_in_receipt == False:
                                finish_string = f'Текущий открытый чек:\n <b>Пуст</b>'
                                await bot.send_message(message.from_user.id, text='Выберите действие:',
                                                       parse_mode='HTML', reply_markup=markup_actions)
                                await bot.send_message(message.from_user.id, text=finish_string,
                                                       parse_mode='HTML')
                            else:
                                await bot.send_message(message.from_user.id, text='Выберите действие:',
                                                       parse_mode='HTML', reply_markup=markup_actions)
                                await bot.send_message(message.from_user.id, text=emoji.emojize(
                                    ':pensive: Ошибка при работе с Базой Данных\n'
                                    'Мы не можем получить открытый чек', language='alias'),
                                                       parse_mode='HTML')

                        elif is_user_have_open_receipt == False:

                            markup_actions = types.InlineKeyboardMarkup()
                            markup_actions.add(types.InlineKeyboardButton(
                                text=emoji.emojize(':heavy_plus_sign: Создать чек', language='alias'),
                                callback_data=f"open_a_receipt"))
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                'Выберите действие:', language='alias'), reply_markup=markup_actions)

                    elif is_user_have_receipts == False:

                        markup_actions = types.InlineKeyboardMarkup()
                        markup_actions.add(types.InlineKeyboardButton(
                            text=emoji.emojize(':heavy_plus_sign: Открыть чек', language='alias'),
                            callback_data=f"open_a_receipt"))
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            'Выберите действие:', language='alias'), reply_markup=markup_actions)

                    else:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))

                elif shop_id == False:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                                                   callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных\n'
                        'Мы не можем определить магазин в котором вы работаете', language='alias'), parse_mode='HTML')

            elif user_is_seller == False:
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


# Создание чека
@dp.callback_query_handler(lambda callback_query: 'open_a_receipt' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = get_requests.check_shop_id_by_user(user_id)
                if shop_id:
                    open_receipt_id = get_requests.check_open_receipt_id(user_id)
                    if open_receipt_id:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'У вас уже есть открытый чек, вы не можете создать еще', language='alias'))
                    elif open_receipt_id == False:
                        receipt_created = post_requests.create_receipt(user_id, shop_id)
                        if receipt_created:
                            markup_categories = types.InlineKeyboardMarkup(row_width=2)
                            all_categories = get_requests.get_all_categories()
                            for categories in all_categories:
                                categories_id = categories[0]
                                categories_name = categories[1]
                                markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                                 callback_data=f"products_category_{categories_id}_{shop_id}"))
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Выберите категорию, которая вас интересует:', language='alias'),
                                                   reply_markup=markup_categories, )
                        else:
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных\n'
                                'Мы не можем cоздать чек', language='alias'),
                                                   parse_mode='HTML')
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем проверить существуют ли открытые чеки или нет', language='alias'),
                                               parse_mode='HTML')

                elif shop_id == False:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                                                   callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных\n'
                        'Мы не можем определить магазин в котором вы работаете', language='alias'), parse_mode='HTML')
            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'buy_disp_' in callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                model_full = callback_query.data.split('buy_disp_')[1]
                shop_id = get_requests.check_shop_id_by_user(user_id)
                item_id_in_shop = int(model_full.split('_')[0])
                item_id = int(model_full.split('_')[1])
                item_count = int(model_full.split('_')[2])

                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    sales_added = post_requests.add_sale(item_id, item_id_in_shop, item_count, user_id, shop_id,
                                                         open_receipt_id)
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    markup_actions = types.InlineKeyboardMarkup()
                    markup_actions.add(types.InlineKeyboardButton(
                        text=emoji.emojize(':heavy_plus_sign:   Продолжить заполнять чек', language='alias'),
                        callback_data=f"continue_a_receipt"))
                    markup_actions.add(types.InlineKeyboardButton(
                        text=emoji.emojize(':heavy_minus_sign:   Удалить позицию', language='alias'),
                        callback_data=f"delete_position_in_receipt"))
                    markup_actions.add(types.InlineKeyboardButton(
                        text=emoji.emojize(':white_check_mark:   Закрыть чек', language='alias'),
                        callback_data=f"close_a_receipt"))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите действие:', language='alias'), reply_markup=markup_actions)

                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        finish_string = f'Текущий открытый чек:\n\n'
                        counter = 0
                        finish_price = Decimal(0)
                        for item_in_recept in all_items_in_receipt:
                            counter += 1
                            item_id = item_in_recept[0]
                            item_id_in_shop = item_in_recept[1]
                            brand_name = item_in_recept[2]
                            item_name = item_in_recept[3]
                            item_count = item_in_recept[4]
                            item_price = Decimal(item_in_recept[5]) * item_count
                            finish_price += item_price
                            finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                             f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                        finish_string += f"<b>Итог: {finish_price} руб.</b>"
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                    elif all_items_in_receipt == False:
                        finish_string = f'Текущий открытый чек:\n\nПуст'
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')

                elif open_receipt_id == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'check_a_receipt' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        finish_string = f'Текущий открытый чек:\n\n'
                        counter = 0
                        finish_price = Decimal(0)
                        for item_in_recept in all_items_in_receipt:
                            counter += 1
                            item_id = item_in_recept[0]
                            item_id_in_shop = item_in_recept[1]
                            brand_name = item_in_recept[2]
                            item_name = item_in_recept[3]
                            item_count = item_in_recept[4]
                            item_price = Decimal(item_in_recept[5]) * item_count
                            finish_price += item_price
                            finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                             f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                        finish_string += f"<b>Итог: {finish_price} руб.</b>"
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                    elif all_items_in_receipt == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        finish_string = f'Текущий открытый чек:\n\nПуст'
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                    else:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')

                elif open_receipt_id == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'close_a_receipt' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        markup_actions = types.InlineKeyboardMarkup()
                        markup_actions.add(types.InlineKeyboardButton(text=emoji.emojize(
                            ':heavy_division_sign:  Добавить скидку', language='alias'),
                            callback_data=f"close_a_receipt_with_discount"))
                        markup_actions.add(types.InlineKeyboardButton(text=emoji.emojize(
                            ':white_check_mark:  Закрыть чек', language='alias'),
                            callback_data=f"close_a_receipt_without_discount"))

                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text='Выберите действие:',reply_markup=markup_actions)


                    elif all_items_in_receipt == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':x: Вы не можете закрыть пустой чек', language='alias'),
                                               parse_mode='HTML')
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')

                elif open_receipt_id == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'continue_a_receipt' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = get_requests.check_shop_id_by_user(user_id)
                if shop_id:
                    open_receipt_id = get_requests.check_open_receipt_id(user_id)
                    if open_receipt_id:

                        markup_categories = types.InlineKeyboardMarkup(row_width=2)
                        all_categories = get_requests.get_all_categories()
                        for categories in all_categories:
                            categories_id = categories[0]
                            categories_name = categories[1]
                            markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                             callback_data=f"products_category_{categories_id}_{shop_id}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите категорию, которая вас интересует:', language='alias'),
                                               reply_markup=markup_categories, )

                    elif open_receipt_id == False:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'У вас нет открытых чеков', language='alias'))
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                elif shop_id == False:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(
                            text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                            callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных\n'
                        'Мы не можем определить магазин в котором вы работаете', language='alias'), parse_mode='HTML')

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'close_a_receipt_with_discount' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = get_requests.check_shop_id_by_user(user_id)
                if shop_id:
                    open_receipt_id = get_requests.check_open_receipt_id(user_id)
                    if open_receipt_id:
                        all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                        if all_items_in_receipt:

                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                f'Проверьте чек и напишите мне какая скидка пойдет на текущий чек: \n\n'
                                f'<b>Пример:</b>  "Скидка 5%"', language='alias'),
                                                   parse_mode="HTML")

                            finish_string = f'Текущий открытый чек:\n\n'
                            counter = 0
                            finish_price = Decimal(0)
                            for item_in_recept in all_items_in_receipt:
                                counter += 1
                                item_id = item_in_recept[0]
                                item_id_in_shop = item_in_recept[1]
                                brand_name = item_in_recept[2]
                                item_name = item_in_recept[3]
                                item_count = item_in_recept[4]
                                item_price = Decimal(item_in_recept[5]) * item_count
                                finish_price += item_price
                                finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                            finish_string += f"<b>Итог: {finish_price} руб.</b>"
                            await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                        elif all_items_in_receipt == False:
                            finish_string = f'Текущий открытый чек:\n <b>Пуст</b>'
                            await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                        else:
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных\n'
                                'Мы не можем получить открытый чек', language='alias'),
                                                   parse_mode='HTML')

                    elif open_receipt_id == False:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'У вас нет открытых чеков', language='alias'))
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных', language='alias'))
                elif shop_id == False:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(
                            text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                            callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных\n'
                        'Мы не можем определить магазин в котором вы работаете', language='alias'), parse_mode='HTML')

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'close_a_receipt_without_discount' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        discount = 0
                        date_and_time_close_receipt = datetime.now()
                        close_receipt = post_requests.close_receipt(open_receipt_id, discount,
                                                                    date_and_time_close_receipt)
                        close_sales = post_requests.close_sales(open_receipt_id)
                        if close_receipt and close_sales:
                            await bot.delete_message(chat_id=callback_query.from_user.id,
                                                     message_id=callback_query.message.message_id)
                            await bot.answer_callback_query(callback_query.id)
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                'Поздравляем с продажей\n'
                                'Продолжай в том же духе :smile:', language='alias'),
                                                   parse_mode='HTML')
                        else:
                            await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных\n'
                                'Мы не закрыли чек', language='alias'),
                                                   parse_mode='HTML')
                    elif all_items_in_receipt == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        finish_string = f'Текущий открытый чек:\n\nПуст'
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Мы не можем закрыть пустой чек', language='alias'),
                                               parse_mode='HTML')
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')
                elif open_receipt_id == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.message_handler(lambda message: 'Скидка' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                result = message.text.split('Скидка')
                discount = result[1].strip()
                discount = int(discount.split('%')[0])
                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        date_and_time_close_receipt = datetime.now()
                        close_receipt = post_requests.close_receipt(open_receipt_id,discount,date_and_time_close_receipt)
                        close_sales = post_requests.close_sales(open_receipt_id)
                        if close_receipt and close_sales:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                'Поздравляем с продажей\n'
                                'Продолжай в том же духе :smile:', language='alias'),
                                                   parse_mode='HTML')
                        else:
                            await bot.send_message(message.from_user.id, text=emoji.emojize(
                                ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не закрыли чек', language='alias'),
                                               parse_mode='HTML')
                    elif all_items_in_receipt == False:
                        finish_string = f'Текущий открытый чек:\n\nПуст'
                        await bot.send_message(message.from_user.id, text=finish_string, parse_mode='HTML')
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            'Мы не можем закрыть пустой чек', language='alias'),
                                               parse_mode='HTML')
                    else:
                        await bot.send_message(message.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')
                elif open_receipt_id == False:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'delete_position_in_receipt' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                    if all_items_in_receipt:
                        counter = 0
                        markup_counter = types.InlineKeyboardMarkup()
                        for item_in_receipt in all_items_in_receipt:
                            counter +=1
                            markup_counter.add(
                                types.InlineKeyboardButton(text=f"{counter}",
                                                           callback_data=f"delete_position_receipt_{counter}"))
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Выберите какую позицию вы хотите удалить из чека:', language='alias'),
                                               reply_markup=markup_counter)
                    elif all_items_in_receipt == False:
                        await bot.delete_message(chat_id=callback_query.from_user.id,
                                                 message_id=callback_query.message.message_id)
                        await bot.answer_callback_query(callback_query.id)
                        finish_string = f'Текущий открытый чек:\n\nПуст'
                        await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            'Мы не можем удалять позиции из пустого чек', language='alias'),
                                               parse_mode='HTML')
                    else:
                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                            ':pensive: Ошибка при работе с Базой Данных\n'
                            'Мы не можем получить открытый чек', language='alias'),
                                               parse_mode='HTML')
                elif open_receipt_id == False:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'delete_position_receipt_' in callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                model_full = callback_query.data.split('delete_position_receipt_')[1]
                number_position_for_delete = int(model_full)

                open_receipt_id = get_requests.check_open_receipt_id(user_id)
                if open_receipt_id:
                    all_items_in_receipt = get_requests.check_sales_for_delete_position(open_receipt_id)
                    if all_items_in_receipt:
                        counter = 0
                        for item_in_recept in all_items_in_receipt:
                            counter += 1
                            if counter == number_position_for_delete:
                                sales_id = item_in_recept[0]
                                delete_position_from_receipt = post_requests.delete_position_from_receipt(sales_id)
                                if delete_position_from_receipt:
                                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                                             message_id=callback_query.message.message_id)
                                    markup_actions = types.InlineKeyboardMarkup()
                                    markup_actions.add(types.InlineKeyboardButton(
                                        text=emoji.emojize(':heavy_plus_sign:   Продолжить заполнять чек',
                                                           language='alias'),
                                        callback_data=f"continue_a_receipt"))
                                    markup_actions.add(types.InlineKeyboardButton(
                                        text=emoji.emojize(':heavy_minus_sign:   Удалить позицию', language='alias'),
                                        callback_data=f"delete_position_in_receipt"))
                                    markup_actions.add(types.InlineKeyboardButton(
                                        text=emoji.emojize(':white_check_mark:   Закрыть чек', language='alias'),
                                        callback_data=f"close_a_receipt"))
                                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                        'Выберите действие:', language='alias'), reply_markup=markup_actions)

                                    all_items_in_receipt = get_requests.check_all_sales_item_in_receipt(open_receipt_id)
                                    if all_items_in_receipt:
                                        finish_string = f'Текущий открытый чек:\n\n'
                                        counter = 0
                                        finish_price = Decimal(0)
                                        for item_in_recept in all_items_in_receipt:
                                            counter += 1
                                            item_id = item_in_recept[0]
                                            item_id_in_shop = item_in_recept[1]
                                            brand_name = item_in_recept[2]
                                            item_name = item_in_recept[3]
                                            item_count = item_in_recept[4]
                                            item_price = Decimal(item_in_recept[5]) * item_count
                                            finish_price += item_price
                                            finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                             f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                        finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                        await bot.send_message(callback_query.from_user.id, text=finish_string,
                                                               parse_mode='HTML')
                                    elif all_items_in_receipt == False:
                                        finish_string = f'Текущий открытый чек:\n\nПуст'
                                        await bot.send_message(callback_query.from_user.id, text=finish_string,
                                                               parse_mode='HTML')
                                    else:
                                        await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                            ':pensive: Ошибка при работе с Базой Данных\n'
                                            'Мы не можем получить открытый чек', language='alias'),
                                                               parse_mode='HTML')
                                else:
                                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                                        ':pensive: Ошибка при удалении позиции из чека', language='alias'))

                elif open_receipt_id == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        'У вас нет открытых чеков', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))

            elif user_is_seller == False:
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
# Main button, ПОИСК ТОВАРА
@dp.message_handler(content_types=['text'], text=emoji.emojize(':mag_right:    Поиск товара', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = get_requests.check_shop_id_by_user(user_id)
                if shop_id:
                    shops_info = get_requests.get_shop_by_id(shop_id)
                    shop_city = shops_info[1]
                    shop_street = shops_info[2]
                    shop_house = shops_info[3]

                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        f'Вы работник магазина по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n',
                        language='alias'))
                    markup_categories = types.InlineKeyboardMarkup(row_width=2)
                    all_categories = get_requests.get_all_categories()
                    for categories in all_categories:
                        categories_id = categories[0]
                        categories_name = categories[1]
                        markup_categories.add(types.InlineKeyboardButton(text=categories_name,
                                                                         callback_data=f"products_category_{categories_id}_{shop_id}"))
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'Выберите категорию, которая вас интересует:', language='alias'),
                                           reply_markup=markup_categories, )
                elif shop_id == False:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                                                   callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
            elif user_is_seller == False:
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


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Main button, ИСТОРИЯ ПРОДАЖ
@dp.message_handler(content_types=['text'], text=emoji.emojize(':book:    История продаж', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:

                markup_actions = types.InlineKeyboardMarkup()
                markup_actions.add(types.InlineKeyboardButton(
                    text=emoji.emojize('Сегодня', language='alias'),
                    callback_data=f"history_salles_today"))
                markup_actions.add(types.InlineKeyboardButton(
                    text=emoji.emojize('Выбрать день', language='alias'),
                    callback_data=f"history_salles_another_day"))

                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    'Выберите действие:', language='alias'), reply_markup=markup_actions)

            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'history_salles_today' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                current_date = datetime.now().date()
                check_all_close_receipt = get_requests.check_close_receipts(user_id,current_date)
                if check_all_close_receipt:
                    await bot.answer_callback_query(callback_query.id)
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.send_message(callback_query.from_user.id, text=f'Итог за {current_date} число:', parse_mode='HTML')
                    day_price = Decimal(0)
                    day_count = 0
                    for close_receipt in check_all_close_receipt:
                        receipt_id = close_receipt[0]
                        shop_id = close_receipt[1]
                        employee_id = close_receipt[2]
                        discount = close_receipt[3]
                        date = close_receipt[5]
                        check_all_close_sales = get_requests.check_close_sales(user_id,receipt_id)
                        if discount == 0:
                            if check_all_close_sales:
                                counter = 0
                                finish_string = f'Чек: Id {receipt_id}\n\n'
                                finish_price = Decimal(0)
                                for close_sales in check_all_close_sales:
                                    counter +=1
                                    item_id = close_sales[0]
                                    item_id_in_shop = close_sales[1]
                                    brand_name = close_sales[2]
                                    item_name = close_sales[3]
                                    item_count = close_sales[4]
                                    item_price = Decimal(close_sales[5]) * item_count
                                    finish_price += item_price
                                    day_count += item_count

                                    finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                     f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                day_price += finish_price
                                finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                await bot.send_message(callback_query.from_user.id, text=finish_string, parse_mode='HTML')
                        elif discount != 0:
                            if check_all_close_sales:
                                counter = 0
                                finish_string = f'Чек: Id {receipt_id}\n' \
                                                f'Скидка: {discount}%\n\n'
                                finish_price = Decimal(0)
                                for close_sales in check_all_close_sales:
                                    counter += 1
                                    item_id = close_sales[0]
                                    item_id_in_shop = close_sales[1]
                                    brand_name = close_sales[2]
                                    item_name = close_sales[3]
                                    item_count = close_sales[4]
                                    item_price = Decimal(close_sales[5]) * item_count
                                    finish_price += item_price
                                    day_count += item_count
                                    finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                     f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                discount_for_price = Decimal(1) - (discount/Decimal(100))
                                finish_price = finish_price * discount_for_price
                                day_price += finish_price
                                finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                await bot.send_message(callback_query.from_user.id, text=finish_string,
                                                       parse_mode='HTML')
                    await bot.send_message(callback_query.from_user.id, text=f'Итог за день: \n\n'
                                                                             f'Кол-во продаж: {day_count} шт.\n'
                                                                             f'Сумма продаж: {day_price} руб.',
                                           parse_mode='HTML')
                elif check_all_close_receipt == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':x: Сегодня у вас нет продаж', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
            elif user_is_seller == False:
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


@dp.callback_query_handler(lambda callback_query: 'history_salles_another_day' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                current_date = datetime.now().date()
                check_all_close_receipt = get_requests.check_close_receipts(user_id,current_date)
                if check_all_close_receipt:

                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Напишите мне о каком дне вы хотели бы получить информацию\n'
                        f'Структура дня такая:(Год)-(Месяц),(День)\n\n'
                        f'<b>Пример:</b>  "История продаж: 2022-07-01"', language='alias'),
                                           parse_mode="HTML")
                elif check_all_close_receipt == False:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':x: Сегодня у вас нет продаж', language='alias'))
                else:
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))
            elif user_is_seller == False:
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


@dp.message_handler(lambda message: 'История продаж: ' in message.text)
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                result = message.text.split('История продаж:')
                date = result[1].strip()
                try:
                    necessary_date = datetime.strptime(date, "%Y-%m-%d").date()
                except ValueError as ex:
                    await bot.send_message(message.from_user.id, text=f'Вы указали дату в неверном формате',
                                           parse_mode='HTML')
                check_all_close_receipt = get_requests.check_close_receipts(user_id, necessary_date)
                if check_all_close_receipt:
                    await bot.send_message(message.from_user.id, text=f'Итог за {necessary_date} число:',
                                           parse_mode='HTML')
                    day_price = Decimal(0)
                    day_count = 0
                    for close_receipt in check_all_close_receipt:
                        receipt_id = close_receipt[0]
                        shop_id = close_receipt[1]
                        employee_id = close_receipt[2]
                        discount = close_receipt[3]
                        date = close_receipt[5]
                        check_all_close_sales = get_requests.check_close_sales(user_id, receipt_id)
                        if discount == 0:
                            if check_all_close_sales:
                                counter = 0
                                finish_string = f'Чек: Id {receipt_id}\n\n'
                                finish_price = Decimal(0)
                                for close_sales in check_all_close_sales:
                                    counter += 1
                                    item_id = close_sales[0]
                                    item_id_in_shop = close_sales[1]
                                    brand_name = close_sales[2]
                                    item_name = close_sales[3]
                                    item_count = close_sales[4]
                                    item_price = Decimal(close_sales[5]) * item_count
                                    finish_price += item_price
                                    day_count += item_count

                                    finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                     f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                day_price += finish_price
                                finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                await bot.send_message(message.from_user.id, text=finish_string,
                                                       parse_mode='HTML')
                        elif discount != 0:
                            if check_all_close_sales:
                                counter = 0
                                finish_string = f'Чек: Id {receipt_id}\n' \
                                                f'Скидка: {discount}%\n\n'
                                finish_price = Decimal(0)
                                for close_sales in check_all_close_sales:
                                    counter += 1
                                    item_id = close_sales[0]
                                    item_id_in_shop = close_sales[1]
                                    brand_name = close_sales[2]
                                    item_name = close_sales[3]
                                    item_count = close_sales[4]
                                    item_price = Decimal(close_sales[5]) * item_count
                                    finish_price += item_price
                                    day_count += item_count
                                    finish_string += f"<b>{counter})</b> <b>{brand_name} {item_name}</b>   {item_price} руб.  {item_count} шт.\n" \
                                                     f"Продукт: ID {item_id}, ID в магазине {item_id_in_shop}\n\n"
                                discount_for_price = Decimal(1) - (discount / Decimal(100))
                                finish_price = finish_price * discount_for_price
                                day_price += finish_price
                                finish_string += f"<b>Итог: {finish_price} руб.</b>"
                                await bot.send_message(message.from_user.id, text=finish_string,
                                                       parse_mode='HTML')
                    await bot.send_message(message.from_user.id, text=f'Итог за день: \n\n'
                                                                             f'Кол-во продаж: {day_count} шт.\n'
                                                                             f'Сумма продаж: {day_price} руб.',
                                           parse_mode='HTML')
                elif check_all_close_receipt == False:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':x: Сегодня у вас нет продаж', language='alias'))
                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_seller == False:
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
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
# Main button, ВЫБРАТЬ МАГАЗИН
@dp.message_handler(content_types=['text'], text=emoji.emojize(':house:    Выбрать магазин', language='alias'))
async def timetable(message: types.Message):
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:

                shop_id = get_requests.check_shop_id_by_user(user_id)

                if shop_id:
                    shops_info = get_requests.get_shop_by_id(shop_id)
                    shop_city = shops_info[1]
                    shop_street = shops_info[2]
                    shop_house = shops_info[3]

                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        f'Вы работник магазина по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n'
                        'Если вы сегодня работаете в другом магазине, вам следует выбрать магазин из представленных ниже',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                                                   callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)
                elif shop_id == False:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        f'Вы не выбрали адрес магазина в котором работаете\n'
                        'Выберите магазин в котором будете работать сегодня',
                        language='alias'))
                    all_shops = get_requests.all_shops()
                    markup_shops = types.InlineKeyboardMarkup()
                    for shop in all_shops:
                        shop_id = shop[0]
                        shop_city = shop[1]
                        shop_street = shop[2]
                        shop_house = shop[3]
                        markup_shops.add(
                            types.InlineKeyboardButton(text=f"ул.{shop_street}, д.{shop_house}, г.{shop_city}\n",
                                                       callback_data=f"seller_select_shop_{shop_id}"))
                    markup_shops.add(
                        types.InlineKeyboardButton(text=emoji.emojize(':arrow_left: Отменить выбор', language='alias'),
                                                   callback_data=f"cancel_seller_select_shop"))
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        'Выберите адрес магазина, в котором вы сегодня работаете:', language='alias'),
                                           reply_markup=markup_shops)

                else:
                    await bot.send_message(message.from_user.id, text=emoji.emojize(
                        ':pensive: Ошибка при работе с Базой Данных', language='alias'))


            elif user_is_seller == False:
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


# Отмена выбора магазина
@dp.callback_query_handler(lambda callback_query: 'cancel_seller_select_shop' == callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                await bot.delete_message(chat_id=callback_query.from_user.id,
                                         message_id=callback_query.message.message_id)
                await bot.answer_callback_query(callback_query.id)
            elif user_is_seller == False:
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


# Cохраняет магазин для работника
@dp.callback_query_handler(lambda callback_query: 'seller_select_shop_' in callback_query.data)
async def timetable(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)
    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_is_seller = get_requests.check_user_is_seller(user_id)
            if user_is_seller:
                shop_id = int(callback_query.data.split('seller_select_shop_')[1])

                update_shop_id_by_user = post_requests.update_shop_id_by_user(user_id, shop_id)
                if update_shop_id_by_user:

                    shops_info = get_requests.get_shop_by_id(shop_id)
                    shop_city = shops_info[1]
                    shop_street = shops_info[2]
                    shop_house = shops_info[3]

                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Вы успешно обновили информацию о магазине в котором вы работаете\n'
                        f'Теперь вы числитесь работником магазина по адресу: ул. {shop_street}, д.{shop_house}, г.{shop_city}',
                        language='alias'), parse_mode='HTML')
                else:
                    await bot.delete_message(chat_id=callback_query.from_user.id,
                                             message_id=callback_query.message.message_id)
                    await bot.answer_callback_query(callback_query.id)
                    await bot.send_message(callback_query.from_user.id, text=emoji.emojize(
                        f'Произошла ошибка при попытке обновить информацию о магазине в котором вы работаете\n',
                        language='alias'), parse_mode='HTML')

            elif user_is_seller == False:
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
