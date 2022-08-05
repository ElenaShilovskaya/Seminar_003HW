# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов

def fibo(n):
    fib = []
    a, b = 1, 1
    for i in range(n):
        fib.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fib.insert(0, a)
        a, b = b, a - b
    return fib

n = 8
fib = fibo(n)
print(fibo(n))   
