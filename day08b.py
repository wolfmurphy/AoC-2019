#!/usr/local/bin/python3
with open("day08.txt",'r') as f:
#with open("day07test1b.txt",'r') as f:
    picture = f.read().rstrip()
    pic = ['2'] * 150
    layerNum = -1
    counts = {}
    max0, bestLayer,ans = -1, -1, -1
    for i in range(0,len(picture)):
        #print picture[i]
        j = i % 150
        c = picture[i]
        if pic[j] == '2':
            if picture[i] != '2':
                pic[j] = picture[i]
    s = ''
    for i in range(0,150):
        if i % 25 == 0:
            print s
            s = ''
        if pic[i] == '0':
            s = s + ' '
        else:
            s = s + 'X'
    print s
