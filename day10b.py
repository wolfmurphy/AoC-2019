#!/usr/local/bin/python3
import math
import numpy
debug = True
def seq(first, last):
    if last<first:
        return seq(last, first)[::-1]
    if last == first:
        return [first]
    return [first] + seq(first+1, last)
def dprint(*argv):
    if not debug:
        return
    print(" ".join(map(str,argv)))

def gcd(x, y):
    while(y): 
       x, y = y, x % y
    return x
def lTerm(x,y):
    gcdVal = abs(gcd(x,y))
    return x // gcdVal, y // gcdVal
def circCmp(a, b):
    if a[0] == b[0]:
        if a[2] == b[2] and a[3] == b[3]:
            return a[4] < b[4]
        if a[1]:
            return a[2]*b[3] < a[3]*b[2]
        else:
            return a[2]*b[3] > a[3]*b[2]
    else:
        return a[0] < b[0]
def quad(x,y):
    i = 3*numpy.sign(x) +  numpy.sign(y) + 4
    quadrant = [4,4,3,1,None,3,1,2,2]
    invert = [False, False, True, True, None, True, True, False, False]
    return quadrant[i], invert[i], abs(x), abs(y)
def mergesort(lis, func):
    def mergetwo(a, b):
        newList = []
        while True:
            if len(a) == 0:
                return newList+b
            if len(b) == 0:
                return newList+a
            if func(a[0], b[0]):
                newList.append(a.pop(0))
            else:
                newList.append(b.pop(0))
    curlists = []
    for v in lis:
        curlists.append([v])
    while len(curlists) > 1:
        newLis = []
        while len(curlists) > 0:
            if len(curlists) == 1:
                newLis.append(curlists.pop(0))
            else:
                a = curlists.pop(0)
                b = curlists.pop(0)
                newLis.append(mergetwo(a, b))
        curlists = newLis
    return curlists.pop(0)

baseX, baseY = 26, 29

with open("day10.txt",'r') as f:
    data = f.readlines()

    targets = []
    maxY = len(data) - 1
    maxX = len(data[0]) - 2
    for y in range(maxY+1):
        lin = data[y]
        for x in range(maxX+1):
            if lin[x] == '#':
                if baseX==x and baseY == y:
                    pass
                else:
                    deltaX = x - baseX
                    deltaY = y - baseY
                    angX, angY = lTerm(deltaX, deltaY)
                    q = quad(angX,angY)
                    targets.append([q[0], q[1], q[2], q[3], abs(deltaX) + abs(deltaY), angX, angY, x, y])

    lis, targets = mergesort(targets, circCmp), []
    for target in  lis: # strip stuff just used for sorting
        targets.append(target[5:9])

    zapped = 0
    newList = []
    oldAngX = None
    oldAngY = None
    while True:
        if len(targets) == 0:
            targets, newList = newList, []
        target = targets.pop(0)
        if target[0] == oldAngX and target[1] == oldAngY :
            newList.append(target)
            continue
        zapped += 1
        if zapped == 200:
            print(100*target[2]+target[3])
            exit(0)
        oldAngX = target[0]
        oldAngY = target[1]
