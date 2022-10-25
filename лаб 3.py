points = 15

import csv
with open('предметы.csv') as csvfile:
    file_reader = csv.reader(csvfile, delimiter = ';')
    objects = [row for row in file_reader][1:]
print(objects)
from operator import itemgetter
values = []
for i in range(len(objects)):
    value = int(objects[i][3]) / int(objects[i][2][0])
    values.append([value, i])
values = sorted(values, key = itemgetter(0))[::-1]


array = [], []
max_values = []
k = 0
i = 0
while k < 8:
    max_values.append(values[i])
    index = values[i][1]
    i += 1
    points += int(objects[index][3])
    k += int(objects[index][2][0])
    if int(objects[index][2][0]) == 1:
        array[0].append(objects[index][1])

    if int(objects[index][2][0]) == 2:
        array[1].append(objects[index][1])
        array[1].append(objects[index][1])

# Находим среди подобранных объектов с высоким рейтингом самый минимальный, чтобы затем проверить сможем ли мы убрать его так, \
# чтобы количество очков оставалось положительным
min_from_max = 1000
if int(objects[max_values[-1][1]][2][0]) == 1:
    min_from_max = int(objects[max_values[-1][1]][3])
else:
    for i in range(len(max_values)):
        if int(objects[max_values[i][1]][2][0]) == 1:
            min_from_max = min(min_from_max, int(objects[max_values[i][1]][2][0]))


if points > 0:
    for x in range(i, len(values)):
        index = values[x][1]
        points -= int(objects[index][3])
    for row in array:
        for i in row:
            print(i, end = ' ')
        print('\n')
    print(f'Итоговые очки выживания: ' + str(points))
else:
    print("Нет решений")


# для 7 ячеек
if (points - 2*min_from_max) > 0:
    print(f'Для 7 ячеек количество очков выживаня:' + str(points - 2*min_from_max))
else:
    print('Для 7 ячеек нет решений')







