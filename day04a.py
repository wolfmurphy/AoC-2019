#!/usr/local/bin/python3
import sys
count = 0
def isIncreasing(lis,start,end):
    for i in range(start,end):
        if lis[i] > lis[i+1]:
            return False
    return True
def hasRepeated(lis,start,end):
    for i in range(start,end):
        if lis[i] == lis[i+1]:
            return True
    return False
for i in range(183564,657474):
    lis =  list(str(i))
    start, end = 0, len(lis) - 1
    if isIncreasing(lis,start,end) and hasRepeated(lis,start,end):
        count = count + 1
print count
