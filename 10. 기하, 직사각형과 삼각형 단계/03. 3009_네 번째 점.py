xList = []
yList = []

for _ in range(3):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

for  i in range(3):
    if xList.count(xList[i]) == 1:
        x4 = xList[i]
    if yList.count(yList[i]) == 1:
        y4 = yList[i]

print(x4, y4)