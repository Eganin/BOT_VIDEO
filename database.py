import sqlite3
import os.path


class SQLither(object):
    def __init__(self, database: str = 'data') -> None:
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def get_user(self) -> list:
        with self.connection:
            return self.cursor.execute('SELECT * FROM subscriptions ').fetchall()

    def add_user(self, user_id: str, videoname: str):
        with self.connection:
            self.cursor.execute('INSERT INTO subscriptions (video_text , user_id) VALUES (? , ?) ',
                                (videoname, user_id,))

    def init_database(self):
        pass

    def check_init_database(self):
        pass

    def truncate_table(self):
        with self.connection:
            self.cursor.execute('DELETE FROM subscriptions')
