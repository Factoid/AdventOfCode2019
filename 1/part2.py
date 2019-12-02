def calcFuel( mass ):
    f = int(mass/3) - 2
    if f <= 0: return 0
    return f + calcFuel(f)

totalFuel = 0
with open("input","r") as f:
    for line in f:
        mass = int(line)
        fuel = calcFuel(mass)
        totalFuel += fuel

print(totalFuel)
