from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
import emoji

# Главная клавиатура админа
from requests_database import get_requests

keyboard_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_statistics = KeyboardButton(
    text=emoji.emojize(':bar_chart:    Получить статистику', language='alias'))
kb_edit_product = KeyboardButton(
    text=emoji.emojize(':arrows_clockwise:    Изменить кол-во товара', language='alias'))
kb_add_product = KeyboardButton(text=emoji.emojize(':heavy_plus_sign:    Добавить информацию', language='alias'))
keyboard_admin.add(kb_statistics)
keyboard_admin.add(kb_edit_product)
keyboard_admin.add(kb_add_product)

# Главная клавиатура продавца
keyboard_seller = ReplyKeyboardMarkup(resize_keyboard=True)
kb_sale = KeyboardButton(text=emoji.emojize(':heavy_dollar_sign:    Продажа', language='alias'))
kb_search = KeyboardButton(text=emoji.emojize(':mag_right:    Поиск товара', language='alias'))
kb_history = KeyboardButton(text=emoji.emojize(':book:    История продаж', language='alias'))
kb_shop = KeyboardButton(text=emoji.emojize(':house:    Выбрать магазин', language='alias'))
keyboard_seller.add(kb_sale)
keyboard_seller.add(kb_search)
keyboard_seller.add(kb_history)
keyboard_seller.add(kb_shop)

# Главная клавиатура покупателя
keyboard_buyer = ReplyKeyboardMarkup(resize_keyboard=True)
kb_items = KeyboardButton(text=emoji.emojize(':mag_right:    Товары', language='alias'))
kb_shops = KeyboardButton(text=emoji.emojize(':house:    Магазины', language='alias'))
keyboard_buyer.add(kb_items)
keyboard_buyer.add(kb_shops)

