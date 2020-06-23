import sqlite3
import os.path


class SQLither(object):
    '''Класс для взаимодействия с БД'''

    def __init__(self, database: str = 'data') -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()
        self.database_name = database

    def get_users(self) -> list:
        '''Получение пользователей который пользовались ботом'''
        with self.connection:
            return self.cursor.execute('SELECT * FROM subscriptions ').fetchall()

    def add_user(self, user_id: str, videoname: str):
        '''add user to DB'''
        with self.connection:
            self.cursor.execute('INSERT INTO subscriptions (video_text , user_id) VALUES (? , ?) ',
                                (videoname, user_id,))

    def delete_user(self, user_id: str, datameta: str = None):
        with self.connection:
            self.cursor.execute('DELETE FROM subscriptions WHERE user_id = ? AND video_text = ?',
                                (user_id, datameta))

    def delete_all(self, user_id: str):
        with self.connection:
            self.cursor.execute('DELETE FROM subscriptions WHERE user_id = ?',
                                (user_id,))

    def init_database(self):
        '''init to database'''
        with open(self.database_name, "r") as f:
            sql = f.read()
        self.cursor.executescript(sql)
        self.connection.commit()

    def check_init_database(self):
        '''check exists database'''
        if os.path.exists(self.database_name):
            pass

        else:
            self.init_database()

    def truncate_table(self):
        '''Truncate table from DB'''
        with self.connection:
            self.cursor.execute('DELETE FROM subscriptions')
