import sqlite3

class Database:
    def __init__(self, path_to_db='main.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parametrs: tuple = None, fetchone = False,
                fetchall = False, commit = False):
        connection = self.connection
        cursor =connection.cursor()
        data = None
        cursor.execute(sql, parametrs)

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchone()

        connection.close()
        return data

    def create_table_message(self):
        sql = """
                CREATE TABLE Message (
                    id int NOT NULL,
                    id_chat int NOT NULL,
                    id_message int NOT NULL,
                    PRIMARY KEY (id)
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