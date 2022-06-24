

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


def create_view_disposable_cigarettes(disposable_cigarettes:list) -> str:
    finish_string = "<b>Одноразовые сигареты</b>\n"
    for disposable_cigarette in disposable_cigarettes:

        item_id_in_shop = disposable_cigarette[0]
        item_id = disposable_cigarette[1]
        brand_name = disposable_cigarette[2]
        item_name = disposable_cigarette[3]
        item_taste = disposable_cigarette[4]
        item_count_traction = disposable_cigarette[5]
        item_charging_type = disposable_cigarette[6]
        item_count = disposable_cigarette[7]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Вкус: <i>{item_taste}</i>, Кол-во тяг: {item_count_traction}, Тип зарядки: {item_charging_type}\n" \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_vaping_liquids(vaping_liquids:list) -> str:
    finish_string = "<b>Жидкости</b>\n"
    for vaping_liquid in vaping_liquids:

        item_id_in_shop = vaping_liquid[0]
        item_id = vaping_liquid[1]
        brand_name = vaping_liquid[2]
        item_name = vaping_liquid[3]
        item_taste = vaping_liquid[4]
        item_fortress = vaping_liquid[5]
        item_size = vaping_liquid[6]
        item_count = vaping_liquid[7]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Вкус: <i>{item_taste}</i>, Тяжесть: {item_fortress} мг. , Объем: {item_size}\n" \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_pod_systems(pod_systems:list) -> str:
    finish_string = "<b>POD системы</b>\n"
    for pod_system in pod_systems:

        item_id_in_shop = pod_system[0]
        item_id = pod_system[1]
        brand_name = pod_system[2]
        item_name = pod_system[3]
        item_count = pod_system[4]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_pod_systems_accessories(pod_systems_accessories:list) -> str:
    finish_string = "<b>Комплектующие POD cистем</b>\n"
    for pod_systems_accessory in pod_systems_accessories:

        item_id_in_shop = pod_systems_accessory[0]
        item_id = pod_systems_accessory[1]
        brand_name = pod_systems_accessory[2]
        item_name = pod_systems_accessory[3]
        item_count = pod_systems_accessory[4]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_hookah_charcoal(hookah_charcoals:list) -> str:
    finish_string = "<b>Кальянный уголь</b>\n"
    for hookah_charcoal in hookah_charcoals:

        item_id_in_shop = hookah_charcoal[0]
        item_id = hookah_charcoal[1]
        brand_name = hookah_charcoal[2]
        item_name = hookah_charcoal[3]
        item_count_in_box = hookah_charcoal[4]
        item_size = hookah_charcoal[5]
        item_count = hookah_charcoal[6]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Кол-во в коробке: {item_count_in_box}, Размер: {item_size}\n"  \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_hookah_tobacco(hookah_tobacco:list) -> str:
    finish_string = "<b>Кальянный табак</b>\n"
    for tobacco in hookah_tobacco:

        item_id_in_shop = tobacco[0]
        item_id = tobacco[1]
        brand_name = tobacco[2]
        item_name = tobacco[3]
        item_taste = tobacco[4]
        item_size = tobacco[5]
        item_count = tobacco[6]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Вкус: <i>{item_taste}</i>, Размер: {item_size} мг.\n"  \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string


def create_view_electronic_devices(electronic_devices:list) -> str:
    finish_string = "<b>Электронные устройства</b>\n"
    for electronic_device in electronic_devices:

        item_id_in_shop = electronic_device[0]
        item_id = electronic_device[1]
        brand_name = electronic_device[2]
        item_name = electronic_device[3]
        item_count = electronic_device[4]

        finish_string += f"<b>ID В Магазине: {item_id_in_shop}</b>, <b>ID Продукта: {item_id}</b>\nБренд: {brand_name}, Название: {item_name}\n" \
                         f"Кол-во: {item_count} шт.\n\n"
    return finish_string