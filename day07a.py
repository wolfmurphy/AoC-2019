#!/usr/local/bin/python3
def computer(memory, noun, verb, inputs):
    def fetch(mode, val):
        if mode == 0:
            return memory.get(val)
        if mode == 1:
            return val
        print "unexpected mode ", mode, " with val=", val
        exit(0)
    def setMem(loc, val):
        #print "setMem(",loc,",",val,")"
        memory[loc] = val
    pc = 0
    #memory[1], memory[2] = noun, verb
    inPtr = 0
    while True:
        instruct, opPos1, opPos2, destPos = memory.get(pc, 0), memory.get(pc+1, 0), memory.get(pc+2, 0), memory.get(pc+3, 0)
        opCode = instruct % 100
        modes = instruct // 100
        ##print  "instruction fetch", opCode, modes, opPos1, opPos2, destPos
        if 99 == opCode:
            break
        elif 1 == opCode: # add
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print "add (1) ", destPos,  op1 + op2, op1, op2
            setMem(destPos, op1 + op2)
            pc = pc + 4
        elif 2 == opCode: #multiply
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print "multiplty (2) ", destPos,  op1 * op2, op1, op2
            setMem(destPos, op1 * op2)
            pc = pc + 4
        elif 3 == opCode: 
            op2 = inputs[inPtr]
            inPtr = inPtr + 1
            #print "input (3) ", opPos1 , op2
            setMem(opPos1, op2)
            pc = pc + 2
        elif 4 == opCode:
            val = fetch(modes % 10, opPos1)
            #print "Program Output: ", val, " from ", inputs
            return val
            pc = pc + 2
        elif 5 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print " (5) ", op1 , op2
            if op1 != 0:
                pc = op2
            else:
                pc = pc + 3
        elif 6 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print " (6) ", op1 , op2
            if op1 == 0:
                pc = op2
            else:
                pc = pc + 3
        elif 7 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print " (7) ", op1 , op2
            if op1 < op2:
                setMem(destPos, 1)
            else:
                setMem(destPos, 0)
            pc = pc + 4
        elif 8 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            #print " (8) ", op1 , op2
            if op1 == op2:
                setMem(destPos, 1)
            else:
                setMem(destPos, 0)
            pc = pc + 4
        else:
            print "bad opCode=", opCode, " at position ", pc+1
            print memory
            exit()
    return memory
def mkMemory(line):
    memory = list(map(int, line.split(",")))
    return {i: memory[i] for i in range(0, len(memory))}
with open("day07.txt",'r') as f:
#with open("day07test1.txt",'r') as f:
    startMemory = mkMemory(f.read())
    curMax = 0
    noun, verb = 42, 42
    for c1 in range(0,5):
        #print "start c1=",c1
        ret1 = computer(startMemory.copy(), noun, verb, [c1, 0])
        #print "ret1=", ret1
        for c2 in range(0,5):
            if c1 == c2:
                continue
            #print "start c2=",c2
            ret2 = computer(startMemory.copy(), noun, verb, [c2, ret1])
            #print "ret2=", ret2
            for c3 in range(0,5):
                if c3 == c1 or c3 == c2:
                    continue
                #print "start c3=",c3
                ret3 = computer(startMemory.copy(), noun, verb, [c3, ret2])
                #print "ret3=", ret3
                for c4 in range(0,5):
                    if c4 == c1 or c4 == c2 or c4 == c3:
                        continue
                    #print "start c4=",c4
                    ret4 = computer(startMemory.copy(), noun, verb, [c4, ret3])
                    #print "ret4=", ret4
                    for c5 in range(0,5):
                        if c5 == c1 or c5 == c2 or c5 == c3 or c5 == c4:
                            continue
                        #print "start c5=",c5
                        ret5 = computer(startMemory.copy(), noun, verb, [c5, ret4])
                        #print "ret5=", ret5
                        curMax = max(curMax, ret5)
    print curMax
