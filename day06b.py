#!/usr/local/bin/python3
with open("day06.txt",'r') as f:
    parents, dists = {}, {}
    for line in f.readlines():
        parent, child = line.rstrip().split(")")
        parents[child] = parent            
    obj, dist, countdown = parents['YOU'], 0, {}
    while True:
        countdown[obj] = dist
        dist = dist + 1
        if obj == 'COM':
            break
        obj = parents[obj]
    obj, dist = parents['SAN'], 0
    while countdown.get(obj) == None:
        dist = dist + 1
        obj = parents[obj]
    print countdown[obj] + dist
