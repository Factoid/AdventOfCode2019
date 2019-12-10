import itertools

layers = []
with open( "input", "r") as f:
    while True:
        ch = f.read(25*6)
        if not ch: break
        layers.append(ch)

counts = [ [ len(list(v)) for k,v in itertools.groupby(sorted(l))] for l in layers[:-1] ]
v = min( counts, key=lambda x: x[0] )
print(v[1]*v[2])

