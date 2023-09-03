N, M = map(int, input().split())
data = [i for i in range(1, N+1)]

for n in range(M):
    i, j = map(int, input().split())
    num = data[i-1]
    data[i-1] = data[j-1]
    data[j-1] = num

for i in range(N):
    print(data[i],end=" ")
