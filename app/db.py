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
        """ id_chat - номер чата
            id_message - номер сообщения
            date - дата отправки сообщения
            word - отправленное слово
            data_update - дата ответа на сообщение, если было отправлено слово
            status - 1-правильный ответ, 0-неправильный
            del - статус удаленного сообщения, 1-удалено
                                                        """
        sql = """
                CREATE TABLE Message (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_chat INTEGER NOT NULL,
                    id_message INTEGER NOT NULL,
                    date datetime default (datetime('now','localtime')),
                    word TEXT,
                    data_update datetime,
                    status INTEGER,
                    del INTEGER
                );
    """
        self.execute(sql, commit=True)

    def add_message(self, id_chat: int, id_message: int):
        """Добавление записи об отправленном сообщении пользователю
        Args:
            id_chat (int): чат пользователя
            id_message (int): номер сообщения
        """
        sql = "INSERT INTO Message(id_chat, id_message) VALUES(?, ?)"
        parameters = (id_chat, id_message)
        self.execute(sql, parametrs=parameters, commit=True)

    def update(self, id_chat: int, id_message: int, word: str = None, status: bool = None, delete: bool = None):
        """Обновление БД
        Args:
            id_chat (int): чат пользователя
            id_message (int): номер сообщения
            word (str, optional): отправляемое слово
            status (bool, optional): статус, 1-отправлено слово, 0-нет
            delete (bool, optional): факт удаления ссобщения, 1 удалено
        """

        sql = "update Message set data_update = datetime('now', 'localtime')"
        if word:
            sql += ", word = ?"
        if status:
            sql += ", status = ?"
        if delete:
            sql += ", del = ? "
        sql += "where id_chat = ? and id_message = ?;"
        # print(sql)
        parameters = tuple([i for i in (word, status, delete) if i]) + (id_chat, id_message)
        # print(parameters)
        return self.execute(sql, parametrs=parameters, commit=True)

    # def select_all_message(self):
    #     sql = "SELECT * FROM Message"
    #     return self.execute(sql, fetchall=True)

    # def count_message(self):
    #     return self.execute("SELECT COUNT(*) FROM Message;", fetchone=True)

    # def del_message(self):
    #     sql = "DELETE FROM Message where id = 22;"
    #     return self.execute(sql, commit=True)

if __name__=="__main__":
    db = Database()
    try:
        db.create_table_message()
    except:
        print('БД создана')

    # print('таблица уже создана')
    # db.add_message(id_chat=12, id_message=22)
    # db.add_message(id_chat=13, id_message=23)
    # print(db.select_all_message())
    # print(db.count_message())
    # db.updateStatus(id_chat=13, id_message=23, status='Delete')
    # db.dalete()
    # print(db.del_message())
    # print(db.count_message())
    db.update(id_chat=12, id_message=22, delete=True)