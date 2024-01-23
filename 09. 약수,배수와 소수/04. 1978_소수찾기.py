N = int(input())
count = 0
line = list(input().split())
for i in range(N):
    x = int(line[i])
    y = 0
    for j in range(2,x):
        if x % j == 0:
            y += 1
    if y == 0:
        if x != 1:
            count += 1
print(count)