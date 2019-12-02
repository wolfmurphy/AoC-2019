#!/usr/local/bin/python3
with open("input02.txt",'r') as f:
    #print(sum(list(map(fuelNeeded, map(int, f.readlines())))))
    line = f.read()
    #line = " 1,9,10,3,2,3,11,0,99,30,40,50"
    memory = list(map(int, line.split(",")))
    memoryLen = len(memory)
    memory = {i: memory[i] for i in range(0, memoryLen)}
pc = 0
memory[1], memory[2] = 12, 2
while True:
    opCode = memory[pc]
    opCode, opPos1, opPos2, destPos = memory.get(pc, 0), memory.get(pc+1, 0), memory.get(pc+2, 0), memory.get(pc+3, 0)
    op1, op2 = memory.get(opPos1, 0), memory.get(opPos2, 0)
    print pc, opCode, opPos1, opPos2, destPos, op1, op2
    if 99 == opCode:
        break
    elif 1 == opCode:
        memory[destPos] = op1 + op2
    elif 2 == opCode:
        memory[destPos] = op1 * op2
    else:
        print "bad opCode=", opCode, " at position ",pc+1
        exit()
    pc = pc + 4
    print list(memory[i] for i in range(0, memoryLen))
print memory[0]
print list(memory[i] for i in range(0, memoryLen))
