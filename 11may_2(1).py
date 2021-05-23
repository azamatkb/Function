#11may_2/1 Написать lambda которая получает сколько дней ПРОШЛО...

import datetime 
now = datetime.datetime.now() - datetime.datetime(2021,1,1)
days = int(str(now).split()[0])
c = lambda d:365 - d
print(f'До Нового Года осталось:',c(days),'дн')
