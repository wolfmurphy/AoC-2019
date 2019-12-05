#!/usr/local/bin/python3
import sys
count = 0
for i in range(183564,657474):
    lis = [char for char in str(i)]
    if (lis[0] > lis[1]) or  (lis[1] > lis[2]) or (lis[2] > lis[3]) or (lis[3] > lis[4]) or (lis[4] > lis[5]):
        continue
    elif ((lis[0] == lis[1]) and (lis[1] != lis[2])) or \
            ((lis[1] == lis[2]) and (lis[0] != lis[1]) and (lis[2] != lis[3])) or \
            ((lis[2] == lis[3]) and (lis[1] != lis[2]) and (lis[3] != lis[4])) or \
            ((lis[3] == lis[4]) and (lis[2] != lis[3]) and (lis[4] != lis[5])) or \
            ((lis[4] == lis[5]) and (lis[3] != lis[4])): 
        count = count + 1
print count

