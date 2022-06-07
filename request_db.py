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


def record_incomplete_user(user_id: int, user_name: str, user_surname: str, link: str)-> None:
    try:
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
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
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        insert_with_param = 'UPDATE Users SET user_phone = ? WHERE user_id = ?'
        data = (phone_number, user_id)
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


def record_user_role_buyer(user_id: int) -> None:
    try:
        sqlite_connection = sqlite3.connect('database/smokybro_db.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")
        user_role = 'Покупатель'
        insert_with_param = 'INSERT INTO Roles (user_id, user_role) VALUES (?, ?)'
        data = (user_id,user_role)
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
