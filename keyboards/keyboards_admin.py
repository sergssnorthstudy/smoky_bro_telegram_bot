from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton
import emoji

add_information = InlineKeyboardMarkup()
kb_add_brand = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::ab:    Добавить брэнд', language='alias'),
                                     callback_data='add_brand')
kb_add_products = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::bookmark_tabs:    Добавить товар', language='alias'),
                                     callback_data='add_products')
kb_add_products_in_shop = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::house:     Добавить товары в магазин', language='alias'),
                                       callback_data='add_products_in_shop')

add_information.add(kb_add_brand)
add_information.add(kb_add_products)
add_information.add(kb_add_products_in_shop)

# Клавиатура категорий и брендов
keyboard_categories_and_brands = InlineKeyboardMarkup(resize_keyboard=True)
kb_categories = InlineKeyboardButton(text=emoji.emojize('Все категории товаров', language='alias'),callback_data='all_categories_for_admin')
kb_brands = InlineKeyboardButton(text=emoji.emojize('Все брэнды', language='alias'),callback_data='all_brands_for_admin')
keyboard_categories_and_brands.add(kb_categories)
keyboard_categories_and_brands.add(kb_brands)


