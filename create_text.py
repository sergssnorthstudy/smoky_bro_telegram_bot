

def create_view_categories(categories:list) -> str:
    finish_string = ""
    for catergory in categories:
        catergory_id = catergory[0]
        catergory_name = catergory[1]
        finish_string += f"{catergory_id}. {catergory_name}\n"
    return finish_string


def create_view_brands(brands:list) -> str:
    finish_string = ""
    for brand in brands:
        brand_id = brand[0]
        brand_name = brand[1]
        finish_string += f"ID Бренда: {brand_id}  {brand_name}\n"
    return finish_string


def create_view_shops(shops:list) -> str:
    finish_string = ""
    for shop in shops:
        shop_id = shop[0]
        shop_city = shop[1]
        shop_street = shop[2]
        shop_house = shop[3]
        finish_string += f"Магазин №{shop_id}  Адрес: ул. {shop_street}, д.{shop_house}, г.{shop_city}\n"
    return finish_string


def create_view_сharging_types(сharging_types:list) -> str:
    finish_string = ""
    for сharging_type in сharging_types:
        сharging_type_id = сharging_type[0]
        сharging_type_name = сharging_type[1]
        finish_string += f"ID Типа зарядки: {сharging_type_id} Название {сharging_type_name}\n"
    return finish_string


def create_view_size_charcoal(size_charcoals:list) -> str:
    finish_string = ""
    for size_charcoal in size_charcoals:
        size_charcoal_id = size_charcoal[0]
        size_charcoal_name = size_charcoal[1]
        finish_string += f"ID Типа размера: {size_charcoal_id} Название {size_charcoal_name}\n"
    return finish_string


def create_view_products_with_category(products:list) -> str:
    finish_string = ""
    for product in products:
        product_id = product[0]
        product_category = product[1]
        product_brand = product[2]
        product_name = product[3]
        product_price = product[4]
        finish_string += f"<b>ID Товара: {product_id}</b>, Категория:  {product_category}," \
                         f" Бренд:  {product_brand}, Название:  {product_name}, Цена:  {product_price}\n"
    return finish_string
