#7may_4(1) Спросите у пользователя имя файла. Создайте функцию...

def my_file(name):
    with open(name,'w') as file:
        return 'Файл создан'

Name = '/home/azamat/Документы/Python/May_2021/07may_Func/' + input('Введите название файла: ')
n = my_file(Name)
print(n)
