# 1.По двум заданным числам проверить является ли одно квадратом второго
import math


num_one = int(input('Введите первое число: '))
num_two = int(input('Введите второе число: '))
if num_one == math.sqrt(num_two):
   print(f'число {num_one} является квадратом числа {num_two} ')
elif num_two == math.sqrt(num_one):
   print(f'число {num_two} является квадратом числа {num_one} ')
else:
   print('Ни одно число не является квадратом другого числа')


#2. Найти максимальное из пяти чисел
a = [11, 23, 454, 54, 6]
print(max(a))

#3.Вывести на экран числа от -N до N
num_n = int(input('Введите любое число: '))
for i in range(-abs(num_n), num_n + 1, 1):
   print(i)


#4. Показать первую цифру дробной части числа
num_x = float(input("Введите число, с цифрами после запятой : "))
print(int(num_x * 10) % 10)
