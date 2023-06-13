import numpy as np
import random as rnd
import time
from time import gmtime, strftime
TARGET_POROSITY=10
FIELD_SIZE=80

target_pore_cells = TARGET_POROSITY / 100 * FIELD_SIZE * FIELD_SIZE
rand_final = []
random_list = []

random_list_land = np.array((None ,None ,None))

check_list = []
check_field = []
check_list_there = []
list_for_check_calculate = np.array([-1, 0, 1])
field_test = np.zeros((FIELD_SIZE + 2 ,FIELD_SIZE + 2 ,FIELD_SIZE + 2))
initial_cluster_coords = np.array([FIELD_SIZE // 2 + 1 ,FIELD_SIZE // 2 + 1 ,FIELD_SIZE // 2 + 1])
print(initial_cluster_coords)
def print_str(a, b):
    print(str(a), b)
    
#List for check -> +-1
def new_check_list(list_for_check_calculate):
    global check_list
    check_list = np.array([0 ,0 ,0])
    for x in list_for_check_calculate:
        for y in list_for_check_calculate:
            for z in list_for_check_calculate:
            # if ((y!=0)==True and (z!=0)==True)==True:
                for_new = np.array([x ,y, z])
                check_list = np.vstack([check_list, for_new])
    check_list = np.delete(check_list, (0, 5), axis=0)

new_check_list(list_for_check_calculate)
# print_str(check_list,'check_list')

# print_str(field_test,'field_test_first')
#Refresh properties of point (2->1) 
def place_cluster():
    field_test[initial_cluster_coords[0]][initial_cluster_coords[1]][initial_cluster_coords[2]] = 1
place_cluster()
# print_str(field_test,'field_test_second')

#Prepare list for new points
def land_list():
    global random_list_land
    for x in range(FIELD_SIZE):
        for y in range(FIELD_SIZE):
            for z in range(FIELD_SIZE):
                random_list_land = np.vstack([random_list_land, np.array([x+1 ,y+1 ,z+1])])
    random_list_land = random_list_land[1::]             
land_list()

#Refresh List for new points
def random_list_vstack_crds(random_list_land,for_del):
    random_list_land = np.delete(random_list_land, np.where((random_list_land==(for_del)).all(axis=0))[0], axis=0)

#New point on feild from List for nwepoints
def new_point(random_list_land):
    x ,y ,z = rnd.choice(random_list_land)
    # print(x,y)
    field_test[x ,y ,z] = 2
new_point(random_list_land)
# print(field_test)

#List for check_neighbours
def new_check_list():
    global check_list
    check_list = np.array([0 ,0 ,0])
    for x in list_for_check_calculate:
        for y in list_for_check_calculate:
            for z in list_for_check_calculate:
            # if ((y!=0)==True and (z!=0)==True)==True:
                for_new = np.array([x ,y ,z])
                check_list = np.vstack([check_list, for_new])
    check_list = np.delete(check_list, (0, 5), axis=0)
new_check_list()

def check_neighbours():
    global field_test
    global check_list
    global check_field
    global random_list_land

    for i in check_list:
        check_field = np.roll(field_test, (i[0] ,i[1] ,i[2]), axis=(0, 0, 1))
        check_field=field_test*check_field
        x ,y ,z = np.where(check_field == 2)
        field_test[x-i[0] ,y-i[1] ,z-i[2]]=1
        # print_str((x-i[0],y-i[1]),'x-i[0],y-i[1]')
        if x.size>0:
            random_list_vstack_crds(random_list_land,((x-i[0])[0] ,(y-i[1])[0] ,(z-i[2])[0]))

x ,y ,z = np.where(field_test == 2)
lenght_x=len(x)
lest_for_move=[0,1,2,3,4]
print(lenght_x)
print(x,y,z)
import scipy.ndimage as sci_nd

lest_for_move=[0,1,2,3,4]
def moving():
    global field_test
    x ,y ,z = np.where(field_test == 2)
    lenght_x=len(x)
    # print(lenght_x)
    # print(x,y)

    b=rnd.randrange(0,8,step = 1)
    # print(b)
    for_new_moving=np.random.randint(4, size=len(x))
    # print(for_new_moving)
    new_arrray = np.array([x ,y ,z, for_new_moving+1])
    new_arrray = new_arrray.transpose()
    # print(new_arrray)
    first_table_1 = np.zeros_like(field_test)
    first_table_2 = np.zeros_like(field_test)
    first_table_3 = np.zeros_like(field_test)
    first_table_4 = np.zeros_like(field_test)
    first_table_5 = np.zeros_like(field_test)
    first_table_6 = np.zeros_like(field_test)
    first_table_7 = np.zeros_like(field_test)
    first_table_8 = np.zeros_like(field_test)
    for i in range(len(x)):
        # print_str(new_arrray[i][1],'new_arrray[i][1]')
        if new_arrray[i][3] == 1:
            first_table_1[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 2:
            first_table_2[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 3:
            first_table_3[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 4:
            first_table_4[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
            
        if new_arrray[i][3] == 5:
            first_table_5[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 6:
            first_table_6[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 7:
            first_table_7[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
        if new_arrray[i][3] == 8:
            first_table_8[new_arrray[i][0]][new_arrray[i][1]][new_arrray[i][2]] = 2
            
    first_table_1_second=np.roll(first_table_1, (-1,1 ,-1), axis=(0, 0, 1)) 
    first_table_2_second=np.roll(first_table_2, (1,1,-1), axis=(0, 0, 1)) 
    first_table_3_second=np.roll(first_table_3, (1,-1,-1), axis=(0, 0, 1))  
    first_table_4_second=np.roll(first_table_4, (-1,-1,-1), axis=(0, 0, 1))    
            
    first_table_1_second=np.roll(first_table_5, (-1,1,1), axis=(0, 0, 1)) 
    first_table_2_second=np.roll(first_table_6, (1,1,1), axis=(0, 0, 1)) 
    first_table_3_second=np.roll(first_table_7, (1,-1,1), axis=(0, 0, 1))  
    first_table_4_second=np.roll(first_table_8, (-1,-1,1), axis=(0, 0, 1))    
            
    # first_table_1_second=np.roll(first_table_9, (-1,1,1), axis=(0, 1)) 
    # first_table_2_second=np.roll(first_table_10, (1,1,1), axis=(0, 1)) 
    # first_table_3_second=np.roll(first_table_11, (1,-1,1), axis=(0, 1))  
    # first_table_4_second=np.roll(first_table_12, (-1,-1,1), axis=(0, 1))    
            
    first_table=np.add(first_table_1, first_table_2, first_table_3)
    first_table=np.add(first_table_4, first_table_5, first_table_6)
    first_table=np.add(first_table_7, first_table_8)
    x,y,z=np.where(field_test==1)
    # print_str((x,y),'x,y')
    first_table[x ,y ,z]=1
    field_test=first_table

moving()
# print(first_table_4)
# print(first_table_3)
# print(first_table_2)
# print(first_table_1)
# print(first_table)
check_list_time = []
for_target=1
start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
while for_target<target_pore_cells:
    # print('str_0')
    a=len(np.where(field_test == 2)[0])
    # print('str_1')
    while a<5 and for_target<target_pore_cells:
        # print('while_1')
        new_point(random_list_land)
        # print('while_2')
        a=len(np.where(field_test == 2)[0])
        # print('while_3')
        print_str(len(np.where(field_test > 0)[0])/FIELD_SIZE/FIELD_SIZE*100,'%')
    check_neighbours()
    # print('check_neighbours')
    moving()
    # print('moving')
    for_target=len(np.where(field_test >0)[0])
    check_list_time.append([strftime("%Y-%m-%d %H:%M:%S", gmtime()) , len(np.where(field_test > 0)[0])/FIELD_SIZE/FIELD_SIZE*100])
    # print(for_target)
end_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())  
print(start_time)
print(end_time)
# print(field_test)

from pathlib import Path  
import pandas as pd
out_list = []
for x in range(FIELD_SIZE + 2):
    for y in range(FIELD_SIZE + 2):
        for z in range(FIELD_SIZE + 2):
            out_list.append([field_test[x][y][z],x,y,z])
# print(in_out_list)
df = pd.DataFrame(out_list, columns = ['self', 'x', 'y', 'z'])
filepath = Path('C:/Users/natka/Desktop/Кандидатская/for_presentation/np_particle_80.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  
# print_str(end_time-start_time,'difference')

df = pd.DataFrame(check_list_time, columns = ['dt', 'percent'])
filepath = Path('C:/Users/natka/Desktop/Кандидатская/for_presentation/np_time_80.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  
df.to_csv(filepath)  