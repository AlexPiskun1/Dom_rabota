from num2t4ru import num2text

print("Добро пожаловать в наш калькулятор")

per1 = float(input("Введите первое число"))
print("Вы ввели: ", per1)
per2 = float(input("Введите второе число"))
print("Вы ввели: ", per2)

per3 = input("Введите операцию")

if per3 == "-":
    print("__________Ваш результат__________:",num2text(per1-per2))
elif per3 == "+":
    print("__________Ваш результат__________:",num2text(per1+per2))
elif per3 == "*":
    print("__________Ваш результат__________:",num2text(per1*per2))
elif per3 == "/":
    print("__________Ваш результат__________:",num2text(per1/per2))
else:
    print("__________Вы ввели неверную операцию__________")