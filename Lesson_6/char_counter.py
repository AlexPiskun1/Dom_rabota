"""
Написать функцию count_char, которая принимает строковое значение STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
    'буква': количество-вхождений-в-строку
}

например: {
    'p': 2,
    'y': 1,
    ...
}

Нельзя пользоваться collections.Counter!
"""


def count_char(s: str):
    res = {}
    for i in s:
        if i in res.keys():
            res[i] +=1
        else:
            res[i] = 1
    return res
STR_VAL = 'python is the fastest-growing major programming language'

print(count_char(STR_VAL))


