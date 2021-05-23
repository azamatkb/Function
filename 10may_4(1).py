#10may_4/1 Напишите функцию, которая спрашивает у вас чтобы...

def my_menu():
    name = input('Чтобы вы хотели заказать покушать и выпить?: ')
    with open('/home/azamat/Рабочий стол/menu.txt', 'w') as file:
        file.write(name)
my_menu()
