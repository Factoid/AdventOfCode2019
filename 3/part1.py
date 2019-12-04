def mark_points(path):
    points = set()
    x = 0
    y = 0
    for val in path:
        d = val[0]
        amnt = int(val[1:])
        for i in range(amnt):
            if d == "U": y += 1
            elif d == "D": y -= 1
            elif d == "L": x -= 1
            elif d == "R": x += 1
            
            points.add( (x,y) )

    return points

def manhattan( t ):
    return abs(t[0]) + abs(t[1])

paths=[]
with open("input","r") as f:
    for line in f.readlines():
        paths.append(line.split(','))
            
set1 = mark_points(paths[0])
set2 = mark_points(paths[1])
cross = set1.intersection(set2)
closest = min(cross,key=manhattan)
print(closest, manhattan(closest))
