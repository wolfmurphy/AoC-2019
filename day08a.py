#!/usr/local/bin/python3
with open("day08.txt",'r') as f:
#with open("day07test1b.txt",'r') as f:
    picture = f.read().rstrip() + 'z'
    layerNum = -1
    counts = {}
    min0, bestLayer,ans = 150, -1, -1
    for i in range(0,len(picture)):
        if i % 150 == 0:
            #print layerNum, counts.get('0',0), counts.get('1',0), counts.get('2',0)
            if layerNum >= 0:
                if min0 > counts.get('0',0):
                    min0 = counts.get('0',0)
                    bestLayer = layerNum
                    ans = counts.get('1',0)*counts.get('2',0)
            layerNum = layerNum + 1;
            counts = {}
        counts[picture[i]] = counts.get(picture[i], 0) + 1
    print ans
