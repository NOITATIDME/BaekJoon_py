M = int(input())
N = int(input())

data = []

for i in range(M, N+1):
    count = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                count += 1
        if count == 0:
            data.append(i)

if len(data) > 0:
    print(sum(data))
    print(min(data))
else:
    print(-1)