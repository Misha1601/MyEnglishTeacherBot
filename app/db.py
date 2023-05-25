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

    def add_message(self, id_chat: int, id_message: int, word: str = None, status: bool = None, delete: bool = None):
        """Добавление записи об отправленном сообщении пользователю
        Args:
            id_chat (int): чат пользователя
            id_message (int): номер сообщения
        """
        sql = "INSERT INTO Message(id_chat, id_message, word, status, del) VALUES(?, ?, ?, ?, ?)"
        parameters = (id_chat, id_message, word, status, delete)
        self.execute(sql, parametrs=parameters, commit=True)

    def update(self, id_chat: int, id_message: int, status: bool = None, delete: bool = None):
        """Обновление БД
        Args:
            id_chat (int): чат пользователя
            id_message (int): номер сообщения
            word (str, optional): отправляемое слово
            status (bool, optional): статус, 1-отправлено слово, 0-нет
            delete (bool, optional): удалить сообщение, 1 удалить
        """

        sql = "update Message set data_update = datetime('now', 'localtime'), status = ?, del = ? where id_chat = ? and id_message = ?;"
        # print(sql)
        parameters = (status, delete, id_chat, id_message)
        # print(parameters)
        return self.execute(sql, parametrs=parameters, commit=True)

    def select_del_message(self, id_chat: int):
        sql = "SELECT id_message FROM Message where id_chat = ? and del = 1"
        parameters = (id_chat,)
        return self.execute(sql, parameters, fetchall=True)

    def select_all_chat(self):
        sql = "SELECT DISTINCT id_chat FROM Message where word is not NULL"
        return self.execute(sql, fetchall=True)

    def statistics(self, id_chat: int):
        sql = "SELECT COUNT(*) FROM Message where id_chat = ? and word is not NULL"
        sql1 = "SELECT COUNT(*) FROM Message where id_chat = ? and word is not NULL and status = 1"
        sql2 = "SELECT COUNT(*) FROM Message where id_chat = ? and word is not NULL and status = 0"
        parameters = (id_chat,)
        return (self.execute(sql, parameters, fetchone=True)[0],
                self.execute(sql1, parameters, fetchone=True)[0],
                self.execute(sql2, parameters, fetchone=True)[0])

    def napominanie(self, id_chat: int):
        # sql = "SELECT date, data_update FROM (SELECT MAX(date) FROM Message where id_chat = ? and word is not NULL)"
        # parameters = (id_chat,)
        # date = self.execute(sql, parameters, fetchone=True)
        # if date[1] > date[0]:
        #     return date

        sql = "SELECT MAX(data_update) FROM Message where id_chat = ?"
        parameters = (id_chat,)
        return self.execute(sql, parameters, fetchone=True)[0]

        # else:
        #     sql = "SELECT MAX(date) FROM Message where id_chat = ? and word is not NULL"
        #     parameters = (id_chat,)
        #     return self.execute(sql, parameters, fetchone=True)[0]

    # def select_message(self, id_chat: int, id_message: int):
    #     sql = "SELECT * FROM Message where id_chat = ? and id_message = ?"
    #     parameters = (id_chat, id_message)
    #     return self.execute(sql, parameters, fetchall=True)

    # def count_message(self):
    #     return self.execute("SELECT COUNT(*) FROM Message;", fetchone=True)

    # def del_message(self):
    #     sql = f"DELETE FROM Message where id_chat = {id_chat} and id_message = {id_message} and del = None;"
    #     return self.execute(sql, commit=True)

    # def message_in_db(self, id_chat: int, id_message: int, clear_del_messege: int = 1, word: str = None, del_messege = None, statistics = None):
    #     if not self.select_message(id_chat, id_message):
    #         self.add_message(id_chat=id_chat, id_message=id_message)
    #     if clear_del_messege:
    #         self.select_del_message(id_chat=id_chat)
    #         print('select_del_message')
    #         self.update(id_chat=id_chat, id_message=id_message, delete=0)
    #         print('update')
    #     if word:
    #         self.update(id_chat=id_chat, id_message=id_message, word=word)
    #     if del_messege:
    #         print('del_messege')
    #         self.update(id_chat=id_chat, id_message=id_message, delete=del_messege)
    #     if statistics:
    #         self.update(id_chat=id_chat, id_message=id_message, status=statistics)


if __name__=="__main__":
    db = Database()
    try:
        db.create_table_message()
    except:
        print('БД создана')
        # pass

    # print('таблица уже создана')
    # db.add_message(id_chat=76, id_message=78, delete=1, word='dfdfdf')
    # db.add_message(id_chat=13, id_message=23)
    # print(db.select_del_message(id_chat=56))
    # print(db.count_message())
    # db.updateStatus(id_chat=13, id_message=23, status='Delete')
    # db.dalete()
    # print(db.del_message())
    # print(db.count_message())
    # db.update(id_chat=56, id_message=78, delete=True)
    # db.message_in_db(id_chat= 12, id_message= 44)
    # db.message_in_db(id_chat=471378174, id_message=117, del_messege=1)
    # print(db.napominanie(id_chat=471378174))
    # print(db.select_all_chat())
    # all_id_chat = db.select_all_chat()
    # for i in all_id_chat:
    #     dt = db.napominanie(id_chat=i[0])
    #     if dt != None:
    #         print((datetime.datetime.now() - datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")).total_seconds() > 1000)
        # print(datetime.strptime(db.napominanie(id_chat=i[0]), "%Y-%m-%d %H:%M:%S"))
        # print(type(db.napominanie(id_chat=i[0])))
        # date_str = "2023-05-24 15:30:00"

        # # Преобразование строки в объект datetime.datetime
        # date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")

        # print(date_obj)
        # print(type(date_obj))
    all_id_chat = db.select_all_chat()
    print(all_id_chat)
    for i in all_id_chat:
        print('all_id_chat')
    for i in all_id_chat:
        dt = db.napominanie(id_chat=i[0])
        rasn_sec = int((datetime.datetime.now() - datetime.datetime.strptime(dt, "%Y-%m-%d %H:%M:%S")).total_seconds())
        if (rasn_sec > 1800):
            print(rasn_sec)
    print(int(datetime.datetime.now().timestamp()))
    print(datetime.datetime.now().timestamp())
