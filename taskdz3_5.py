# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. (Дополнительное)
# решил двумя способами
 
# n = int(input())
# fib1 = fib2 = 1 
# print(0, fib1, fib2, end=' ')
 
# for i in range(2, n):
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')

fib = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(fib+1):    
    print(fibonacci(i), end= ' ')
print()
