import decimal

from num2t4ru import num2text
from num2t4ru import decimal2text

int_units = ((u'целых', u'целых', u'целых'), 'm')
exp_units = ((u'сотых', u'сотых', u'сотых'), 'f')

int_units = ((u'целых', u'целых', u'целых'), 'm')
exp_units = ((u'сотых', u'сотых', u'сотых'), 'f')
decimal2text(decimal.Decimal(),
    int_units=int_units,
    exp_units=exp_units)


print("Добро пожаловать в наш калькулятор")

per1 = float(input("Введите первое число"))
print("Вы ввели: ", per1)
per2 = float(input("Введите второе число"))
print("Вы ввели: ", per2)

zn = input("Введите номер действия\n 1 - Сумма\n 2 - Разность\n 3 - Умножение \n 4 - Деление \n 5 - Возведение в степень")


if zn == "1":
    print("\n_____Ваш Результат_____:",decimal2text( (per1+per2),
    places=2,
    int_units=int_units,
    exp_units=exp_units))

elif zn == "2":
    print("\n_____Ваш Результат_____:",decimal2text( (per1-per2),
    places=2,
    int_units=int_units,
    exp_units=exp_units))
elif zn == "3":
    print("\n_____Ваш Результат_____:", decimal2text((per1 * per2),
    places=2,
    int_units=int_units,
    exp_units=exp_units))
elif zn == "4":
    if per2 == 0:
        print("\n_____На ноль не делится_____")
    else:
        print("\n_____Ваш Результат_____:", decimal2text((per1 / per2),
        places=2,
        int_units=int_units,
        exp_units=exp_units))

elif zn == "5":
    print("\n_____Ваш Результат_____:", decimal2text((per1 ** per2),
        places=2,
        int_units=int_units,
        exp_units=exp_units))

else:
    print("\n__________Вы ввели некорректные данные__________")


