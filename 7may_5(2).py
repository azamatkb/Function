#7may_5(2) Представьте Вы работаете в Мобильной Компании и вас попросили...

from random import choices
num = [0, 1, 4, 5, 7, 9]
cod = [444]
cod.insert(0, 0)

def gen_number():
    choose = choices(num, k=6)
    num1 = (cod + choose)
    replced = str(num1).replace(',', '')
    joined = replced.replace(' ', '')
    print(joined)

gen_number()
