#11may_1/2 Напишите функцию которая генерирует 100 рандомных...

import random

def my_func(func):
    def my_func2():
        s = set(func())
        return list(s)
    return my_func2

@my_func

def my_func3():
    c = [random.randint(10,50) for x in range(100)]
    return c
print(my_func3())
