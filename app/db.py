import sqlite3
import datetime

class Database:
    def __init__(self, path_to_db='app/main_db.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone = False,
                fetchall = False, commit = False):
        if not parametrs:
            parametrs = tuple()
        connection = self.connection
        cursor =connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        connection.close()
        return data

    def create_table_message(self):
        sql = """
                CREATE TABLE Message (
                    id INTEGER PRIMARY KEY,
                    id_chat INTEGER NOT NULL,
                    id_message STRING NOT NULL,
                    date DATE NOT NULL,
                    stat STRING NOT NULL,
                    state_date int NOT NULL
                );
        """
        self.execute(sql, commit=True)
    def search_chat_id():
        # поиск чата с определенным id
        pass

    def add_message(self, id_chat: int, id_message: int, date: str, stat: str, state_date: int):
        # если чат уже есть, то обновляем данные
        sql = "INSERT INTO Message(id_chat, id_message, date, stat, state_date) VALUES(?, ?, ?, ?, ?)"
        parameters = (id_chat, id_message, date, stat, state_date)
        self.execute(sql, parametrs=parameters, commit=True)

    def select_all_message(self):
        sql = "SELECT * FROM Message"
        return self.execute(sql, fetchall=True)

    def count_message(self):
        return self.execute("SELECT COUNT(*) FROM Message;", fetchone=True)

if __name__=="__main__":
    db = Database(path_to_db='app/main.db')
    try:
        db.create_table_message()
    except:
        print('таблица уже создана')
    db.add_message(id_chat=12, id_message=22, date='', stat='[0,0,0]', state_date=0)
    print(db.select_all_message())
    print(db.count_message())