
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
        break      

##Task 2
file_1 = file_read.copy()
count_valid = 0
count_invalid = 0
array_valid = []
array_invalid = []
array_invalid_id = []

for i in range(len(file_1)):
    file_1_len = file_1[i].split(',')
    if len(file_1_len[0]) == 9 and file_1_len[0][1:len(file_1_len[0])].isnumeric():
        if len(file_1[i].split(',')) == 26:
            array_valid.append(file_1[i])
            count_valid += 1
        else:
            array_invalid.append(file_1[i])
            count_invalid += 1
    else:
        array_invalid_id.append(file_1[i])
        count_invalid += 1

##Analyzing
print('*'*10,'ANALYZING','*'*10)
if count_invalid !=0:
    print('Invalid line of data: N# is invalid')
    for x in array_invalid_id:
        print(x)
    print('Invalid line of data: does not contain exactly 26 values:')
    for x in array_invalid:
        print(x)
else:
    print('No errors found!')

##Report
print('*'*10,'REPORT','*'*10)        
print('Total valid lines of data:',count_valid)
print('Total invalid lines of data:',count_invalid)



