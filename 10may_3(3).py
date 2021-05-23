#10may_3/3 Создайте функцию, которая принимает Имя пользователя и его зарплату...

name = input('Ваше имя: ')
salary = input('Ваша зарплата: ')

def my_func(salary2=5000):
    if salary == '':
        print(f'{name} {salary2}')
    else:
        print(f'{name} {salary}')

my_func()
