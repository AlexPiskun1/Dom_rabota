from num2t4ru import num2text

print("Добро пожаловать в наш калькулятор")

per1 = float(input("Введите первое число"))
print("Вы ввели: ", per1)
per2 = float(input("Введите второе число"))
print("Вы ввели: ", per2)

zn = input("Введите номер действия\n 1 - Сумма\n 2 - Разность\n 3 - Умножение \n 4 - Деление \n 5 - Возведение в степень")


if zn == "1":
     print("\n_____Ваш Результат_____:",num2text(per1+per2))

elif zn == "2":
    print("\n_____Ваш Результат_____:",num2text(per1-per2))

elif zn == "3":
    print("\n_____Ваш Результат_____:",num2text(per1*per2))

elif zn == "4":
    print("\n_____Ваш Результат_____:",num2text(per1/per2))

elif zn == "5":
    print("\n_____Ваш Результат_____:",num2text(per1**per2))

else:
    print("\n__________Вы ввели некорректные данные__________")


