import logging
import string
from aiogram import Bot, Dispatcher, executor, types
import emoji
import asyncio
import requests_database.get_requests as get_requests
import requests_database.post_requests as post_requests

#Тут меняес API TOKEN
API_TOKEN = '5554060477:AAF1S1mymxmuaaj0gi-oV5K9Kv-P5FaAJsk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):

    #Keyboard seller
    keyboard_seller = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_sale = types.KeyboardButton(
        text=emoji.emojize(':heavy_dollar_sign:    Продажа', language='alias'))
    kb_search = types.KeyboardButton(text=emoji.emojize(':mag_right:    Поиск товара', language='alias'))
    kb_history = types.KeyboardButton(
        text=emoji.emojize(':book:    История продаж', language='alias'))
    keyboard_seller.add(kb_sale)
    keyboard_seller.add(kb_search)
    keyboard_seller.add(kb_history)
    # Keyboard buyer
    keyboard_buyer = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_items = types.KeyboardButton(
        text=emoji.emojize(':mag_right:    Товар', language='alias'))
    kb_shops = types.KeyboardButton(text=emoji.emojize(':house:    Магазины', language='alias'))
    keyboard_buyer.add(kb_items)
    keyboard_buyer.add(kb_shops)
    # Keyboard admin
    keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_statistics = types.KeyboardButton(
        text=emoji.emojize(':bar_chart:    Получить статистику', language='alias'))
    kb_edit_product = types.KeyboardButton(text=emoji.emojize(':arrows_clockwise:    Изменить кол-во товара', language='alias'))
    kb_add_product = types.KeyboardButton(text=emoji.emojize(':heavy_plus_sign:    Добавить новый товар', language='alias'))
    keyboard_admin.add(kb_statistics)
    keyboard_admin.add(kb_edit_product)
    keyboard_admin.add(kb_add_product)


    #Start authorization
    user_id = message.from_user.id
    is_incomplete_user = get_requests.is_incomplete_user(user_id)

    if is_incomplete_user:
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_roles = list()
            all_user_role = get_requests.check_user_roles(user_id)
            if all_user_role is not None:
                for all_user_role in all_user_role:
                    user_roles.append(all_user_role)
                if len(user_roles) == 1:
                    role = user_roles[0][1]
                    if role == 'Покупатель':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize('Выберите категорию, которая вас интересует :point_down:',
                                                                  language='alias'), reply_markup=keyboard_buyer)
                    elif role == 'Продавец':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize('Выберите категорию, которая вас интересует :point_down:',
                                                                  language='alias'), reply_markup=keyboard_seller)
                    elif role == 'Админ':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize('Выберите категорию, которая вас интересует :point_down:',
                                                                  language='alias'), reply_markup=keyboard_admin)
                if len(user_roles) > 1:
                    roles = list()
                    for user_role in user_roles:
                        roles.append(user_role[1])
                    markup = types.InlineKeyboardMarkup()
                    if 'Покупатель' in roles:
                        markup.add(types.InlineKeyboardButton(text='Покупатель',
                                                              callback_data=f"user_role_buyer"))
                    if 'Продавец' in roles:
                        markup.add(types.InlineKeyboardButton(text='Продавец',
                                                                  callback_data=f"user_role_seller"))
                    if 'Админ' in roles:
                        markup.add(types.InlineKeyboardButton(text='Админ',
                                                              callback_data=f"user_role_admin"))
                    await bot.send_message(message.from_user.id, text='У вас несколько ролей, пожалуйста выберите одну:',
                                           reply_markup=markup)
            elif all_user_role == None:
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Скорее всего у вас не привязан номер телефона', language='alias'))
                keyboard_phone = types.ReplyKeyboardMarkup(True, True)
                kb_add_phone = types.KeyboardButton(text=emoji.emojize('Отправить номер телефона',
                                                                       language='alias'), request_contact=True)
                keyboard_phone.add(kb_add_phone)
                await bot.send_message(message.from_user.id, text=emoji.emojize(':telephone_receiver: Чтобы '
                                                                                'взаимодействовать со мной '
                                                                                'вам необходимо указать свой'
                                                                                ' номер телефона.',
                                                                                language='alias'),
                                       reply_markup=keyboard_phone)
            elif all_user_role == "exception":
                await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
        elif not is_complete_user:
            keyboard_phone = types.ReplyKeyboardMarkup(True, True)
            kb_add_phone = types.KeyboardButton(text=emoji.emojize('Отправить номер телефона',
                                                                   language='alias'), request_contact=True)
            keyboard_phone.add(kb_add_phone)
            await bot.send_message(message.from_user.id, text=emoji.emojize(':telephone_receiver: Чтобы '
                                                                            'взаимодействовать со мной '
                                                                            'вам необходимо указать свой'
                                                                            ' номер телефона.',
                                                                            language='alias'),
                                   reply_markup=keyboard_phone)
        else:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Error when working with the database', language='alias'))
    elif is_incomplete_user == False:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            '<b>Приветствую Вас!</b> :wave:\n Я виртуальный ассистент вейп-шопа Smoky Bro и я надеюсь, что мы подружимся\n'
            'Я помогу Вам получить максимально актуальную информацию о наличии товара в наших магазинах\n'
            'Сделайте Ваш выбор в меню ниже :arrow_down:', language='alias'))
        us_name = message.from_user.first_name
        us_sname = message.from_user.last_name
        user_link = message.from_user.username
        post_requests.record_incomplete_user(user_id=user_id, user_name=us_name, user_surname=us_sname, link=user_link)
        is_complete_user = get_requests.is_complete_user(user_id)
        if is_complete_user:
            user_roles = list()
            all_user_role = get_requests.check_user_roles(user_id)
            if all_user_role is not None:
                for all_user_role in all_user_role:
                    user_roles.append(all_user_role)
                if len(user_roles) == 1:
                    role = user_roles[0][1]
                    if role == 'Покупатель':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize(
                                                   'Выберите категорию, которая вас интересует :point_down:',
                                                   language='alias'), reply_markup=keyboard_buyer)
                    elif role == 'Продавец':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize(
                                                   'Выберите категорию, которая вас интересует :point_down:',
                                                   language='alias'), reply_markup=keyboard_seller)
                    elif role == 'Админ':
                        await bot.send_message(message.from_user.id,
                                               text=emoji.emojize(
                                                   'Выберите категорию, которая вас интересует :point_down:',
                                                   language='alias'), reply_markup=keyboard_admin)
                if len(user_roles) > 1:
                    roles = list()
                    for user_role in user_roles:
                        roles.append(user_role[1])
                    await bot.send_message(message.from_user.id,
                                           text=emoji.emojize('У вас несколько ролей, пожалуйста выберите одну:',
                                                              language='alias'))
                    markup = types.InlineKeyboardMarkup()
                    if 'Покупатель' in roles:
                        markup.add(types.InlineKeyboardButton(text='Покупатель',
                                                              callback_data=f"user_role_buyer"))
                    elif 'Продавец' in roles:
                        markup.add(types.InlineKeyboardButton(text='Продавец',
                                                              callback_data=f"user_role_seller"))
                    elif 'Админ' in roles:
                        markup.add(types.InlineKeyboardButton(text='Админ',
                                                              callback_data=f"user_role_admin"))
                    await bot.send_message(message.from_user.id,
                                           text='У вас несколько ролей, пожалуйста выберите одну:',
                                           reply_markup=markup)
        elif is_complete_user == False:
            keyboard_phone = types.ReplyKeyboardMarkup(True, True)
            kb_add_phone = types.KeyboardButton(text=emoji.emojize('Отправить номер телефона',
                                                                   language='alias'), request_contact=True)
            keyboard_phone.add(kb_add_phone)
            await bot.send_message(message.from_user.id, text=emoji.emojize(':telephone_receiver: Чтобы '
                                                                            'взаимодействовать со мной '
                                                                            'вам необходимо указать свой'
                                                                            ' номер телефона.',
                                                                            language='alias'),
                                   reply_markup=keyboard_phone)
        else:
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                    ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    else:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':pensive: Ошибка при работе с Базой Данных', language='alias'))


