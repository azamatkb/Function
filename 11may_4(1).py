#11may_4/1 Напишите функцию которая принимает SET и рекурсивно...

set1 = {1,2,3,4,5}

def my_func(c):
    if len(c) > 0:
        c.pop()
        my_func(c)
    else:
        print('Готово!')
        return
my_func(set1)
