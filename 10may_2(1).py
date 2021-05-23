#10may_2/1 Написать функцию которая принимает предложение как аргумент...

def my_func(name):
    count = 0
    for i in name:
        count += 1
    return count

name = input('Ваше предложение : ')
print('В вашем предложении -',my_func(name), 'символов')
