import pyopencl as cl
import numpy as np
import random as rnd

STANDART_SIZE = 7
size_to_check = STANDART_SIZE - 2
TARGET_POROSITY = size_to_check ** 3 *0.2

len_x, width, height = STANDART_SIZE, STANDART_SIZE, STANDART_SIZE
next_x, next_y, next_z= size_to_check, size_to_check, size_to_check

list_index_one_line = [i for i in range(0,STANDART_SIZE, 1)]
print(f"list_index_one_line: {list_index_one_line}")

check_list = [-1, 0, 1]

def convert_3d_to_1d(x, y, z, width, height):
    return x + width * (y + height * z)


test_field = np.zeros(len_x * width * height)
m_x, m_y, m_z = len_x // 2, width // 2, height // 2

middle_index =  convert_3d_to_1d(m_x, m_y, m_z, width, height)
print(f"middle_index: {middle_index}")
test_field[middle_index] = 1

list_not_busy_index = [i for i in range(0, len_x * width * height, 1)]
list_not_busy_index.remove(middle_index)
print(f"len_not_busy: {len(list_not_busy_index)}, {list_not_busy_index}")
print(test_field)
print(np.where(test_field == 1))

list_to_remove = []

for x in list_index_one_line:
    for y in list_index_one_line:
        for z in list_index_one_line:
            if x == 0 or y == 0 or z == 0 or x == len_x - 1 or  y == width - 1 or z == height - 1:
                index_for_remove =  convert_3d_to_1d(x, y, z, width, height)
                # if index_for_remove not in list_to_remove:
                list_to_remove.append(index_for_remove)
# list_to_remove.remove(middle_index)
list.sort(list_to_remove)
print(f"list_to_remove:      {len(list_to_remove)}, {list_to_remove}")
print(f"list_not_busy_index: {len(list_not_busy_index)}, {list_not_busy_index}")
for i in list_to_remove:
    # print(i)
    list_not_busy_index.remove(i)
print(f"list_not_busy_index_after: {len(list_not_busy_index)}, {list_not_busy_index}")


def direction_random_choice(check_list_direction = check_list):
    return rnd.choice(check_list_direction)


def new_point_random_choice(check_list_points = list_not_busy_index):
    test_field[rnd.choice(list_not_busy_index)] = 2


def check_neghbour(field_check_neighbour = test_field):
    points_to_check_1 = np.where(field_check_neighbour == 1)[0]
    if len(points_to_check_1) > 0:
        for i in points_to_check_1:
            z = int(i / (width * height))
            y = int((i - z * width * height) / width)
            x = int(i - width * (y + height * z))
            for a in check_list:
                for b in check_list:
                    for c in check_list:
                        check_coords = convert_3d_to_1d(x + a, y + b, z + c, width, height)
                        if field_check_neighbour[check_coords] == 2:
                            field_check_neighbour[check_coords] = 1
                            list_not_busy_index.remove(check_coords)
                                    
                                    
def move_points(field_for_move = test_field):
    points_to_move = np.where(field_for_move == 2)[0]
    if len(points_to_move) > 0:
        for i in points_to_move:
            z = int(i / (width * height))
            y = int((i - z * width * height) / width)
            x = int(i - width * (y + height * z))
            
            field_for_move[convert_3d_to_1d(x, y, z, width, height)] = 0
            new_coords = []
            
            for p in ([x, len_x], [y, width] ,[z, height]):
                a = 0
                while a == 0:
                    p_1 = direction_random_choice()
                    if (p[0] + p_1) > 0 and (p[0] + p_1) < p[1]:
                        p[0] += p_1
                        new_coords.append(p[0])
                        a = 1
                    new_coords.append(p[0])
            field_for_move[convert_3d_to_1d(new_coords[0], new_coords[1], new_coords[2], width, height)] = 2
            
counter = 1
t_c = 0

print(counter)
while counter < TARGET_POROSITY:
    new_point_random_choice()
    check_neghbour()
    move_points()
    t_c += 1
    counter = len(np.where(test_field == 1)[0])
    # if t_c % 1000 == 0:
        # print(counter)
        # print(test_field)
