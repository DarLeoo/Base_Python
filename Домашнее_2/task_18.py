#  Реализовать алгоритм перемешивания списка.
import random

list_one = [1, 4, 5, 776, 134, 5456, 324, 5435]
list_two = []
num_iter = len(list_one)
num_index = 0
while num_iter > 0:
    el = list_one[num_index - 1]
    list_two.append(el)
    num_iter -= 1
    num_index -= 1
print(list_two)
# здесь сделал только реверс, без math здесь непонятно как делать

list_three = [1, 4, 5, 776, 134, 5456, 324, 5435]
random.shuffle(list_three)
print(list_three)

# решение с random