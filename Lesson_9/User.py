"""
Создать класс User с атрибутами:
Свойства:
	- name - имя - содержит только буквы русского алфавита
	- login - логин - может содержать  только латинские буквы цыфры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия:
					содержит менее шести символов
					содержит строчную букву
					содержит заглавную букву
					содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)
Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату.
						Если дата не передана значит на дату проверки.
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего.
						Пароль должен пройти валидацию.
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.
Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
"""
import datetime
import re
import random


class User():
    name: str
    login: str
    password: str
    is_blocked: bool
    subscription_date: classmethod
    subscription_mode: str


    def __init__(self,name,login:str,subscription_date=datetime.date.today()+datetime.timedelta(days=30),
                 subscription_mode = "Free",password = "1",is_blocked = False):
        name_ok = "^([А-Я]{1}[а-яё]{1,23})$"
        if re.match(name_ok, name):
            self.name = name
        else:
            print("Неверный ввод имени")
        login_ok = "^[A-Za-z0-9_-]{6,16}$"
        if re.match(login_ok, login):
            self.login = login
        else:
            print("Неверный ввод Логина")
        password_ok = "^[A-Za-z0-9_-]{3,5}$"
        if password == "1":
            pas = ''
            for x in range(5):
                pas = pas + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
            self.password = pas
            print(f"Ваш пароль - {self.password} ")


        elif re.match(password_ok, password):
            self.password = password
        else:
            print("Неверный ввод пароля")


        self.is_blocked = is_blocked
        self.subscription_date =subscription_date
        self.subscription_mode = subscription_mode


    def __str__(self):
        print(f"Имя - {self.name}, Логин - {self.login}, Подписка до - {self.subscription_date}, Тип подписки - {self.subscription_mode}")


    def get_info(self):
        return (f"Имя - {self.name}, Логин - {self.login}, Подписка до - {self.subscription_date}, "
                f"Тип подписки - {self.subscription_mode}, Заблокирован - {self.is_blocked}")

    def password_info(self):
        print(f"Ваш пароль {self.password}")

    def bloc(self):
        self.is_blocked = True
        return self.is_blocked


    def bloc_not(self):
        self.is_blocked = False
        return self.is_blocked


    def check_subscr(self,data:str=datetime.date.today()):
        self.data = data
        if self.data == datetime.date.today():
            delta = data - datetime.date.today()
            print(f"Подписка Закончилась, Вид подписки - {self.subscription_mode} ")

        else:
            data1 = datetime.datetime.strptime(str(data), "%d.%m.%Y")
            delta =data1-datetime.datetime.now()
            print(f"Подписка Активна, Вид подписки - {self.subscription_mode}  Осталось - {delta} ")

    def change_pass(self, password:str):

        password_ok = "^[A-Za-z0-9_-]{3,5}$"
        if re.match(password_ok, password):
            self.password = password
        else:
            print("Неверный ввод пароля")
        return self.password



user1 = User("Саша","Weld_22")
user2= User("Билл", "Bill_debil")
print(user2.get_info())

print(user1.get_info())

user1.bloc()
print(user1.get_info())
user1.bloc_not()
print(user1.get_info())

user1.check_subscr("20.04.2022")

user1.password_info()
user1.change_pass("BB22b")
user1.password_info()