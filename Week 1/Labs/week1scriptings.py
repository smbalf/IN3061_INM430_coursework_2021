import csv
import os
import numpy as np
import matplotlib.pyplot as plt


os.system('cls')

# Start of exercise one 

years_list = []
row_count = 0
e_pop_num_list = [] 
with open('TB_burden_countries_2014-09-29.csv', 'r') as csvfile:
    filereader = csv.reader(csvfile)
    headers = next(filereader) # skip header 
    for row in filereader:
        key = row[5]
        value = row[6]
        years_list.append([key,value])
        e_pop_num_list.append(value)
        row_count += 1

sum_e_pop_num = 0

for value in e_pop_num_list:
    sum_e_pop_num += int(value)

sum_1999 = 0
sum_2011 = 0
for year in years_list:
    if year[0] == '1999':
        sum_1999 += int(year[1])
    elif year[0] == '2011':
        sum_2011 += int(year[1])

mean_e_pop_num = round(sum_e_pop_num / row_count, 0)
mean_1999 = round(sum_1999 / row_count, 0)
mean_2011 = round(sum_2011/ row_count, 0)

print(f'rows in file = {row_count}')
print(f'e_pop_num mean: {mean_e_pop_num}')
print(f'e_pop_num mean 1999: {mean_1999} -- e_pop_num mean 2011: {mean_2011}')

# Start of exercise two

array_5_15 = np.arange(5,16)
space = 23 / 7
array_7_23 = np.arange(0,23,space)

array_uniform = np.random.uniform(-1, 1, size=100)
plt.hist(array_uniform)
plt.show()

array_one = np.random.rand(5 ,2)
array_two = np.random.rand(5, 2)

sum_sq = np.sum(np.square(array_one - array_two))

print(np.sqrt(sum_sq))