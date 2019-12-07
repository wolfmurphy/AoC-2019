#!/usr/local/bin/python3
debug = False
def dprint(*argv):
    if debug:
        for arg in argv:  
            print " ".join(map(str,argv))
    return
def computer(memory, pc, inputSoFar):
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
    outputSoFar = []
    dprint (memory)
    while True:
        instruct, opPos1, opPos2, destPos = memory.get(pc, 0), memory.get(pc+1, 0), memory.get(pc+2, 0), memory.get(pc+3, 0)
        opCode = instruct % 100
        modes = instruct // 100
        ##print  "instruction fetch", opCode, modes, opPos1, opPos2, destPos
        if 99 == opCode:
            return None, None, outputSoFar, False
        elif 1 == opCode: # add
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 1: (",destPos,") <- ", op1 + op2, " = ", op1, " + ", op2)
            setMem(destPos, op1 + op2)
            pc = pc + 4
        elif 2 == opCode: #multiply
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 2: (",destPos,") <- ", op1 * op2, " = ", op1, " * ", op2)
            setMem(destPos, op1 * op2)
            pc = pc + 4
        elif 3 == opCode:
            if len(inputSoFar) == 0:
                return memory, pc, outputSoFar, True
            nextInput = inputSoFar.pop(0)
            dprint ("op 3: (",opPos1,") <- ", nextInput)
            setMem(opPos1, nextInput)
            pc = pc + 2
        elif 4 == opCode:
            val = fetch(modes % 10, opPos1)
            dprint ("op 4: outputing ", val) 
            outputSoFar.append(val)
            pc = pc + 2
        elif 5 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 5: jump to ", op2, ": if ", op1, " != 0")
            if op1 != 0:
                pc = op2
            else:
                pc = pc + 3
        elif 6 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 6: jump to ", op2, ": if ", op1, " == 0")
            if op1 == 0:
                pc = op2
            else:
                pc = pc + 3
        elif 7 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 7: (",destPos,") <- 1(or 0) if ", op1, " < ", op2) 
            if op1 < op2:
                setMem(destPos, 1)
            else:
                setMem(destPos, 0)
            pc = pc + 4
        elif 8 == opCode:
            op1 = fetch(modes % 10, opPos1)
            op2 = fetch((modes//10) % 10, opPos2)
            dprint ("op 8: (",destPos,") <- 1(or 0) if ", op1, " == ", op2) 
            if op1 == op2:
                setMem(destPos, 1)
            else:
                setMem(destPos, 0)
            pc = pc + 4
        else:
            print "bad opCode=", opCode, " at position ", pc+1
            print memory
            exit()
def mkMemory(line):
    memory = list(map(int, line.split(",")))
    return {i: memory[i] for i in range(0, len(memory))}
def runAmps(mem, phase):
    start1, start2, start3, start4, start5 = phase[0:1], phase[1:2], phase[2:3], phase[3:4], phase[4:5]
    mem1, mem2, mem3, mem4, mem5 = mem.copy(), mem.copy(), mem.copy(), mem.copy(), mem.copy()
    pc1, pc2, pc3, pc4, pc5 = 0, 0, 0, 0, 0
    retVal = [0]
    keepGoing = True
    newOutput = [0]
    while keepGoing:
        dprint ("----\nStart amplifier 1 at ", pc1, " with ", start1, newOutput)
        mem1, pc1, newOutput, newHalt = computer(mem1, pc1, start1 + newOutput)
        keepGoing = keepGoing and newHalt

        dprint ("----\nStart amplifier 2 at ", pc2, " with ", start2, newOutput)
        mem2, pc2, newOutput, newHalt = computer(mem2, pc2, start2 + newOutput)
        keepGoing = keepGoing and newHalt

        dprint ("----\nStart amplifier 3 at ", pc3, " with ", start3, newOutput)
        mem3, pc3, newOutput, newHalt = computer(mem3, pc3, start3 + newOutput)
        keepGoing = keepGoing and newHalt

        dprint ("----\nStart amplifier 4 at ", pc4, " with ", start4, newOutput)
        mem4, pc4, newOutput, newHalt = computer(mem4, pc4, start4 + newOutput)
        keepGoing = keepGoing and newHalt

        dprint ("----\nStart amplifier 5 at ", pc5, " with ", start5, newOutput)
        mem5, pc5, newOutput, newHalt = computer(mem5, pc5, start5 + newOutput)
        keepGoing = keepGoing and newHalt

        retVal = retVal + newOutput
        start1, start2, start3, start4, start5 = [], [], [], [], []
    return retVal[-1]
dprint("------------------------------------------------------------------------------------------")
with open("day07.txt",'r') as f:
#with open("day07test1b.txt",'r') as f:
    startMemory = mkMemory(f.read())
    curMax = 0
    noun, verb = 42, 42
    for c1 in range(5,10):
        for c2 in range(5,10):
            if c1 == c2:
                continue
            for c3 in range(5,10):
                if c3 == c1 or c3 == c2:
                    continue
                for c4 in range(5,10):
                    if c4 == c1 or c4 == c2 or c4 == c3:
                        continue
                    for c5 in range(5,10):
                        if c5 == c1 or c5 == c2 or c5 == c3 or c5 == c4:
                            continue
                        curMax = max(curMax, runAmps(startMemory, [c1,c2,c3,c4,c5]))
    print curMax
#too low 2728444
