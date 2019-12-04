def mark_points(path):
    points = {}
    x = 0
    y = 0
    step = 0
    for val in path:
        d = val[0]
        amnt = int(val[1:])
        for i in range(amnt):
            if d == "U": y += 1
            elif d == "D": y -= 1
            elif d == "L": x -= 1
            elif d == "R": x += 1
            step += 1
            p = (x,y)
            if p not in points:
                points[p] = step
                
    return points

def manhattan( t ):
    return abs(t[0]) + abs(t[1])

paths = []
with open("input","r") as f:
    for line in f.readlines():
        paths.append(line.split(','))

set1 = mark_points(paths[0])
set2 = mark_points(paths[1])
cross = set(set1.keys()).intersection( set(set2.keys()) )
bestPoint, bestDist = min( [ (p, set1[p] + set2[p]) for p in cross ], key=lambda x: x[1] )
print(bestPoint,bestDist)
