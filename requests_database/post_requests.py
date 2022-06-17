import sqlite3
from settings.config import path_db
from decimal import Decimal


def record_incomplete_user(user_id: int, user_name: str, user_surname: str, link: str)-> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO Users (user_id, user_name, user_surname,user_link) VALUES (?, ?, ?, ?)'
        data = (user_id, user_name, user_surname, link)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Users")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def record_user_phone(user_id: int, phone_number : str) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'UPDATE Users SET user_phone = ? WHERE user_id = ?'
        data = (phone_number, user_id)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно обновлены в таблице Users")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def record_user_role_buyer(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        role_id = 1
        insert_with_param = 'INSERT INTO Roles (user_id, role_id) VALUES (?, ?)'
        data = (user_id,role_id)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Roles")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_brand(brand: str) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO Brands (brand_name) VALUES (?)'
        data = (brand,)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_product(category:str,brand:str,name:str,item_price) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO Products ( category_id, brand_id, item_name) SELECT Categories.category_id , Brands.brand_id, Crutch.item_name  ' \
                            'FROM Categories,Brands ,Crutch Where Categories.category_name = ? and Brands.brand_name = ? and Crutch.item_name = ?'
        data = (category,brand,'new_name')
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()

        insert_with_param1 = 'UPDATE Products SET item_name = ?,item_price =? WHERE item_name = ?'
        data1 = (name,item_price, 'new_name')
        cursor.execute(insert_with_param1, data1)
        sqlite_connection.commit()

        print("Переменные Python успешно вставлены в таблицу Brands")
        cursor.close()
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def update_product(brand:str,name:str,item_price,item_id:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = "UPDATE Products " \
                            "SET brand_id = (SELECT brand_id FROM Brands WHERE brand_name = ?), " \
                            "item_name = ?, " \
                            "item_price = ? " \
                            "WHERE Products.item_id = ?"
        data = (brand,name,item_price,item_id)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        cursor.close()
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_disposable_cigarettes_in_shop(item_id:int,shop_id:int,item_taste:str,item_count_traction:int, item_charging_type:int ,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO DisposableСigarettes (item_id, shop_id, item_taste,item_count_traction,item_charging_type,item_count) ' \
                            'VALUES (?, ?, ?, ?, ?, ?)'
        data = (item_id,shop_id,item_taste,item_count_traction,item_charging_type,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        cursor.close()
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_vaping_liquids_in_shop(item_id:int,shop_id:int,item_taste:str,item_fortress:int,item_size:int,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO VapingLiquids (item_id, shop_id, item_taste,item_fortress,item_size,item_count) ' \
                            'VALUES (?, ?, ?, ?, ?, ?)'
        data = (item_id,shop_id,item_taste,item_fortress,item_size,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_hookah_tobacco_in_shop(item_id:int,shop_id:int,item_taste:str,item_size:int,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO HookahTobacco (item_id, shop_id, item_taste,item_size,item_count) ' \
                            'VALUES (?, ?, ?, ?, ?)'
        data = (item_id,shop_id,item_taste,item_size,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_vaping_hookah_charcoal(item_id:int,shop_id:int,item_count_in_box:int,item_size:int,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO HookahCharcoal (item_id, shop_id, item_count_in_box,item_size,item_count) ' \
                            'VALUES (?, ?, ?, ?, ?)'
        data = (item_id,shop_id,item_count_in_box,item_size,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_vaping_pod(item_id:int,shop_id:int,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO PodSystems (item_id, shop_id, item_count) ' \
                            'VALUES (?, ?, ?)'
        data = (item_id,shop_id,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def add_electronic_devices(item_id:int,shop_id:int,item_count:int) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO ElectronicDevices (item_id, shop_id, item_count) ' \
                            'VALUES (?, ?, ?)'
        data = (item_id,shop_id,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def add_pod_accessories(item_id:int,shop_id:int,item_count:int):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO PodSystemsAccessories (item_id, shop_id, item_count) ' \
                            'VALUES (?, ?, ?)'
        data = (item_id,shop_id,item_count)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно вставлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



def update_brand_in_id(brand_id:int,brand_name:str):
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param =  'UPDATE Brands SET brand_name = ? WHERE brand_id = ?'
        data = (brand_name,brand_id)
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()
        print("Переменные Python успешно обновлены в таблицу Brands")
        return True
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
        return False
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")