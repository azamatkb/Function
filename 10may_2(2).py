#10may_2/2 Создайте функцию, которая принмает тип данных dictionary, но...

def my_func(a):
    tuple1 = []
    tuple2 = []

    for i in a.keys():
        tuple1.append(i)

    print(tuple(tuple1))

    for x in a.values():
        tuple2.append(x)
    print(tuple(tuple2))

my_func({1: 'манты', 2: 'плов', 3: 'лагмат', 4: 'шорпо'})
