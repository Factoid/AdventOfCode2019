from collections import deque
from itertools import permutations

def readparams(nparams, ip, mem, modes):
    vals = []
    for x in range(0,nparams):
        b = modes & (1<<x)
        if b == 0:  
            addr = mem[ip+1+x]
            val = mem[addr]
            vals.append( val )
        else:
            val = mem[ip+1+x]
            vals.append( val )
            
    return vals

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
    out = mem[ip+3]
    if a < b:
        mem[out] = 1
    else:
        mem[out] = 0
    return(0, ip+4)

def equals(mem,ip,modes):
    a, b = readparams(2, ip, mem, modes)
    out = mem[ip+3]
    if a == b:
        mem[out] = 1
    else:
        mem[out] = 0
    return(0, ip+4)
    
def read(mem,ip,modes):
    if len(input_buffer) > 0 :
        val = input_buffer.popleft()
    else:
        val = int(input("intput: "))
    mem[mem[ip+1]] = val
    return (0,ip+2)

def write(mem,ip,modes):
    p1, = readparams(1, ip, mem, modes)
    if output_buffer != None:
        output_buffer.append(p1)
        return (1,ip+2)
    else:
        print(p1)
        return (0,ip+2)

def add(mem,ip,modes):
    p1, p2 = readparams(2, ip, mem, modes)
    out = mem[ip+3]
    mem[out] = p1 + p2
    return (0,ip+4)

def mult(mem,ip,modes):
    p1, p2 = readparams(2, ip, mem, modes)
    out = mem[ip+3]
    mem[out] = p1 * p2
    return (0,ip+4)

def halt(mem,ip,modes):
    return (-1,ip+1)

def intcode(mem,ip,codes,break_codes=[]):
    while True:
        val = str(mem[ip])
        opt = int(val[-2:])
        mask = val[:-2]
        modes = 0
        if mask != "": modes = int(mask,2)
        if opt not in codes: return -1
        ret,ip = codes[opt](mem,ip,modes)
        if ret < 0 or ret in break_codes: return (ret,ip)
        
instructions = {1:add,2:mult,99:halt,3:read,4:write,5:jump_if_true,6:jump_if_false,7:less_than,8:equals}

d = []
with open("input","r") as f:
    d = [int(x) for x in f.read().split(',')]

bestThrust = 0
bestInputs = None
phase_inputs = [5,6,7,8,9]

for perm in permutations(phase_inputs):
    states = deque( (d[:],0) for x in range(len(phase_inputs)) )
    phase_values = deque( perm )
    input_buffer = deque()
    output_buffer = deque( [0] )
    
    while len(states) > 0:
        if len(phase_values) > 0: input_buffer.append( phase_values.popleft() )
        if len(output_buffer) > 0: input_buffer.append( output_buffer.popleft() )
        mem, ip = states.popleft()
        ret, ip = intcode(mem,ip,instructions,[1])
        if ret > 0: states.append( (mem,ip) )
 
    thrust = input_buffer.popleft()
    if thrust > bestThrust:
        bestThrust = thrust
        bestInputs = perm
        
print(bestInputs, bestThrust)
