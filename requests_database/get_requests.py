import sqlite3
from settings.config import path_db

def is_incomplete_user(user_id:int) -> bool:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Users where user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce:
            cursor.close()
            return True
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_user_roles(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM Roles WHERE user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return None
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_complete_user(user_id: int) -> bool:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT user_phone FROM Users where user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce[0]:
            if str(responce[0]) != '':
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif not responce[0]:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return None
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_user_is_seller(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        role_id = 2
        sql_select_query = 'Select * FROM Roles WHERE user_id = ? and role_id = ?'
        data = (user_id,role_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return True
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_user_is_admin(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        role_id = 3
        sql_select_query = 'Select * FROM Roles WHERE user_id = ? and role_id = ?'
        data = (user_id,role_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return True
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_user_is_buyer(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        role_id = 1
        sql_select_query = 'Select * FROM Roles WHERE user_id = ? and role_id = ?'
        data = (user_id,role_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return True
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def all_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM ShopsInfo'
        cursor.execute(sql_select_query, )
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def all_сharging_types():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM ChargingTypes'
        cursor.execute(sql_select_query, )
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def all_size_charcoal():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM SizeCharcoal'
        cursor.execute(sql_select_query, )
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_brand(brand:str) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Brands WHERE brand_name = ?'
        data = (brand,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce:
            if responce[1].lower() == brand.lower():
                cursor.close()
                return True
            else:
                cursor.close()
                return False
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_brand_in_id(brand_id:int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Brands WHERE brand_id = ?'
        data = (brand_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        elif responce is None:
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def get_all_categories() -> list():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Categories'
        cursor.execute(sql_select_query)
        responce = cursor.fetchall()
        if responce:
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def get_brands_starting_with_letter(letter:str) -> list():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Brands WHERE brand_name LIKE ? OR ?'
        data = (letter + '%',letter.lower() + '%')
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_product(category:str,brand:str,name:str):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,category_name,brand_name,item_name FROM Products INNER JOIN Categories INNER JOIN Brands ' \
                           'ON Products.category_id = Categories.category_id and Products.brand_id = Brands.brand_id ' \
                           'Where category_name = ? and brand_name = ? and item_name = ?'
        data = (category,brand,name)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if responce[1].lower() == category.lower() and responce[2].lower() == brand.lower() and responce[3].lower() == name.lower():
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_disposable_cigarettes(item_id:int,shop_id:int,item_taste:str,item_count_traction:int,item_charging_type:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id,item_taste,item_count_traction,item_charging_type FROM DisposableСigarettes' \
                           ' Where item_id = ? and shop_id = ? and item_taste = ? and item_count_traction = ? and item_charging_type = ?'
        data = (item_id,shop_id,item_taste,item_count_traction,item_charging_type)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id and \
                    responce[2].lower() == item_taste.lower()  and int(responce[3]) == item_count_traction and \
                    int(responce[4]) == item_charging_type:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_vaping_liquids(item_id:int,shop_id:int,item_taste:str,item_fortress:int,item_size:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id,item_taste,item_fortress,item_size FROM VapingLiquids' \
                           ' Where item_id = ? and shop_id = ? and item_taste = ? and item_fortress = ? and item_size = ?'
        data = (item_id,shop_id,item_taste,item_fortress,item_size)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id and responce[2].lower() == item_taste.lower() \
                    and int(responce[3]) == item_fortress and int(responce[4]) == item_size:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_hookah_tobacco(item_id:int,shop_id:int,item_taste:str,item_size:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id,item_taste,item_size FROM HookahTobacco' \
                           ' Where item_id = ? and shop_id = ? and item_taste = ? and item_size = ?'
        data = (item_id,shop_id,item_taste,item_size)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id and responce[2].lower() == item_taste.lower() \
                     and int(responce[4]) == item_size:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_hookah_charcoal(item_id:int,shop_id:int,item_count_in_box:int,item_size:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id,item_count_in_box,item_size FROM HookahCharcoal' \
                           ' Where item_id = ? and shop_id = ? and item_count_in_box = ? and item_size = ? '
        data = (item_id,shop_id,item_count_in_box,item_size)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id and int(responce[2]) == item_count_in_box \
                    and int(responce[3]) == item_size:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_category_in_db(category):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Categories WHERE category_name = ?'
        data = (category,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_product_in_db(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Products WHERE item_id = ?'
        data = (item_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_product_corresponds_category(item_id,category_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Products WHERE item_id = ? and category_id = ?'
        data = (item_id,category_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_brand_in_db(brand):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Brands WHERE brand_name = ?'
        data = (brand,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_products_with_category(category_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,category_name,brand_name,item_name,item_price FROM Products INNER JOIN Categories ' \
                           'INNER JOIN Brands ON Products.category_id = Categories.category_id and ' \
                           'Products.brand_id = Brands.brand_id Where Products.category_id = ?'
        data = (category_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
            return responce
        elif not responce:
            print('Нет')
            cursor.close()
            return list()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_category_by_product(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT category_id FROM Products WHERE item_id = ?'
        data = (item_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return responce[0]
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_category_name(category_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT category_name FROM Categories WHERE category_id = ?'
        data = (category_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            return responce[0]
        elif not responce:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_pod(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id FROM PodSystems' \
                           ' Where item_id = ? and shop_id = ?'
        data = (item_id,shop_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_electronic_devices(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id FROM ElectronicDevices' \
                           ' Where item_id = ? and shop_id = ?'
        data = (item_id,shop_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_similar_pod_accessories(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT item_id,shop_id FROM PodSystemsAccessories' \
                           ' Where item_id = ? and shop_id = ?'
        data = (item_id,shop_id)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            if int(responce[0]) == item_id and int(responce[1]) == shop_id:
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        elif responce is None:
            print('Нет')
            cursor.close()
            return False
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")