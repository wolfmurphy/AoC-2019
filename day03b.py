#!/usr/local/bin/python3
import sys
grid = {}
bestMdist = sys.maxsize
stepVal = {True:1, False:-1}
def setGrid(x,y,lineNum, step):
    global bestMdist
    #print "\t", x, y
    key = str(x)+'-'+str(y)
    val = grid.get(key, None)
    #print x, y, lineNum, step, val
    if lineNum == 1:
        if val == None:
            grid[key] = step
    elif val == None:
        pass
    else:
        #print "test it", bestMdist, val+step
        bestMdist = min(bestMdist, val+step)
def mkMove(step, lineNum, startX, endX, startY, endY):
    #print lineNum, startX, endX, startY, endY
    for x in range(startX, endX, stepVal[startX<=endX]):
        for y in range(startY, endY, stepVal[startY<=endY]):
            step = step + 1
            setGrid(x,y,lineNum, step)
    return step
#33303 too high and 562
with open("day03.txt",'r') as f:
#with open("day03test0.txt",'r') as f:
    lines = f.readlines()
    lineNum = 0
    minx, maxx, miny, maxy = 0,0,0,0
    setGrid(0,0,1, 0)
    for line in lines:
        lineNum = lineNum + 1
        #print "line", lineNum
        x, y, step = 0, 0, 0
        for move in line.split(","):
            direction = move[0:1]
            cnt = int(move[1:]) 
            #print "\t", direction, cnt
            if direction == "R":
                step = mkMove(step, lineNum, x+1, x+cnt+1, y, y+1)
                x = x + cnt
            elif direction == "L":
                step = mkMove(step, lineNum, x-1, x-cnt-1, y, y+1)
                x = x - cnt
            elif direction == "U":
                step = mkMove(step, lineNum, x, x+1, y+1, y+cnt+1)
                y = y + cnt
            elif direction == "D":
                step = mkMove(step, lineNum, x, x+1, y-1, y-cnt-1)
                y = y - cnt
    print bestMdist
    #print grid
