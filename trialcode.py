import random

ArrData = [[0]*10 for i in range(10)]

for x in range(10):
    for y in range(10):
        ArrData[x][y] = random.randrange(100)

for j in ArrData:
    print(j)