# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
number = int(input('Введите число: '))

def fibb(num):
    res = [0, 1]
    for i in range(2, num + 1 ):
        res.append(res[i - 1] + res[i - 2])
    reversed = res.copy()
    reversed.reverse() 
    reversed = [x*-1 for x in reversed]
    print(reversed[0:-1] + res)



fibb(number)