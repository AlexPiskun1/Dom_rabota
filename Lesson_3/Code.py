#age = input("Сколько тебе лет")

#print(f"У нас разница в {abs(int(age) -25)} лет")
#print(type(age))


#a = "22.5"
#print(int(a)) из str с запятой нельзя сделать int
print(0.1+0.1+0.1)

text = """
Hello
how
do
you
fell
"""
print(text)

print("How do you feel\n" * 7) # Умнажает строку 7 раз

text1= "Mazafaca"
print(text1[4:])
print(text1[4:-1])
print(len(text))
print(len(text1))

name = "Alex"
age = 33

print("Меня зовут {}. Мне {} лет".format(name,age))
print(f"Меня зовут {name}. Мне {age} лет")

numbers = "one,two,three"
print(numbers.split(","))

print("12345".find("3"))
print("123453".rfind("3"))
print("123453".count("3"))
print("Hello World".replace("Hello", "Goodbye"))

text2= "Hello WORLD"
print(text2.upper())
print(text2.lower())
print(text2.title())