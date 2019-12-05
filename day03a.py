#!/usr/local/bin/python3
import sys
grid = {}
bestMdist = sys.maxsize
stepVal = {True:1, False:-1}
def setGrid(x,y,lineNum):
    global bestMdist
    #print "\t", x, y
    key = str(x)+'-'+str(y)
    val = grid.get(key, lineNum)
    grid[key] = lineNum
    if val == lineNum:
        return
    if x == 0 and y == 0:
        return
    bestMdist = min(bestMdist, abs(x) + abs(y))
def mkMove(lineNum, startX, endX, startY, endY):
    #print lineNum, startX, endX, startY, endY
    for x in range(startX, endX, stepVal[startX<=endX]):
        for y in range(startY, endY, stepVal[startY<=endY]):
            setGrid(x,y,lineNum)
#33303 too high and 562
with open("day03.txt",'r') as f:
#with open("day03test2.txt",'r') as f:
    lines = f.readlines()
    lineNum = 0
    minx, maxx, miny, maxy = 0,0,0,0
    for line in lines:
        lineNum = lineNum + 1
        #print "line", lineNum
        x, y = 0, 0
        for move in line.split(","):
            direction = move[0:1]
            cnt = int(move[1:]) 
            #print "\t", direction, cnt
            if direction == "R":
                mkMove(lineNum, x+1, x+cnt+1, y, y+1)
                x = x + cnt
            elif direction == "L":
                mkMove(lineNum, x-1, x-cnt-1, y, y+1)
                x = x - cnt
            elif direction == "U":
                mkMove(lineNum, x, x+1, y+1, y+cnt+1)
                y = y + cnt
            elif direction == "D":
                mkMove(lineNum, x, x+1, y-1, y-cnt-1)
                y = y - cnt
    print bestMdist
    #print grid
