"""
Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты:
- brand - бренд
- model - модель
- issue_year - год выпуска
Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: str

    def __init__(self,brand,model,issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        return f"Бренд: {self.brand} \nМодель: {self.model} \nГод выпуска: {self.issue_year}"


    def receive_call(self,name):
        self.name = name
        print( f"Звонит {self.name}")
        return " "

    def get_info(self):
        return (f"Бренд - {self.brand}, Модель - {self.model}, Год выпуска - {self.issue_year}")



x= Phone("Samsung","Max", 2020)
print(x.get_info())

print("---------------------------")
print(str(x))
print("---------------------------")
a = Phone("IPhon", "12Pro", 2021 )
a.receive_call("Alex")
print(a.get_info())

