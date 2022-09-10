'''
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''

number = int(input('Введите число: '))
def decimal(number):
    res = ""
    while(number > 0):
        res = str(number % 2) + res
        number = number // 2
    print(res)
decimal(number)