# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a = [1, 10, 3, 4, 5, 6, 7, 8]
sum = 0
for i in range(1, len(a), 2):
    sum +=a[i]
print(sum)