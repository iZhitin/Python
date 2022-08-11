# импортируем библиотеку редис для работы с облачной БД
import redis

""" Программа представляет демонстрацию функционала с использованием
облачной БД. В данной программе можно записать, прочитать или удалить контакт в БД """

red = redis.Redis(
    host='redis-19935.c257.us-east-1-3.ec2.cloud.redislabs.com',
    port=19935,
    password='BZdVPJzwWe95APqij8a2RRWa5g9PoJMK'
)

while True:
    choose = input("Введите W чтобы записать номер,"
                   "\nR - чтобы узнать номер по имени или"
                   "\nD - чтобы удалить номер по имени\n")
    if choose == 'W':
        name = input('Ввведите имя контакта\n')
        red.set(name, input('Ввведите его номер\n'))
        print(f'Контакт с именем {name} и номером {red.get(name)} создан!')
        exit = input('Для выхода из программы введите E, введите С - чтобы вернуться в начало программы\n')
        if exit == 'E':
            break
    elif choose == 'R':
        name = input('Ввведите имя контакта\n')
        print(f'Номер контакта {name}: {red.get(name)}!')
        exit = input('Для выхода из программы введите E, введите С - чтобы вернуться в начало программы\n')
        if exit == 'E':
            break
    elif choose == 'D':
        name = input('Ввведите имя контакта\n')
        red.delete(name)
        print(f'Контакт {name} удален!')
        exit = input('Для выхода из программы введите E, введите С - чтобы вернуться в начало программы\n')
        if exit == 'E':
            break
