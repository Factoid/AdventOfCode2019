def calcFuel( mass ):
    return int(mass/3) - 2

totalFuel = 0
with open("input","r") as f:
    for line in f:
        mass = int(line)
        fuel = calcFuel(mass)
        totalFuel += fuel

print(totalFuel)
