import sqlite3
from settings.config import path_db

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


def add_product(category:str,brand:str,name:str) :
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'INSERT INTO Products ( category_id, brand_id, item_name) SELECT Categories.category_id , Brands.brand_id, Crutch.item_name  ' \
                            'FROM Categories,Brands ,Crutch Where Categories.category_name = ? and Brands.brand_name = ? and Crutch.item_name = ?'
        data = (category,brand,'new_name')
        cursor.execute(insert_with_param, data)
        sqlite_connection.commit()

        insert_with_param1 = 'UPDATE Products SET item_name = ? WHERE item_name = ?'
        data1 = (name, 'new_name')
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