@dp.message_handler(content_types=['contact'])
async def contact(message):
    if message.contact is not None:
        try:
            post_requests.record_user_phone(message.from_user.id, message.contact.phone_number)
            post_requests.record_user_role_buyer(message.from_user.id)
            await bot.send_message(message.from_user.id, text=emoji.emojize(':white_check_mark: '
                                                                            'Мы успешно привязали ваш телефон к вашему аккаунту',
                                                                            language='alias'))

        except Exception as ex:
            print(ex)
            await bot.send_message(message.from_user.id, text=emoji.emojize(
                ':pensive: Ошибка при работе с Базой Данных', language='alias'))
    else:
        await bot.send_message(message.from_user.id, text=emoji.emojize(
            ':x: Номер телефона не привязан к вашей учетной записи', language='alias'))


@dp.callback_query_handler(lambda callback_query: 'user_role_' in callback_query.data)
async def some_callback_handler(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    callback = callback_query.data.split('user_role_')

    # Keyboard seller
    keyboard_seller = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_sale = types.KeyboardButton(
        text=emoji.emojize(':heavy_dollar_sign:    Продажа', language='alias'))
    kb_search = types.KeyboardButton(text=emoji.emojize(':mag_right:    Поиск товара', language='alias'))
    kb_history = types.KeyboardButton(
        text=emoji.emojize(':book:    История продаж', language='alias'))
    keyboard_seller.add(kb_sale)
    keyboard_seller.add(kb_search)
    keyboard_seller.add(kb_history)
    # Keyboard buyer
    keyboard_buyer = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_items = types.KeyboardButton(
        text=emoji.emojize(':mag_right:    Товар', language='alias'))
    kb_shops = types.KeyboardButton(text=emoji.emojize(':house:    Магазины', language='alias'))
    keyboard_buyer.add(kb_items)
    keyboard_buyer.add(kb_shops)
    # Keyboard admin
    keyboard_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb_statistics = types.KeyboardButton(
        text=emoji.emojize(':bar_chart:    Получить статистику', language='alias'))
    kb_edit_product = types.KeyboardButton(
        text=emoji.emojize(':arrows_clockwise:    Изменить кол-во товара', language='alias'))
    kb_add_product = types.KeyboardButton(
        text=emoji.emojize(':heavy_plus_sign:    Добавить новый товар', language='alias'))
    keyboard_admin.add(kb_statistics)
    keyboard_admin.add(kb_edit_product)
    keyboard_admin.add(kb_add_product)

    role = callback[1]
    if role == 'buyer':
        await bot.send_message(callback_query.from_user.id,
                               text=emoji.emojize(
                                   'Выберите категорию, которая вас интересует :point_down:',
                                   language='alias'), reply_markup=keyboard_buyer)
    elif role == 'seller':
        await bot.send_message(callback_query.from_user.id,
                               text=emoji.emojize(
                                   'Выберите категорию, которая вас интересует :point_down:',
                                   language='alias'), reply_markup=keyboard_seller)
    elif role == 'admin':
        await bot.send_message(callback_query.from_user.id,
                               text=emoji.emojize(
                                   'Выберите категорию, которая вас интересует :point_down:',
                                   language='alias'), reply_markup=keyboard_admin)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)