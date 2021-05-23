#11may_3/1 Напишите программу которая выводит только нечётные...

def my_func(c):
    if c % 2:
        print(c)
    if c > 992:
        return
    my_func(c + 1)
my_func(1)
