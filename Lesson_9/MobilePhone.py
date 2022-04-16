
"""
Создать класс MobilePhone на основе класса Phone из пред ДЗ, у которого будут следующие атрибуты:

добавить свойства:
	is_busy - занято - когда кто-то позвонил до момента когда положили трубку должен иметь значение True

переопределить методы:
	- receive_call - теперь не только выводит фразу с именем но и сохраняет время и имя в историю.
						Если в момент вызова трубка еще не положена - вернуть "занято".

добавить методы:
		- receive_sms - принимает имя и текст и сохраяет в историю
		- call_history - возвращает историю звонивших с датой и временем именем и случайным номером телефона формата +375*********
		- sms_histiry - возвращает историю sms (имя/дата/время/текст)
		- сделать метод (положил трубку)
		* метод receive_call принимает номер и если есть в справочнике в историю записать имя
		* положить трубку с возвратом  времени разговора которое тоже в записывается историю


"""
import  datetime
import time
import random

class MobilePhone:
    brand: str
    model: str
    issue_year: str
    is_busy: bool = False
    list1: list
    sms: list
    call_time: str



    def __init__(self,brand,model,issue_year,is_busy= False, list1 = list):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year
        self.is_busy = is_busy
        self.list1 = []
        self.sms = []




    def __str__(self):
        return f"{self.brand} \n{self.model} \n{self.issue_year}\n{self.is_busy}"


    def receive_call(self,name,list1 = list, call_time = 0):
        if self.is_busy is False:
            self.call_time = call_time
            start_call = datetime.datetime.now()
            self.name = name
            self.is_busy = True
            hist1 = datetime.datetime.now()
            hist2 = hist1.strftime("%H:%M:%S %d-%m-%Y")
            kod = ["29", "33", "44", "25"]
            kod_r = random.choice(kod)
            tel_r = random.randrange(1111111, 9999999, 1)
            print( f"Звонит {self.name}, +375({kod_r}){tel_r} Время {hist2}")

            end_call = datetime.datetime.now()
            call_time_1= end_call - start_call
            self.call_time = call_time_1.total_seconds()
            self.list1.append(f"{self.name} +375({kod_r}){tel_r} {hist2} {self.call_time}")
        else:
            print("Абанент занят")



    def call_history(self):
        print(self.list1)

    def end_call(self):
        self.is_busy = False
        print(f"Время разговора {self.call_time}")
        return self.is_busy


    def get_info(self):
        return (f"Бренд - {self.brand}, Модель - {self.model}, Год выпуска - {self.issue_year}, Разговор идет - {self.is_busy}")

    def receive_sms(self,name,text):
        self.name = name
        self.text = text
        hist1 = datetime.datetime.now()
        hist2 = hist1.strftime("%H:%M:%S %d-%m-%Y")
        self.sms.append(f"{self.name}  {hist2}  {self.text}")
        return self.sms

    def sms_histiry(self):
        print(self.sms)

a1= MobilePhone("Samsung","Max", 2020)
a2 = MobilePhone("IPhon", "12Pro", 2021 )


print(a2.__str__())
a2.receive_call("Alex")
time.sleep(1)
a2.receive_call("Dima")
time.sleep(1)
a2.end_call()
a2.receive_call("Vova")
time.sleep(1)
a2.receive_call("Marina")
a2.end_call()
a2.receive_call("Pedro")

a2.call_history()

a2.receive_sms("Володя", "Сообщение 1")
a2.receive_sms("Инокентий", "Сообщение 2")
a2.receive_sms("Сергей", "Сообщение 3")
a2.sms_histiry()

print("---------")
