"""import random 
the_numb = random.randint(1, 100)
guess = int(input("Назовите число"))
tries=1
while guess != the_numb:
    if guess > the_numb:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Назовите число"))
    tries +=1
print("Вам удалось отгадать число,это в самом деле" ,the_numb)
print("На это вам потребовалось" , tries ,"Попыток")"""

"""import random
 
play = ''
while play != 'n':
    x = input('Загадай число от 1 до 100: ')
    succ = ''
    tmp = [1, 100]
    count = 0
    rnd = random.randint(1, 100)
    while succ != 'y':
        succ = input(f'Может быть это {rnd}? (y/n): ')
        count += 1
        if succ == 'n':
            if input('Больше или меньше (b/m): ') == 'b':
                tmp[0] = rnd
                rnd = (tmp[0]+tmp[1])//2
            else:
                tmp[1] = rnd
                rnd = (tmp[0]+tmp[1])//2
    print(f'Ура! Угадал с {count} попыток!')
    play = input('Сыграем еще раз? (y/n): ')"""

import random
import time
while True:
    hide_num = int(input('загадайте число от 1 до 100\n>>>'))
    if 1 <= hide_num <= 100:
        break
    else:
        print('число вне диапазона!')
a = 1
b = 100
while True:
    num = random.randint(a, b)
    print(f'компьютер: "это число {num}"')
    if num > hide_num:
        b = num - 1
        print('ВЫ: "нет это число меньше"')
    elif num < hide_num:
        a = num + 1
        print('ВЫ: "нет это число больше"')
    else:
        print(f'верно!!!, это число {hide_num}')
        break
    time.sleep(2)
    print('-----------------------')
