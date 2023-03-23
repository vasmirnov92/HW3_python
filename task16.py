# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1
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

simmilar = 0
for i in range(len(collection)):
    if collection[i] == find:
        simmilar = simmilar + 1

print(simmilar)
