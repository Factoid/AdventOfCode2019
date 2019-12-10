import itertools

layers = []
with open( "input", "r") as f:
    while True:
        ch = f.read(25*6)
        if not ch: break
        layers.append(ch)

def pixel(layers, x, y):
    for l in layers:
        v = l[y*25+x]
        if v == '2': continue
        if v == '1': return '*'
        return ' '

for y in range(6):
    for x in range(25):
        print( pixel(layers,x,y), end='' )
    print()
