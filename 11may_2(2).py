#11may_2/2 Напишите функцию которая спрашивает у пользователя...

import random
def shifrovka(func):
    def inner():
        alfavit_EU =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
        smeshenie = random.randint(0,33)
        message = func().upper()
        itog = ''
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
        return itog.lower()
    return inner
@shifrovka
def logpass():
    login = input('Введите логин : ')
    password = input('Введите пароль : ')
    return f"{login} - {password}"
print(logpass())
