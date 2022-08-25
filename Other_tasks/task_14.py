# Подсчитать сумму цифр в вещественном числе.
num_one = 1.234
num_one = str(num_one)
num_one = num_one.replace(".", "")
sum_num = 0
for el in num_one:
    sum_num += int(el)

print(sum_num)

real_number = input().replace('.', '')
num_str = list(real_number)
num_int = map(int, num_str)


print(f'Сумма цифр вашего вещественного числа : {sum(num_int)}')
