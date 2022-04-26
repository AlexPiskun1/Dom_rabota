
import datetime
import re
import random

import sqlite3


class User():
    __name: str
    __login: str
    __password: str
    is_blocked: bool
    subscription_date: classmethod
    subscription_mode: str


    def __init__(self,__name,__login:str,subscription_date=datetime.date.today()+datetime.timedelta(days=30),
                 subscription_mode = "Free",__password:str="1",is_blocked = False):
        self.__check_name(__name)
        self.__check_login(__login)
        self.change_pass(__password)
        self.is_blocked = is_blocked
        self.subscription_date =subscription_date
        self.subscription_mode = subscription_mode
        self.__save_db()





    def __str__(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        for i in  sql.execute(f"SELECT id, name, login, password, is_blocked, sub_date, sub_mode FROM users_tv WHERE login = '{self.__login}'"):
            print(f"ID - {i[0]}, Имя - {i[1]}, Логин - {i[2]}, Подписка до - {i[5]}, Тип подписки - {i[6]}")



    def get_info(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        for i in sql.execute(
                f"SELECT id, name, login, password, is_blocked, sub_date, sub_mode FROM users_tv WHERE login = '{self.__login}'"):
            return (f"ID - {i[0]}, Имя - {i[1]}, Логин - {i[2]}, Подписка до - {i[5]}, Тип подписки - {i[6]}, Заблокирован - {i[4]}")


    def password_info(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        for i in sql.execute(
                f"SELECT  password FROM users_tv WHERE login = '{self.__login}'"):
            print(f"Ваш пароль - {i[0]}")

    def __save_db(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        sql.execute(f"SELECT login FROM users_tv WHERE login = '{self.__login}'")
        if sql.fetchone() is None:
            sql.execute(
                f"INSERT INTO users_tv (name, login, password, is_blocked, sub_date, sub_mode) VALUES( '{self.__name}', '{self.__login}', '{self.__password}', '{self.is_blocked}','{self.subscription_date}','{self.subscription_mode}')")
            db.commit()


    def bloc(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        self.is_blocked = True
        sql.execute(f"UPDATE users_tv SET is_blocked = 'True' WHERE login = '{self.__login}'")
        db.commit()
        return self.is_blocked


    def bloc_not(self):
        db = sqlite3.connect("server.user.db")
        sql = db.cursor()
        self.is_blocked = False
        sql.execute(f"UPDATE users_tv SET is_blocked = 'Falce' WHERE login = '{self.__login}'")
        db.commit()
        return self.is_blocked

    def __check_name(self,__name):
        name_ok = "^([А-Я]{1}[а-яё]{1,23})$"
        if re.match(name_ok, __name):
             self.__name = __name
             return self.__name
        else:
            print("Неверный ввод имени")

    def __check_login(self,__login):
        login_ok = "^[A-Za-z0-9_-]{6,16}$"
        if re.match(login_ok, __login):
            self.__login = __login
            return self.__login
        else:
            print("Неверный ввод Логина")



    def check_subscr(self,data:str=datetime.date.today()):
        self.data = data
        if self.data == datetime.date.today():
            delta = data - datetime.date.today()
            print(f"Подписка Закончилась, Вид подписки - {self.subscription_mode} ")

        else:
            data1 = datetime.datetime.strptime(str(data), "%d.%m.%Y")
            delta =data1-datetime.datetime.now()
            print(f"Подписка Активна, Вид подписки - {self.subscription_mode}  Осталось - {delta} ")

    def change_pass(self,__password):
        password_ok = "^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{8,}$"
        if __password == "1":
            pas = ''
            for x in range(8):
                pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
            self.__password = pas
            print(f"Ваш пароль - {self.__password} ")
            return self.__password



        else:
            if re.match(password_ok, __password):
                self.__password = __password
                db = sqlite3.connect("server.user.db")
                sql = db.cursor()
                sql.execute(f"UPDATE users_tv SET password = '{self.__password}' WHERE login = '{self.__login}'")
                db.commit()
                print(f"Новый пароль - {self.__password}")
                return self.__password
            else:
                print("Неверный ввод пароля")







user1 = User("Саша","Weld_22", is_blocked= True,)
user2= User("Билл","Bill_debil")
user3 = User("Алекс","Nick_21")
user4 = User("Дима","Dima_21", subscription_mode="Pay")


print(user1.get_info())
print(user2.get_info())



print(user1.get_info())
#user1.bloc()
#print(user1.get_info())
#user1.bloc_not()
#print(user1.get_info())

#user1.check_subscr("20.04.2022")

#user1.password_info()
user1.change_pass("bbvd1Q1q")



print("---------")

user1.password_info()
user2.bloc()
user3.bloc()
user1.bloc_not()
user4.bloc_not()

user2.change_pass("gL0R1qqq")

