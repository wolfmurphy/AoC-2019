#!/usr/local/bin/python3
debug = False
def seq(first, last):
    if last<first:
        return seq(last, first)[::-1]
    if last == first:
        return [first]
    return [first] + seq(first+1, last)
def dprint(*argv):
    if not debug:
        return
    print( " ".join(map(str,argv)))
def mkMemory(line):
    memory = list(map(int, line.split(",")))
    return {i: memory[i] for i in range(0, len(memory))}

def getIndex(x,y):
    return str(x)+'-'+str(y)
def gcd(x, y):
    while(y): 
       x, y = y, x % y
    return x
def lTerm(x,y):
    gcdVal = abs(gcd(x,y))
    return x // gcdVal, y // gcdVal
with open("day10.txt",'r') as f:
    data = f.readlines()
    asterisks = {}
    maxY = len(data) - 1
    maxX = len(data[0]) - 2
    for y in range(maxY+1):
        lin = data[y]
        for x in range(maxX+1):
            if lin[x] == '#':
                index = getIndex(x,y)
                asterisks[index] = [x, y, True]
    indexes = asterisks.keys()
    numAsterisks = len(indexes)
    maxAsterisks = 0
    maxLoc = None
    for index in indexes:
        baseX = asterisks[index][0]
        baseY = asterisks[index][1]
        for ast in indexes:
            asterisks[ast][2] = True
        for ast in indexes:
            if index == ast:
                asterisks[index][2] = False
            else:
                deltaX = asterisks[ast][0] - baseX
                deltaY = asterisks[ast][1] - baseY
                deltaX, deltaY = lTerm(deltaX, deltaY)
                x,y = asterisks[ast][0], asterisks[ast][1] 
                while True:
                    x += deltaX
                    y += deltaY
                    if x<0 or x>maxX or y<0 or y>maxY:
                        break
                    i = getIndex(x,y)
                    if None != asterisks.get(i):
                        asterisks[i][2] = False
        count = 0
        for i in indexes:
            if asterisks[i][2] == True:
                count += 1
        if count > maxAsterisks:
            maxAsterisks = count
            maxLoc = index
    print( maxAsterisks, maxLoc)
