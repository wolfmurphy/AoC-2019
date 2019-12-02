#!/usr/local/bin/python3
def basicFuelNeeded(m):
    return m//3 - 2
def fuelNeeded(m, total=0):
    newM = basicFuelNeeded(m)
    if newM <= 0:
        return total
    return fuelNeeded(newM, total + newM)
with open("input01.txt",'r') as f:
    #print(sum(list(map(basicFuelNeeded, map(int, f.readlines())))))
    print(sum(list(map(fuelNeeded, map(int, f.readlines())))))
