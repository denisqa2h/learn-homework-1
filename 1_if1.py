"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    age = int(input())
    if 3<=age<=5:
        return('Sadik')
    elif 6<=age<=16:
        return('Shkola')
    elif 16<=age<=22:
        return('VUZ')
    elif 22<=age<=60:
        return('Rabotyaga')
    else:
        print('Ты что-то путаешь, давай заново')
        return main()
        
print(f'Твоё предназначение: {main()}')

