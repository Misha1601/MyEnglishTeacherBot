import sqlite3
import datetime

class Database:
    def __init__(self, path_to_db='main_db.db'):
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
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_chat INTEGER NOT NULL,
                    id_message INTEGER NOT NULL,
                    date datetime default (datetime('now','localtime')),
                    word TEXT,
                    data_update datetime,
                    status TEXT,
                    voprosotvet INTEGER
                );
    """
        self.execute(sql, commit=True)

    def add_message(self, id_chat: int, id_message: int):
        sql = "INSERT INTO Message(id_chat, id_message) VALUES(?, ?)"
        parameters = (id_chat, id_message)
        self.execute(sql, parametrs=parameters, commit=True)

    def select_all_message(self):
        sql = "SELECT * FROM Message"
        return self.execute(sql, fetchall=True)

    def count_message(self):
        return self.execute("SELECT COUNT(*) FROM Message;", fetchone=True)

    def updateStatus(self, id_chat: int, id_message: int, status: str):
        sql = "update Message set status = ?, data_update = datetime('now', 'localtime') where id_message = ? and id_chat = ?;"
        parameters = (status, id_message, id_chat)
        return self.execute(sql, parametrs=parameters, commit=True)

    def dalete(self):
        sql = "DELETE FROM Message;"
        return self.execute(sql, commit=True)

if __name__=="__main__":
    db = Database()
    try:
        db.create_table_message()
    except:
        print('БД создана')

    # print('таблица уже создана')
    db.add_message(id_chat=12, id_message=22)
    db.add_message(id_chat=13, id_message=23)
    # print(db.select_all_message())
    # print(db.count_message())
    # db.updateStatus(id_chat=13, id_message=23, status='Dalete')
    # db.dalete()