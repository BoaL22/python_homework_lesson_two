    
    # задача 4 НЕГА необязательная Задайте число. 
    # Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
    # для k = 8 список будет выглядеть так: 
    # [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(num):
    # Фибонначи
    # Список, заполненный числами фибонначи, от 1 до num

    if num in [1, 2]:                       
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

def nega_fibonacci(list):
    # Негафибоначчи
    # Вывод списка, заполненного от -list[-1] до list[-1]

    list_two = list[:]
    i = 0
    while i != len(list):
        list_two.insert(0, -list[i])
        i += 1
    list_two.insert(len(list), 0)
    print(list_two)


list = []
num = int(input('Enter a number:'))

for i in range(1, num + 1):
    list.append(fibonacci(i))

nega_fibonacci(list)
