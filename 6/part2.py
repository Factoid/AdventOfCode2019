from collections import deque

def chain( src ):
    ret = []
    while src in parents:
        src = parents[src]
        ret.append(src)
    return ret

def first_common( a, b ):
    for v in a:
        if v in b:
            return v
    return None

def distance_to( a, c ):
    i = 0
    for v in a:
        if v == c: return i
        i += 1
        
parents = {}
with open( "input", "r" ) as f:
    for line in f:
        a, b = line.strip().split(')')
        parents[b] = a

you = chain("YOU")
san = chain("SAN")
first_common = first_common(you,san)
dist_you = distance_to(you,first_common)
dist_san = distance_to(san,first_common)
print(dist_you+dist_san)
