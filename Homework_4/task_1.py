# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n_i = int(input('Введите натуральное число N: '))
n_list = []
n_2 = 2

while n_2 * n_2 <= n_i:
    if n_i % n_2 == 0:
        n_list.append(n_2)
        n_i //= n_2
    else:
        n_2 += 1
n_list.append(n_i)
print(n_list)

