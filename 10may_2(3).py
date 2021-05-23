#10may_2/3 Напишите функцию, которая спрашивает у пользователя число и выводит...

number = int(input('Введите число: '))

def my_func(number):
    b = str(number) * number
    return b
print(my_func(number))
