
print("Добро пожаловать в наш калькулятор")

per1 = float(input("Введите первое число"))
print("Вы ввели: ", per1)
per2 = float(input("Введите второе число"))
print("Вы ввели: ", per2)

zn = int(input("Введите номер действия\n 1 - Сумма\n 2 - Разность\n 3 - Умножение \n 4 - Деление \n 5 - Возведение в степень"))


while True:

    if zn == 1:
        print("\n_____Ваш Результат_____:",per1+per2)
        break
    if zn == 2:
        print("\n_____Ваш Результат_____:",per1-per2)
        break
    if zn == 3:
        print("\n_____Ваш Результат_____:",per1*per2)
        break
    if zn == 4:
        print("\n_____Ваш Результат_____:",per1/per2)
        break
    if zn == 5:
        print("\n_____Ваш Результат_____:",per1**per2)
        break
    else:
        print("\n__________Вы ввели некорректные данные__________")
        exit()




