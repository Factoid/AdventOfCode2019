from collections import deque

orbits = {}
with open( "input", "r" ) as f:
    for line in f:
        a, b = line.strip().split(')')
        if a in orbits:
            orbits[a].append(b)
        else:
            orbits[a] = [b]

total = 0
seq = deque( [("COM",0)] )
while len(seq) > 0:
    v, n = seq.popleft()
    total += n
    if v in orbits:
        seq.extend( [ (x,n+1) for x in orbits[v] ] )
print(total)
        
