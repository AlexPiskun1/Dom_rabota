"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.

Номер значения нужно проверить

Пример:

fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""

def fibonacci(n1:int):
    a,b =1,1
    if n1 == 0:
        raise ValueError('Введите значение больше 1')
    else:
        for i in range(n1):
            yield a
            a,b = b,a+b




n=5
fb=fibonacci(n)

print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))


