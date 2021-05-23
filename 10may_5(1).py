#10may_5/1 Создайте функцию, которая принимает слово ...

def my_func():
    name = input('Название файла: ')
    c = open(name, 'w')
    c.close()

my_func()
