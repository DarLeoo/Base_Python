# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def calk(num_n):
    if num_n == 1:
        return num_n
    else:
        return num_n * calk(num_n - 1)


num_n = int(input("Введите N: "))
generated = []
for e in range(1, num_n + 1):  # диапазон чисел
    generated.append(calk(e))  # добавление значении в список

print(f"Произведения чисел от 1 до {num_n}:  {generated}")