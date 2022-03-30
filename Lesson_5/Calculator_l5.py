

n= 0

while True:
    a = input("Введите действие через пробел").split()
    n +=1
    if a[0] == "стоп":
        break
    elif a[1] == "+":
        print("Ответ", float(a[0])+float(a[2]))
        print("Номера вашей операции", n)
    elif a[1] == "-":
        print("Ответ", float(a[0])-float(a[2]))
        print("Номера вашей операции", n)
    elif a[1] == "*":
        print("Ответ", float(a[0])*float(a[2]))
        print("Номера вашей операции", n)
    elif a[1] == "/":
        if a[2] == "0":
            print("На ноль не делится")
        else:
            print("Ответ", float(a[0]) / float(a[2]))
            print("Номера вашей операции", n)
    elif a[1] == "**":
        print("Ответ", float(a[0])**float(a[2]))
        print("Номера вашей операции", n)
    else:
        print("Некоректный ввод данных")
        print("Номера вашей операции",n)
