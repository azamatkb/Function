#7may_1 Создайте функцию которая берет лист делит его пополам и разворачивает...

def revers():
    list_1 = ['name', 'age', '1', '19']
    a = list(reversed(list_1[len(list_1)//2:]))
    b = list(reversed(list_1[:len(list_1)//2]))
    print(b + a)
revers()





#7may_1 - 2 версия Создайте функцию которая берет лист делит его пополам и разворачивает...
#def revers():
#    a = input('Введите слова: ').split()
#    print((list(reversed(a[:(int(len(a)) // 2)]))) + (list(reversed(a[(int(len(a)) // 2)::]))))
#
#revers()
