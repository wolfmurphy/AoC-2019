#!/usr/local/bin/python3
with open("day06.txt",'r') as f:
    children, dists = {}, {}
    for line in f.readlines():
        parent, child = line.rstrip().split(")")
        children[parent] = children.get(parent, []) 
        children[parent].append(child)
        children[child] = children.get(child, []) 
    todo, dists['COM'] = ['COM'], 0
    while len(todo) > 0:
        obj = todo.pop(0)
        dist = dists[obj] + 1
        for child in children[obj]:
            dists[child] = dist
            todo.append(child)
    print sum(dists.values())
