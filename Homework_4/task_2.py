# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# вариант через set
num_list = [2, 2, 3, 4, 5, 6, 6, 7]
s = list(set(num_list))
print(s)

# второй вариант
nums_list = [11, 11, 12, 13, 15,15, 17]
nums = []
for el in nums_list:
    if el not in nums:
        nums.append(el)
print(nums)
