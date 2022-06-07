import sqlite3

def is_incomplete_user(user_id:int) -> bool:
    try:
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT * FROM Users where user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce is not None:
            cursor.close()
            return True
        else:
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
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        user_role = 'Покупатель'
        sql_select_query = 'Select * FROM Roles WHERE user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchall()
        if responce is not None:
            cursor.close()
            return responce
        else:
            print('Нет')
            cursor.close()
            return None
    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
        sqlite_connection.close()
        return "exception"
        print("Соединение с SQLite закрыто")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def is_complete_user(user_id: int) -> bool:
    try:
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        sql_select_query = 'SELECT user_phone FROM Users where user_id = ?'
        data = (user_id,)
        cursor.execute(sql_select_query, data)
        responce = cursor.fetchone()
        if responce[0] is not None:
            if str(responce[0]) != '':
                cursor.close()
                return True
            else:
                print('Нет')
                cursor.close()
                return False
        else:
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
