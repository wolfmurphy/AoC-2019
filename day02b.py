#!/usr/local/bin/python3
def computer(memory, noun, verb):
    pc = 0
    memory[1], memory[2] = noun, verb
    while True:
        opCode = memory[pc]
        opCode, opPos1, opPos2, destPos = memory.get(pc, 0), memory.get(pc+1, 0), memory.get(pc+2, 0), memory.get(pc+3, 0)
        op1, op2 = memory.get(opPos1, 0), memory.get(opPos2, 0)
        if 99 == opCode:
            break
        elif 1 == opCode:
            memory[destPos] = op1 + op2
            pc = pc + 4
        elif 2 == opCode:
            memory[destPos] = op1 * op2
            pc = pc + 4
        else:
            print "bad opCode=", opCode, " at position ", pc+1
            exit()
    return memory
def mkMemory(line):
    memory = list(map(int, line.split(",")))
    return {i: memory[i] for i in range(0, len(memory))}
with open("input02.txt",'r') as f:
    startMemory = mkMemory(f.read())
for noun in range(100):
    for verb in range(100):
        memory = computer(startMemory.copy(), noun, verb)
        if memory[0] == 19690720:
            print 100 * noun + verb
            exit()
