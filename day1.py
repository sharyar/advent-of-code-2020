list_nums = []
with open('input.txt', 'r') as file:
    for line in file:
        list_nums.append(int(line[:-1]))

from itertools import combinations

for i,j,k in combinations(list_nums, 3):
    if (i+j+k) == 2020:
        print(i*j*k)