# Напишите программу, которая будет преобразовывать 
# десятичное число в двоичное.

number = 15
str_a = ''
while number > 0:
    str_a = str(number % 2) + str_a
    number = number // 2
print(str_a)
