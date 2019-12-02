#!/usr/local/bin/python3
def fuelNeeded(m):
    return m//3 - 2
with open("input01.txt",'r') as f:
    print(sum(list(map(fuelNeeded, map(int, f.readlines())))))
