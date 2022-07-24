# from typing import final
import numpy as np
import math

rotate_arr = np.array(
    [
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0]
    ]
)

file = open('test.obj')
to_file = open('to.obj', 'w')
line = file.readline()
count = 0
while line :
    if count == 0:
        to_file.write(line)

    line = file.readline()
    
    if 'v ' in line:
        split_line = line.split('v ')[1]
        if ' ' in split_line:
            x_str = split_line.split(' ')[0]
            y_str = split_line.split(' ')[1]
            z_str = split_line.split(' ')[2]
            x_num = int(x_str)
            y_num = int(y_str)
            z_num = int(z_str)

            before_array = np.array(
            [
                [x_num, y_num, z_num]
            ]
            )
            final_array = np.dot(before_array, rotate_arr)

            final_str = str(final_array)
            final_str = final_str.replace('[','')
            final_str = final_str.replace(']','')
            
            write_final_str = 'v ' + final_str + '\n'
            write_final_str = write_final_str.replace('  ',' ')
            print(write_final_str)            
            to_file.write(write_final_str)
    else:
        to_file.write(line)
    count = count+1