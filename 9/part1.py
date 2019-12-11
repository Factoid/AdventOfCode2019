from collections import deque
from itertools import permutations

relbase = 0
input_buffer = None
output_buffer = None

def ensure_addr(addr,mem):
    if addr >= len(mem):
        mem.extend( [0]*(addr-len(mem)+1) )
    
def readparams(nparams, ip, mem, modes):
    global relbase
    vals = []
    for x in range(0,nparams):
        b = (modes//10**x) % 10
        if b == 0:
            addr = mem[ip+1+x]
            ensure_addr(addr,mem)
            val = mem[addr]
            vals.append( val )
        elif b == 1:
            val = mem[ip+1+x]
            vals.append( val )
        elif b == 2:
            addr = mem[ip+1+x] + relbase
            ensure_addr(addr,mem)
            val = mem[addr]
            vals.append( val )
    return vals

def writeout(val, pindex, ip, mem, modes):
    global relbase
    b = (modes//10**(pindex-1))
    addr = 0
    if b == 0:
        addr = mem[ip+pindex]
    elif b == 2:
        addr = mem[ip+pindex] + relbase
    ensure_addr(addr,mem)
    mem[addr] = val

def jump_if_true(mem,ip,modes):
    v, jmp = readparams(2, ip, mem, modes)
    if v != 0:
        return (0,jmp)
    else:
        return (0,ip+3)

def jump_if_false(mem,ip,modes):
    v, jmp = readparams(2, ip, mem, modes)
    if v == 0:
        return (0,jmp)
    else:
        return (0,ip+3)

def less_than(mem,ip,modes):
    a, b = readparams(2, ip, mem, modes)
    if a < b:
        writeout(1,3,ip,mem,modes)
    else:
        writeout(0,3,ip,mem,modes)
    return(0, ip+4)

def equals(mem,ip,modes):
    a, b = readparams(2, ip, mem, modes)
    if a == b:
        writeout(1,3,ip,mem,modes)
    else:
        writeout(0,3,ip,mem,modes)
    return(0, ip+4)
    
def read(mem,ip,modes):
    global input_buffer
    if input_buffer != None and len(input_buffer) > 0 :
        val = input_buffer.popleft()
    else:
        val = int(input("intput: "))
    writeout(val,1,ip,mem,modes)
    return (0,ip+2)

def write(mem,ip,modes):
    global output_buffer
    p1, = readparams(1, ip, mem, modes)
    if output_buffer != None:
        output_buffer.append(p1)
        return (1,ip+2)
    else:
        print(p1)
        return (0,ip+2)

def add(mem,ip,modes):
    p1, p2 = readparams(2, ip, mem, modes)
    writeout( p1 + p2, 3, ip, mem, modes)
    return (0,ip+4)

def mult(mem,ip,modes):
    p1, p2 = readparams(2, ip, mem, modes)
    writeout( p1 * p2, 3, ip, mem, modes)
    return (0,ip+4)

def halt(mem,ip,modes):
    return (-1,ip+1)

def adj_relbase(mem,ip,modes):
    global relbase
    adj, = readparams(1, ip, mem, modes)
    relbase += adj
    return (0,ip+2)

def intcode(mem,ip,codes,break_codes=[]):
    while True:
        val = str(mem[ip])
        opt = int(val[-2:])
        mask = val[:-2]
        modes = 0
        if mask != "": modes = int(mask)
        if opt not in codes: return -1
        #print("opt",opt,"ip",ip,"modes",modes)
        ret,ip = codes[opt](mem,ip,modes)
        if ret < 0 or ret in break_codes: return (ret,ip)
        
instructions = {1:add,2:mult,99:halt,3:read,4:write,5:jump_if_true,6:jump_if_false,7:less_than,8:equals,9:adj_relbase}

d = []
with open("input","r") as f:
    d = [int(x) for x in f.read().split(',')]

mem = d[:]
intcode(mem,0,instructions)
