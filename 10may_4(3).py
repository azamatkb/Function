#10may_4/3 Напишите функцию, которая спрашивает число N и генерирует...

from random import randrange

def my_func():
    a = int(input('Введите число: '))
    count = 0
    c = []
    while a != count:
        b = randrange(100)
        c.append(b)
        count += 1
    print(c)
my_func()
