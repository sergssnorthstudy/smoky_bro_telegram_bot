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


def all_shops() -> None:
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


def check_similar_brand(brand:str) -> None:
    try:
        sqlite_connection = sqlite3.connect(path_db)
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Brands WHERE brand_name = ?'
        data = (brand,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
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