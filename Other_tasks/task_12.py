# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num_n = int(input("Введите n: "))
d = {a: (3 * a + 1) for a in range(1, num_n + 1)}
print(d)