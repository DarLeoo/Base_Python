# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def not_fibonacci(nn):
    if nn == -1:
        return 1
    elif nn == -2:
        return -1
    elif nn != 0:
        return not_fibonacci(nn + 2) - not_fibonacci(nn + 1)


num = 8
nums_fibonacci = []
for el in range(-num, 0):
    nums_fibonacci.append(not_fibonacci(el))
for el in range(num + 1):
    nums_fibonacci.append(fibonacci(el))

print(nums_fibonacci)
