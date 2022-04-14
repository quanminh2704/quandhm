
import pandas as pd
import numpy as np
##Task 1
direction = "C:\\Users\\DELL\\Desktop\\FUNIX\\DSP301x_asm2_quandhmFX16121@funix.edu.vn\\Data Files\\"
file_name_check = True
while file_name_check:
    file_name = input('Enter file name:\n')
    file_name_record = direction + file_name + '.txt'
    try:
        with open(file_name_record) as readfile:
            file_read = readfile.readlines()
    except IOError:
        print('The file cannot be found.')
        file_name_check = False
    else:
        print('Successfully opened', file_name + '.txt')
        print('*'*10,'ANALYZING','*'*10)
        print('No errors found')
        break    
