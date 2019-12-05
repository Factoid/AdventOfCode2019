def doubleDigit(x):
    sequences = {}
    for c in range(len(x)-1):
        if x[c] == x[c+1]:
            if x[c] not in sequences:
                sequences[ x[c] ] = 2
            else:
                sequences[ x[c] ] += 1

    for val in sequences.values():
        if val == 2: return True
        
    return False

def incrementsOnly(x):
    for c in range(len(x)-1):
        if int(x[c]) > int(x[c+1]): return False

    return True

def satisfies( x ):
    if not doubleDigit(x): return False
    if not incrementsOnly(x): return False
    return True

n = 0
for x in range(245318,765747):
    if satisfies( str(x) ): n += 1
print(n)
