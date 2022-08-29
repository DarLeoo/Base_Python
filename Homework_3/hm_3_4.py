# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


def find_num(number):
    if number >= 1:
        if int(number) % 2 == 0:
            num_list.append(0)
        else:
            num_list.append(1)
        return find_num(number / 2)
    else:
        return ''.join(map(str, reversed(num_list)))


number = int(input('Введите число: '))
num_list = []
print(find_num(number))




