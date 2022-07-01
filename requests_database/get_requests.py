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


def check_user_is_seller(user_id: int):
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


def check_shop_id_by_user(user_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select user_shop FROM Users WHERE user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce[0] is not None:
            cursor.close()
            return responce[0]
        elif responce[0] is None:
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


def is_user_have_receipts(user_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select * FROM Receipts 
        WHERE employee_id = ?
        GROUP BY employee_id'''
        data = (user_id,)
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


def is_user_have_open_receipt(user_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select * FROM Receipts 
        WHERE employee_id = ? and receipt_status = 2'''
        data = (user_id,)
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


def check_open_receipt_id(user_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select Receipts.id_receipt FROM Receipts 
        WHERE employee_id = ? and receipt_status = 2'''
        data = (user_id,)
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



def check_all_sales_item_in_receipt(open_receipt_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select Sales.item_id,Sales.item_id_in_shop,Brands.brand_name,Products.item_name,Sales.item_count, Products.item_price FROM Sales INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and Sales.item_id = Products.item_id
        WHERE receipt_id = ?'''
        data = (open_receipt_id,)
        cursor.execute(sql_select_query, data)
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


def check_sales_for_delete_position(open_receipt_id: int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select Sales.sales_id FROM Sales 
        WHERE receipt_id = ?'''
        data = (open_receipt_id,)
        cursor.execute(sql_select_query, data)
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


def all_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM ShopsInfo ORDER BY shop_id'
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


def get_shop_by_id(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'Select * FROM ShopsInfo WHERE shop_id = ?'
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
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


def get_product_brand_and_name(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_name, Products.item_name FROM Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id
        Where Products.item_id = ?'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
        responce = cursor.fetchall()
        if responce:
            cursor.close()
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


def get_disposable_cigarettes_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        DisposableСigarettes.item_taste,DisposableСigarettes.item_count_traction,ChargingTypes.type_name,DisposableСigarettes.item_count
        FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands INNER JOIN ChargingTypes
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id = Products.item_id and ChargingTypes.type_id = DisposableСigarettes.item_charging_type
        Where DisposableСigarettes.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_vaping_liquids_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        VapingLiquids.item_taste,VapingLiquids.item_fortress,VapingLiquids.item_size,VapingLiquids.item_count
        FROM VapingLiquids INNER JOIN Products INNER JOIN Brands
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id = Products.item_id
        Where VapingLiquids.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_pod_systems_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystems.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        PodSystems.item_count
        FROM PodSystems INNER JOIN Products INNER JOIN Brands
        ON Products.brand_id = Brands.brand_id and PodSystems.item_id = Products.item_id
        Where PodSystems.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_pod_systems_accessories_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystemsAccessories.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        PodSystemsAccessories.item_count
        FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands
        ON Products.brand_id = Brands.brand_id and PodSystemsAccessories.item_id = Products.item_id
        Where PodSystemsAccessories.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_hookah_charcoal_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahCharcoal.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        HookahCharcoal.item_count_in_box, SizeCharcoal.size_name ,HookahCharcoal.item_count
        FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands INNER JOIN SizeCharcoal
        ON Products.brand_id = Brands.brand_id and HookahCharcoal.item_id = Products.item_id and SizeCharcoal.size_id = HookahCharcoal.item_size
        Where HookahCharcoal.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_hookah_tobacco_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahTobacco.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        HookahTobacco.item_taste, HookahTobacco.item_size ,HookahTobacco.item_count
        FROM HookahTobacco INNER JOIN Products INNER JOIN Brands
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id = Products.item_id 
        Where HookahTobacco.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def get_electronic_devices_by_shopid(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT ElectronicDevices.item_id_in_shop,
        Products.item_id,Brands.brand_name,Products.item_name,
        ElectronicDevices.item_count
        FROM ElectronicDevices INNER JOIN Products INNER JOIN Brands
        ON Products.brand_id = Brands.brand_id and ElectronicDevices.item_id = Products.item_id 
        Where ElectronicDevices.shop_id = ?
        ORDER BY Products.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def is_product_in_shop(item_id,shop_id):
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


def check_category_id(category_name:str):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT category_id FROM Categories WHERE category_name = ?'
        data = (category_name,)
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


def check_product_in_shop(name_table:str,shop_id:int,item_id_in_shop:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM ? WHERE shop_id = ? and item_id_in_shop = ?'
        data = (name_table,shop_id,item_id_in_shop)
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


def check_liquid_info_in_all_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_id 
        ORDER BY Brands.brand_name'''
        cursor.execute(sql_select_query, )
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


def check_liquid_info_in_shop(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_count > 0 and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_id 
        ORDER BY Brands.brand_name'''
        data = (shop_id,)
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


def check_all_liquid_by_fortress(item_fortress:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_id 
        ORDER BY Brands.brand_name'''
        data = (item_fortress,)
        cursor.execute(sql_select_query,data)
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


def check_all_liquid_by_fortress_in_shop(item_fortress:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0 and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_id 
        ORDER BY Brands.brand_name'''
        data = (item_fortress,shop_id)
        cursor.execute(sql_select_query,data)
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



def check_liquid_fortress_in_all_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_fortress FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id = Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_fortress
        ORDER BY Brands.brand_name'''
        cursor.execute(sql_select_query, )
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


def check_liquid_fortress_in_shop(shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_fortress FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id = Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_count > 0 and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_fortress
        ORDER BY Brands.brand_name'''
        data = (shop_id,)
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


def check_liquid_fortress_in_all_shops_by_id(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_fortress FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id = Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_id =? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_fortress
        ORDER BY Brands.brand_name'''
        data = (item_id,)
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


def check_liquid_fortress_in_shop_by_item(item_id,shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_fortress FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id = Products.item_id and Products.brand_id = Brands.brand_id
        WHERE VapingLiquids.item_id =? and VapingLiquids.item_count > 0 and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_fortress
        ORDER BY Brands.brand_name'''
        data = (item_id,shop_id)
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


def check_taste_liquid_by_id_and_fortress(item_id:int,item_fortress:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id,VapingLiquids.item_taste FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_taste'''
        data = (item_id,item_fortress)
        cursor.execute(sql_select_query,data)
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


def shop_taste_liquid_by_id_and_fortress(item_id:int,item_fortress:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id,VapingLiquids.item_taste FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_taste'''
        data = (item_id,item_fortress,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_characteristic_disposable_cigarette(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_name,Products.item_name,DisposableСigarettes.item_count_traction,ChargingTypes.type_name,Products.item_price FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands INNER JOIN ChargingTypes  
        ON DisposableСigarettes.item_id == Products.item_id and Products.brand_id = Brands.brand_id and ChargingTypes.type_id = DisposableСigarettes.item_charging_type
        WHERE Products.item_id = ?
        GROUP BY DisposableСigarettes.item_id'''
        data = (item_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
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


def check_characteristic_hookah_tobacco(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_name,Products.item_name,HookahTobacco.item_size,Products.item_price FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON HookahTobacco.item_id == Products.item_id and Products.brand_id = Brands.brand_id 
        WHERE Products.item_id = ?
        GROUP BY HookahTobacco.item_id'''
        data = (item_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
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


def check_characteristic_hookah_charcoal(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_name,Products.item_name,SizeCharcoal.size_name,HookahCharcoal.item_count_in_box,Products.item_price FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands INNER JOIN SizeCharcoal  
        ON HookahCharcoal.item_id == Products.item_id and Products.brand_id = Brands.brand_id and SizeCharcoal.size_id = HookahCharcoal.item_size
        WHERE Products.item_id = ?
        GROUP BY HookahCharcoal.item_id'''
        data = (item_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
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


def check_characteristic_liquid(item_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_name,Products.item_name,VapingLiquids.item_fortress,VapingLiquids.item_size,Products.item_price FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON VapingLiquids.item_id == Products.item_id and Products.brand_id = Brands.brand_id 
        WHERE Products.item_id = ?
        GROUP BY VapingLiquids.item_fortress'''
        data = (item_id,)
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


def check_all_brands_disposable_cigarettes_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON DisposableСigarettes.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE DisposableСigarettes.item_count > 0
        GROUP BY Brands.brand_id'''
        cursor.execute(sql_select_query,)
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


def check_all_brands_disposable_cigarettes_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON DisposableСigarettes.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE DisposableСigarettes.item_count > 0 and DisposableСigarettes.shop_id = ?
        GROUP BY Brands.brand_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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



def check_all_brands_hookah_tobacco_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON HookahTobacco.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE HookahTobacco.item_count > 0
        GROUP BY Brands.brand_id'''
        cursor.execute(sql_select_query,)
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


def check_all_brands_hookah_tobacco_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON HookahTobacco.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE HookahTobacco.item_count > 0 and HookahTobacco.shop_id = ?
        GROUP BY Brands.brand_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def check_all_brands_hookah_tobacco_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON HookahTobacco.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE HookahTobacco.shop_id = ? and HookahTobacco.item_count > 0
        GROUP BY Brands.brand_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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



def check_all_brands_pod_systems_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON PodSystems.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE PodSystems.item_count > 0
        GROUP BY Brands.brand_id'''
        cursor.execute(sql_select_query,)
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


def check_all_brands_pod_systems_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON PodSystems.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE PodSystems.shop_id = ? and PodSystems.item_count > 0
        GROUP BY Brands.brand_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def check_all_brands_pod_systems_accessories_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON PodSystemsAccessories.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE PodSystemsAccessories.item_count > 0 
        GROUP BY Brands.brand_id'''
        cursor.execute(sql_select_query,)
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


def check_all_brands_pod_systems_accessories_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Brands.brand_id,Brands.brand_name FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON PodSystemsAccessories.item_id == Products.item_id and Products.brand_id = Brands.brand_id
        WHERE PodSystemsAccessories.shop_id = ? and PodSystemsAccessories.item_count > 0 
        GROUP BY Brands.brand_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def check_all_size_hookah_charcoal_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahCharcoal.item_size, SizeCharcoal.size_name FROM HookahCharcoal INNER JOIN SizeCharcoal
        ON HookahCharcoal.item_size = SizeCharcoal.size_id
        WHERE HookahCharcoal.item_count > 0
        GROUP BY HookahCharcoal.item_size'''
        cursor.execute(sql_select_query,)
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


def check_all_size_hookah_charcoal_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahCharcoal.item_size, SizeCharcoal.size_name FROM HookahCharcoal INNER JOIN SizeCharcoal
        ON HookahCharcoal.item_size = SizeCharcoal.size_id
        WHERE HookahCharcoal.shop_id = ? and HookahCharcoal.item_count > 0
        GROUP BY HookahCharcoal.item_size'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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


def check_disposable_cigarette_name_and_price_by_brand_id(brand_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 1  and DisposableСigarettes.item_count > 0
        GROUP BY DisposableСigarettes.item_id'''
        data = (brand_id,)
        cursor.execute(sql_select_query,data)
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


def shop_disposable_cigarette_name_and_price_by_brand_id(brand_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 1  and DisposableСigarettes.item_count > 0 and DisposableСigarettes.shop_id = ?
        GROUP BY DisposableСigarettes.item_id'''
        data = (brand_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_hookah_tobacco_name_and_price_by_brand_id(brand_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 6 and HookahTobacco.item_count > 0
        GROUP BY HookahTobacco.item_id'''
        data = (brand_id,)
        cursor.execute(sql_select_query,data)
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


def shop_hookah_tobacco_name_and_price_by_brand_id(brand_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 6 and HookahTobacco.item_count > 0 and HookahTobacco.shop_id = ?
        GROUP BY HookahTobacco.item_id'''
        data = (brand_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_all_electronic_devices_in_shops():
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM ElectronicDevices INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and ElectronicDevices.item_id == Products.item_id
        WHERE category_id = 7 and ElectronicDevices.item_count > 0
        GROUP BY ElectronicDevices.item_id'''
        cursor.execute(sql_select_query,)
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


def check_all_electronic_devices_in_shop(shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM ElectronicDevices INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and ElectronicDevices.item_id == Products.item_id
        WHERE category_id = 7 and ElectronicDevices.item_count > 0 and ElectronicDevices.shop_id = ?
        GROUP BY ElectronicDevices.item_id'''
        data = (shop_id,)
        cursor.execute(sql_select_query,data)
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



def check_pod_systems_name_and_price_by_brand_id(brand_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystems.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 3
        GROUP BY PodSystems.item_id'''
        data = (brand_id,)
        cursor.execute(sql_select_query,data)
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


def shop_pod_systems_name_and_price_by_brand_id(brand_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystems.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 3 and PodSystems.item_count > 0 and PodSystems.shop_id = ?
        GROUP BY PodSystems.item_id'''
        data = (brand_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_hookah_charcoal_name_and_price_by_size_id(size_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahCharcoal.item_id == Products.item_id
        WHERE HookahCharcoal.item_size = ?  and category_id = 5 and HookahCharcoal.item_count > 0
        GROUP BY HookahCharcoal.item_id'''
        data = (size_id,)
        cursor.execute(sql_select_query,data)
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


def shop_hookah_charcoal_name_and_price_by_size_id(size_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahCharcoal.item_id == Products.item_id
        WHERE HookahCharcoal.item_size = ?  and category_id = 5 and HookahCharcoal.item_count > 0
        and HookahCharcoal.shop_id = ?
        GROUP BY HookahCharcoal.item_id'''
        data = (size_id,shop_id)
        cursor.execute(sql_select_query,data)
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



def check_pod_accessories_name_and_price_by_brand_id(brand_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystemsAccessories.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 4 and PodSystemsAccessories.item_count > 0
        GROUP BY PodSystemsAccessories.item_id'''
        data = (brand_id,)
        cursor.execute(sql_select_query,data)
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


def shop_pod_accessories_name_and_price_by_brand_id(brand_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT Products.item_id,Brands.brand_name,Products.item_name,Products.item_price FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystemsAccessories.item_id == Products.item_id
        WHERE Brands.brand_id == ?  and category_id = 4 and PodSystemsAccessories.item_count > 0 
        and PodSystemsAccessories.shop_id = ?
        GROUP BY PodSystemsAccessories.item_id'''
        data = (brand_id,shop_id)
        cursor.execute(sql_select_query,data)
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



def check_taste_disposable_cigarette(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.item_id,DisposableСigarettes.item_taste FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE DisposableСigarettes.item_id = ? and DisposableСigarettes.item_count > 0
        GROUP BY DisposableСigarettes.item_taste'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def shop_taste_disposable_cigarette(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.item_id,DisposableСigarettes.item_taste FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE DisposableСigarettes.item_id = ? and DisposableСigarettes.item_count > 0 and DisposableСigarettes.shop_id = ?
        GROUP BY DisposableСigarettes.item_taste'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_taste_hookah_tobacco_in_shop(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahTobacco.item_id,HookahTobacco.item_taste FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE HookahTobacco.item_id = ? and HookahTobacco.item_count > 0 and HookahTobacco.shop_id = ?
        GROUP BY HookahTobacco.item_taste'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_taste_liquid(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id,VapingLiquids.item_taste FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_taste'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def check_taste_hookah_tobacco(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahTobacco.item_id,HookahTobacco.item_taste FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE HookahTobacco.item_id = ? and HookahTobacco.item_count > 0
        GROUP BY HookahTobacco.item_taste'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def check_taste_liquid_with_fortress(item_id:int,item_fortress:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id,VapingLiquids.item_taste FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.item_taste'''
        data = (item_id,item_fortress)
        cursor.execute(sql_select_query,data)
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


def check_taste_liquid_with_fortress_in_shop(item_id:int,item_fortress:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.item_id,VapingLiquids.item_taste FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.item_taste'''
        data = (item_id,item_fortress,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_shop_id_by_disposable_cigarettes(item_id:int,item_taste):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.shop_id FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE DisposableСigarettes.item_id = ? and DisposableСigarettes.item_taste = ? and DisposableСigarettes.item_count > 0
        GROUP BY DisposableСigarettes.shop_id'''
        data = (item_id,item_taste)
        cursor.execute(sql_select_query,data)
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


def is_disposable_cigarettes_in_shop(item_id:int,item_taste,shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.shop_id FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE DisposableСigarettes.item_id = ? and DisposableСigarettes.item_taste = ? and DisposableСigarettes.item_count > 0 
        and DisposableСigarettes.shop_id = ?
        GROUP BY DisposableСigarettes.shop_id'''
        data = (item_id,item_taste,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_disposable_cigarettes_id_in_shop(item_id:int,item_taste,shop_id):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT DisposableСigarettes.item_id_in_shop,DisposableСigarettes.item_id FROM DisposableСigarettes INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and DisposableСigarettes.item_id == Products.item_id
        WHERE DisposableСigarettes.item_id = ? and DisposableСigarettes.item_taste = ? and DisposableСigarettes.item_count > 0 
        and DisposableСigarettes.shop_id = ?
        GROUP BY DisposableСigarettes.shop_id'''
        data = (item_id,item_taste,shop_id)
        cursor.execute(sql_select_query,data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return responce
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


def check_shop_id_by_hookah_tobacco(item_id:int,item_taste):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahTobacco.shop_id FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE HookahTobacco.item_id = ? and HookahTobacco.item_taste = ? and HookahTobacco.item_count > 0
        GROUP BY HookahTobacco.shop_id'''
        data = (item_id,item_taste)
        cursor.execute(sql_select_query,data)
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


def is_hookah_tobacco_in_shop(item_id:int,item_taste,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahTobacco.shop_id FROM HookahTobacco INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahTobacco.item_id == Products.item_id
        WHERE HookahTobacco.item_id = ? and HookahTobacco.item_taste = ? and HookahTobacco.item_count > 0
        and HookahTobacco.shop_id = ?
        GROUP BY HookahTobacco.shop_id'''
        data = (item_id,item_taste,shop_id)
        cursor.execute(sql_select_query,data)
        responce = cursor.fetchone()
        if responce is not None:
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


def check_shop_id_by_electronic_devices(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT ElectronicDevices.shop_id FROM ElectronicDevices INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and ElectronicDevices.item_id == Products.item_id
        WHERE ElectronicDevices.item_id = ? and ElectronicDevices.item_count > 0
        GROUP BY ElectronicDevices.shop_id'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def is_electronic_devices_in_shop(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT ElectronicDevices.shop_id FROM ElectronicDevices INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and ElectronicDevices.item_id == Products.item_id
        WHERE ElectronicDevices.item_id = ? and ElectronicDevices.item_count > 0 and ElectronicDevices.shop_id = ?
        GROUP BY ElectronicDevices.shop_id'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_shop_id_by_pod_systems(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystems.shop_id FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystems.item_id == Products.item_id
        WHERE PodSystems.item_id = ? and PodSystems.item_count > 0
        GROUP BY PodSystems.shop_id'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def is_pod_systems_in_shop(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystems.shop_id FROM PodSystems INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystems.item_id == Products.item_id
        WHERE PodSystems.item_id = ? and PodSystems.item_count > 0 and PodSystems.shop_id = ?
        GROUP BY PodSystems.shop_id'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_shop_id_by_pod_accessories(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystemsAccessories.shop_id FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystemsAccessories.item_id == Products.item_id
        WHERE PodSystemsAccessories.item_id = ? and PodSystemsAccessories.item_count > 0
        GROUP BY PodSystemsAccessories.shop_id'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def is_pod_accessories_in_shop(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT PodSystemsAccessories.shop_id FROM PodSystemsAccessories INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and PodSystemsAccessories.item_id == Products.item_id
        WHERE PodSystemsAccessories.item_id = ? and PodSystemsAccessories.item_count > 0 and PodSystemsAccessories.shop_id = ?
        GROUP BY PodSystemsAccessories.shop_id'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_shop_id_by_hookah_charcoal(item_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahCharcoal.shop_id FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahCharcoal.item_id == Products.item_id
        WHERE HookahCharcoal.item_id = ? and HookahCharcoal.item_count > 0
        GROUP BY HookahCharcoal.shop_id'''
        data = (item_id,)
        cursor.execute(sql_select_query,data)
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


def is_hookah_charcoal_in_shop(item_id:int,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT HookahCharcoal.shop_id FROM HookahCharcoal INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and HookahCharcoal.item_id == Products.item_id
        WHERE HookahCharcoal.item_id = ? and HookahCharcoal.item_count > 0 and HookahCharcoal.shop_id = ?
        GROUP BY HookahCharcoal.shop_id'''
        data = (item_id,shop_id)
        cursor.execute(sql_select_query,data)
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
        return None
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def check_shop_id_by_liquid(item_id:int,item_taste,item_fortress):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.shop_id FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_taste = ? and VapingLiquids.item_fortress = ?  and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.shop_id'''
        data = (item_id,item_taste,item_fortress)
        cursor.execute(sql_select_query,data)
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



def check_shop_id_by_liquid_fortress(item_id:int,item_taste,item_fortress):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.shop_id FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_taste = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        GROUP BY VapingLiquids.shop_id'''
        data = (item_id,item_taste,item_fortress)
        cursor.execute(sql_select_query,data)
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


def is_liquid_fortress_in_shop(item_id:int,item_taste,item_fortress,shop_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''SELECT VapingLiquids.shop_id FROM VapingLiquids INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and VapingLiquids.item_id == Products.item_id
        WHERE VapingLiquids.item_id = ? and VapingLiquids.item_taste = ? and VapingLiquids.item_fortress = ? and VapingLiquids.item_count > 0
        and VapingLiquids.shop_id = ?
        GROUP BY VapingLiquids.shop_id'''
        data = (item_id,item_taste,item_fortress,shop_id)
        cursor.execute(sql_select_query,data)
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


def check_close_receipts(user_id: int, date):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select * FROM Receipts 
        WHERE employee_id = ? and receipt_status = 1 and date(date) = ? '''
        data = (user_id,date)
        cursor.execute(sql_select_query, data)
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


def check_close_sales(user_id: int, receipt_id:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = '''Select Sales.item_id,Sales.item_id_in_shop,Brands.brand_name,Products.item_name,Sales.item_count,Products.item_price FROM Sales 
        INNER JOIN Products INNER JOIN Brands 
        ON Products.brand_id = Brands.brand_id and Sales.item_id == Products.item_id
        WHERE employee_id = ? and sale_status = 1 and receipt_id = ? '''
        data = (user_id,receipt_id)
        cursor.execute(sql_select_query, data)
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