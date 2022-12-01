# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов. (Дополнительное)


fib = int(input())

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(fib, 0, -1):    
    print(fibonacci(i) * ((-1)**(i+1)), end= ' ')
for i in range(fib+1):    
    print(fibonacci(i), end= ' ')
print()
