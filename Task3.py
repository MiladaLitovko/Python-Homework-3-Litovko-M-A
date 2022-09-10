# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

def difference():
    list = [1.1, 1.2, 3.1, 5, 10.01]
    for i in range(len(list)):
        list[i] = list[i] % 1
    maximum = max(list)
    minimum = min(list)
    dif = maximum - minimum
    dif = str(dif)
    return(dif[0:4]) 

print(difference())