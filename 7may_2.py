#7may_2 Создайте функцию которая генерирует 10 чисел Фибоначчи

def my_fibonach():
    f1 = 0
    f2 = 1
    n = int(input('Введите необходимое вам колличество чисел: '))
    print ('0,', f2, end=', ')
    while n > 2:
        f1, f2 = f2, f1 + f2
        print (f2, end=', ')
        n -= 1

my_fibonach()



#7may_Расчет числа Фибоначчи
#fib1 = fib2 = 1
#n = input("Номер элемента ряда Фибоначчи: ")
#n = int(n) - 2
#while n > 0:
#    fib1, fib2 = fib2, fib1 + fib2
#    n -= 1
#print("Значение этого элемента:", fib2)
