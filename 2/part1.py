def intcode(arr):
    for pos in range(0,len(arr),4):
        code = arr[pos]
        op1 = arr[pos+1]
        op2 = arr[pos+2]
        out = arr[pos+3]

        if code == 1:
            arr[out] = arr[op1] + arr[op2]
        elif code == 2:
            arr[out] = arr[op1] * arr[op2]
        elif code == 99:
            return 0
        else:
            print("Bad opt code at",pos)
            return 1 

arr = []
with open("input","r") as f:
    arr = [int(x) for x in f.read().split(',')]

arr[1] = 12
arr[2] = 2
ret = intcode(arr)
print(arr[0])
