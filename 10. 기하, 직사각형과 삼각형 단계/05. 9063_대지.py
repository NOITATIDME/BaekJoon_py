N = int(input())

xList = []
yList = []

for i in range(N):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)


if N == 1:
    print(0)
else:
    print((max(xList) - min(xList)) * (max(yList) - min(yList)))
