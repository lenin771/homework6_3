# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

list1 = [3, 6, 2, 7, 8, 9]
sum = 0
print('\n Элементы на нечетных позициях', end= ' ')
for i in range(1, len(list1), 2):
    sum = sum + list1[i]
    print(list1[i], end= ', ')
print(f'\n\n Сумма элементов на нечетных позициях {sum} \n')