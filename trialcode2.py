import random

def PrintMatrix(TheArray):
    for x in range(10):
        for y in range(10):
            print(TheArray[x][y], " ", end='')
        print("")

ArrData = [[0] * 10 for i in range(10)]

for x in range(10):
    for y in range(10):
        ArrData[x][y] = random.randrange(100)

print("Unsorted array")
PrintMatrix(ArrData)
print("===========================================")

ArrayLength = 10

for x in range(0, ArrayLength):
    for y in range(0, ArrayLength-1):
        for z in range(0, ArrayLength - y - 1):
            if ArrData[x][z] > ArrData[x][z + 1]:
                Temp = ArrData[x][z]
                ArrData[x][z] = ArrData[x][z + 1]
                ArrData[x][z + 1] = Temp


print("Sorted array")
PrintMatrix(ArrData)
print("===========================================")

