
    # Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
    # решкой, а некоторые – гербом. Определите минимальное число
    # монеток, которые нужно перевернуть, чтобы все монетки были
    # повернуты вверх одной и той же стороной. Выведите минимальное
    # количество монет, которые нужно перевернуть.

    # 5 -> 1 0 1 1 0
    # 2

import random

n = int(input('Enter N: '))
list = [random.randint(0, 1) for i in range(n)]

sum = 0
for i in list:
    if i == 0: sum +=1

print(list)
print(f'{sum}')