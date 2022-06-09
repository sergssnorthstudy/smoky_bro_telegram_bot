from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton , InlineKeyboardButton
import emoji

add_information = InlineKeyboardMarkup()
kb_add_brand = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::ab:    Добавить брэнд', language='alias'),
                                     callback_data='add_brand')
kb_add_products = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::bookmark_tabs:    Добавить товар', language='alias'),
                                     callback_data='add_products')
kb_add_products_in_shop = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::house:     Добавить товар в магазин', language='alias'),
                                       callback_data='add_products_in_shop')
kb_add_category = InlineKeyboardButton(text=emoji.emojize(':heavy_plus_sign::1234:    Добавить брэнд', language='alias'),
                                     callback_data='add_category')
add_information.add(kb_add_products)
add_information.add(kb_add_products_in_shop)