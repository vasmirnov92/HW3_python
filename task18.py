# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

print('Введите количество чисел')
n = input()
n = int(n)
# print(type(n))

collection = []
for i in range(n):
    collection.append(randint(1, 10))
#     collection.append(i)          # вариант с выводом подряд чисел, как в примере
# collection.pop(0)
print(collection)

print('Введите искомое число')
find = input()
find = int(find)
# print(type(find))

lowestDifference = abs(collection[0] - find)
lowestIndex = 0
for i in range(len(collection)):
    difference = abs(collection[i] - find)
    if difference < lowestDifference:
        lowestDifference = difference
        lowestIndex = i

print('Cамый близкий по величине элемент к заданному числу:')
print(collection[lowestIndex])