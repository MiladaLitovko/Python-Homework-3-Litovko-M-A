'''

Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
def difference():
    list = [1.1, 1.2, 3.1, 5, 10.01]
    newlist = []
    max = 0
    min = 0
    for i in range(len(list)):
        list[i] = list[i] % 1
        newlist.append(list[i])
    for index in range(len(newlist)):
        if newlist[index] > newlist[index + 1]:
            max = newlist[index]
        else:
            max = newlist[index + 1]
    for index in range(len(newlist)):
        if newlist[index] > newlist[index + 1]:
            min = newlist[index + 1]
        else:
            min = newlist[index]
    dif = max - min
    return(dif)

print(difference())