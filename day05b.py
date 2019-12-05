#!/usr/local/bin/python3
def computer(memory, noun, verb):
    def fetch(mode, val):
        if mode == 0:
            return memory.get(val)
        if mode == 1:
            return val
        print "unexpected mode ", mode, " with val=", val
        exit(0)
    def setMem(loc, val):
        memory[loc] = val
    pc = 0
    #memory[1], memory[2] = noun, verb
    while True:
        instruct, opPos1, opPos2, destPos = memory.get(pc, 0), memory.get(pc+1, 0), memory.get(pc+2, 0), memory.get(pc+3, 0)
        opCode = instruct % 100
        modes = instruct // 100
        if 99 == opCode:
            break
        elif 1 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            setMem(destPos, op1 + op2)
            pc = pc + 4
        elif 2 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            setMem(destPos, op1 * op2)
            pc = pc + 4
        elif 3 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = 5
            print "Operation 3: set ", op1, " to ", op2
            setMem(fetch(op1, 1), op2)
            pc = pc + 2
        elif 4 == opCode:
            val = fetch(modes % 10, opPos1)
            print "Program Output: ", val
            pc = pc + 2
        elif 5 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            if op1 != 0:
                pc = op2
            else:
                pc = pc + 3
        elif 6 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            if op1 == 0:
                pc = op2
            else:
                pc = pc + 3
        elif 7 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            if op1 < op2:
                setMem(destPos, 1)
            else:
                setMem(destPos, 0)
            pc = pc + 4
        elif 8 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
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
with open("day05.txt",'r') as f:
    startMemory = mkMemory(f.read())
    computer(startMemory, 42, 42)
'''
for noun in range(100):
    for verb in range(100):
        memory = computer(startMemory.copy(), noun, verb)
        if memory[0] == 19690720:
            print 100 * noun + verb
            exit()
'''
