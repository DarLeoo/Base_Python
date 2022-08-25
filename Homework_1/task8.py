# 8.Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У
coordinate_x = int(input('Введите координату X: '))
coordinate_y = int(input('Введите координату Y: '))

if coordinate_x > 0 and coordinate_y > 0:
    print('1 четверь')
elif coordinate_x < 0 < coordinate_y:
    print('2 четверь')
elif coordinate_x < 0 and coordinate_y < 0:
    print('3 четверь')
elif coordinate_x > 0 > coordinate_y:
    print('4 четверь')
else:
    if coordinate_x == 0 and coordinate_y > 0 or coordinate_y < 0:
        print('Точка лежит на оси координат Y')
    else:
        print('Точка лежит на оси координат X')

