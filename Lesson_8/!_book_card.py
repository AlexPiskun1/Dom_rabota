"""
Создать класс BookCard, в классе должны быть:
- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).
Аксессоры реализоваться через property.
"""
from datetime import date

#CURRENT_YEAR = date.today().

class BookCard:
    __author: str
    __title: str
    __year: int

    def __init__(self,__author,__title,__year):
        self.__author = __author
        self.__title = __title
        self.__year = __year
    #def __cmp__(self, other):
       #return (self.__year, other.__year)


    def get_init(self):
        return (f"Автор- {self.__author}\nНазвание книги - {self.__title}\nГод издания - {self.__year}")

    @property
    def author_in(self):
        return self.__author

    @author_in.setter
    def author_in(self,author):
        self.__author = author
        if author == int:
           raise ValueError ("Невверный ввод данных")



    @property
    def title_in(self):
        return self.__title

    @title_in.setter
    def title_in(self,title):
        self.__title = title

    @property
    def year_in(self):
        return self.__year

    @year_in.setter
    def year_in(self, year):
        self.__year = year


    def get_list(self):
        return (f"Автор- {self.__author}. Название книги - {self.__title}. Год издания - {self.__year}")






a1 = BookCard("Vasya", "Don", 2005)
a2 = BookCard("Petya", "Gav", 1998)
a3 = BookCard("Kolya", "Hvost", 2022)

print(a1.get_init())

l=[a1,a2,a3]
for i in l:
    print(i.get_list())

print("-------------")

a1.author_in = "Толстой"
print(a1.author_in)

a1.title_in = "Анна Каренина"
print(a1.title_in)

a1.year_in = 1873
print(a1.year_in)

a2.author_in = "Ден Брайнa"
a2.title_in = "Код Давинча"
a2.year_inК = 2010

print(a2.get_init())

a4 = BookCard(111, 3333, 2022) # Ввожу не str, все равно принимает

print(a4.get_init())