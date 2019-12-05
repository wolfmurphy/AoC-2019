#!/usr/local/bin/python3
import sys
count = 0
def isIncreasing(lis):
    for i in range(1,6):
        if lis[i] > lis[i+1]:
            return False
    return True
def hasRepeated(L):
    for i in range(1,6):
        if (L[i] == L[i+1]) and (L[i-1] != L[i]) and (L[i+1] != L[i+2]):
            return True
    return False
for i in range(183564,657474):
    lis = [char for char in ('-'+str(i)+'-')]
    if isIncreasing(lis) and hasRepeated(lis):
        count = count + 1
print count
