"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(l: list):
    l2=[]
    for i in l:
        if l2.count(i) > 0:
            print("Yes")
        else:
            l2.append(i)
            print("No")
    print(l2)


a = [1,2,1,4,3,2,1]
yes_or_no(a)